from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Vendor, Shipment, Base
from scoring import calc_score, check_cert

Base.metadata.create_all(bind=engine)

app = FastAPI()

# needed so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/vendors")
def get_vendors(db: Session = Depends(get_db)):
    vendors = db.query(Vendor).all()
    result = []
    for v in vendors:
        score = calc_score(v)
        cert_status = check_cert(v.certification, v.cert_year)
        result.append({
            "id": v.id,
            "name": v.name,
            "carbon_per_shipment": v.carbon_per_shipment,
            "certification": v.certification,
            "cert_status": cert_status,
            "score": score
        })
    return result


@app.get("/vendors/{vendor_id}/carbon-score")
def get_carbon_score(vendor_id: int, db: Session = Depends(get_db)):
    v = db.query(Vendor).filter(Vendor.id == vendor_id).first()
    if not v:
        return {"error": "vendor not found"}
  
    return {
        "vendor": v.name,
        "score": calc_score(v),
        "cert_status": check_cert(v.certification, v.cert_year)
    }


@app.get("/shipments")
def get_shipments(db: Session = Depends(get_db)):
    shipments = db.query(Shipment).all()
    return shipments

@app.get("/dashboard/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    vendors = db.query(Vendor).all()
    shipments = db.query(Shipment).all()
    total_carbon = sum(s.carbon_emitted for s in shipments)
    avg_score = sum(calc_score(v) for v in vendors) / len(vendors)
    best = max(vendors, key=lambda v: calc_score(v))
    
    return {
        "total_vendors": len(vendors),
        "total_shipments": len(shipments),
        "total_carbon_emitted": round(total_carbon, 2),
        "avg_sustainability_score": round(avg_score, 1),
        "best_vendor": best.name
    }

@app.post("/vendors")
def add_vendor(data: dict, db: Session = Depends(get_db)):
    new_v = Vendor(**data)
    db.add(new_v)
    db.commit()
    return {"msg": "vendor added"}
