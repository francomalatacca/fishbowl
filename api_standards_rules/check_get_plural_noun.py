from utils.paths_utils import PathsUtils

paths_utils = PathsUtils()

def check_get_plural_noun(paths):
    try:
        issues = []
        for path, methods in paths.items():
            path_segments = path.strip('/').split('/')
            resource_name = path_segments[-1]  # Assuming the resource name is the last segment
            for method in methods.keys():
                if method.lower() == 'get' and not paths_utils.is_noun_and_plural(resource_name):
                    issues.append(f"Resource name '{resource_name}' in path '{path}' must be a plural noun for GET method.")
        if issues:
            return False, " | ".join(issues), 'error'
        return True, "All resource names for GET methods are plural nouns.", 'success'
    except Exception as e:
        return False, f"Exception in check_get_plural_noun: {e}", 'error'
