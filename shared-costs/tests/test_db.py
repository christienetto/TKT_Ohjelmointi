
from shared_costs.db import save_cost, load_costs

def test_save_and_load():
    save_cost("10")
    assert "10" in load_costs()
