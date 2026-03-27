from sqlalchemy import Column, Integer, String, Float
from database import Base

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    carbon_per_shipment = Column(Float)
    certification = Column(String)
    cert_year = Column(Integer)
    on_time_eco_deliveries = Column(Integer)
    total_deliveries = Column(Integer)

class Shipment(Base):
    __tablename__ = "shipments"
    id = Column(Integer, primary_key=True)
    vendor_id = Column(Integer)
    route = Column(String)
    carbon_emitted = Column(Float)
    date = Column(String)
    status = Column(String)
