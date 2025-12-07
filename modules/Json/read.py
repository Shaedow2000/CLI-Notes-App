import os
import json

def readFile(path):
    full_path = f"data/{path}"

    if not os.path.exists(full_path):
        # Create folders if they don't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Create empty JSON file
        with open(full_path, "w") as f:
            json.dump({}, f)

    with open(full_path, "r") as file:
        return json.load(file)
