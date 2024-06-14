from utils.paths_utils import PathsUtils

paths_utils = PathsUtils()

def check_post_verb(paths):
    try:
        issues = []
        for path, methods in paths.items():
            path_segments = path.strip('/').split('/')
            resource_name = path_segments[-1]  # Assuming the resource name is the last segment
            if paths_utils.is_verb(resource_name):
                for method in methods.keys():
                    if method.lower() != 'post':
                        issues.append(f"Resource name '{resource_name}' in path '{path}' must use POST method because it is a verb.")
        if issues:
            return False, " | ".join(issues), 'error'
        return True, "All resource names that are verbs use POST method.", 'success'
    except Exception as e:
        return False, f"Exception in check_post_verb: {e}", 'error'
