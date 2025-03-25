import json

FILE = "costs.json"

def save_cost(amount):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    data.append(amount)
    with open(FILE, "w") as f:
        json.dump(data, f)

def load_costs():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
