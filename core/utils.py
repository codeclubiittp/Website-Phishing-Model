import json

def load_settings(filepath="config/settings.json"):
    with open(filepath, "r") as f:
        return json.load(f)