import json
import os

PROFILE_FILE = "data/profile.json"

def profile_exists():
    return os.path.exists(PROFILE_FILE)

def save_profile(profile):
    with open(PROFILE_FILE, "w") as file:
        json.dump(profile, file, indent=4)

def load_profile():
    with open(PROFILE_FILE, "r") as file:
        return json.load(file)