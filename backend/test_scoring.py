# quick tests to make sure scoring works
from scoring import calc_score, check_cert

# fake vendor object for testing
class FakeVendor:
    def __init__(self, carbon, cert, cert_year, eco, total):
        self.carbon_per_shipment = carbon
        self.certification = cert
        self.cert_year = cert_year
        self.on_time_eco_deliveries = eco
        self.total_deliveries = total

def test_good_vendor():
    v = FakeVendor(9.1, "CarbonNeutral", 2024, 48, 50)
    assert calc_score(v) >= 70  # should be high
    print("good vendor test passed")

def test_bad_vendor():
    v = FakeVendor(55.2, "None", 2019, 5, 50)
    assert calc_score(v) < 30  # should be low
    print("bad vendor test passed")

def test_cert_check():
    assert check_cert("None", 2020) == "Unverified"
    assert check_cert("CarbonNeutral", 2024) == "Verified ✅"
    assert check_cert("Expired", 2021) == "Unreliable ❌"
    print("cert check test passed")

test_good_vendor()
test_bad_vendor()
test_cert_check()
print("all tests passed ✅")