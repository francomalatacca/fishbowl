import json

def read_spec(spec_path):
    try:
        with open(spec_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading spec file {spec_path}: {e}")
        return None
