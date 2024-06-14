import os
import importlib.util

def load_custom_rules(directory='custom_rules'):
    rules = []
    for filename in os.listdir(directory):
        if filename.endswith('_rules.py'):
            filepath = os.path.join(directory, filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], filepath)
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
                rules.extend(module.rules)
            except Exception as e:
                print(f"Failed to load rule from {filepath}: {e}")
    return rules
    