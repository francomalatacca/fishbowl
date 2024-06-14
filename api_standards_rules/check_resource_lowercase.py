def check_resource_lowercase(paths):
    try:
        issues = []
        for path in paths.keys():
            path_segments = path.strip('/').split('/')
            for segment in path_segments:
                if segment != segment.lower():
                    issues.append(f"Resource name '{segment}' in path '{path}' must be lowercase.")
        if issues:
            return False, " | ".join(issues), 'error'
        return True, "All resource names are lowercase.", 'success'
    except Exception as e:
        return False, f"Exception in check_resource_lowercase: {e}", 'error'
