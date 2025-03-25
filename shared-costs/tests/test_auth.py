from shared_costs.auth import login

def test_login():
    assert login("user", "password")
    assert not login("wrong", "pass")
