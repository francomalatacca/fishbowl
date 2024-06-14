import os
import yaml
import json

def load_openapi_spec(file_path: str) -> dict:
    """
    Load OpenAPI specification from a file.
    
    Parameters:
    - file_path: Path to the OpenAPI specification file (YAML or JSON)
    
    Returns:
    - A dictionary containing the OpenAPI specification
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        with open(file_path, 'r') as file:
            if file_path.endswith('.yaml') or file_path.endswith('.yml'):
                spec = yaml.safe_load(file)
            elif file_path.endswith('.json'):
                spec = json.load(file)
            else:
                raise ValueError("Unsupported file format. Only YAML and JSON are supported.")
        
        return spec

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return {}
    except ValueError as e:
        print(f"Error: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while loading the OpenAPI spec: {e}")
        return {}
