import re

def check_resource_version(paths):
    try:
        issues = []
        version_pattern = re.compile(r'^v\d+$')
        for path in paths.keys():
            path_segments = path.strip('/').split('/')
            if len(path_segments) < 2 or not version_pattern.match(path_segments[0]):
                issues.append(f"Path '{path}' does not start with a valid version segment (e.g., 'v1').")
        if issues:
            return False, " | ".join(issues), 'error'
        return True, "All paths start with a valid version segment.", 'success'
    except Exception as e:
        return False, f"Exception in check_resource_version: {e}", 'error'
