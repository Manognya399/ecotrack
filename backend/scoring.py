# scoring logic for vendor sustainability
# formula decided by us, can be improved later

def calc_score(vendor):
    score = 0

    # carbon score - lower carbon = better (max 40 pts)
    # we set 60 as the worst possible carbon value
    co2_val = vendor.carbon_per_shipment
    if co2_val <= 10:
        score += 40
    elif co2_val <= 20:
        score += 30
    elif co2_val <= 35:
        score += 20
    elif co2_val <= 50:
        score += 10
    else:
        score += 0  # worst case

    # certification score (max 30 pts)
    cert = vendor.certification
    if cert == "CarbonNeutral":
        score += 30
    elif cert == "ISO14001":
        score += 25
    elif cert == "Expired":
        score += 5
    else:
        score += 0  # no cert

    # on time eco deliveries (max 30 pts)
    # ratio of eco deliveries to total
    if vendor.total_deliveries > 0:
        ratio = vendor.on_time_eco_deliveries / vendor.total_deliveries
    else:
        ratio = 0

    score += round(ratio * 30)

    return score  # out of 100


def check_cert(cert_name, cert_year):
    # idk if 2 years is the right threshold but seems reasonable
    if cert_name == "None" or cert_name is None:
        return "Unverified"

    current_year = 2025
    age = current_year - cert_year

    if cert_name == "Expired":
        return "Unreliable ❌"
    elif age > 2:
        return "Outdated ⚠️"
    else:
        return "Verified ✅"