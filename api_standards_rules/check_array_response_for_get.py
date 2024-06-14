def check_array_response_for_get(paths):
    try:
        issues = []
        for path, methods in paths.items():
            if '{' not in path and '}' not in path:  # Check if there are no path parameters (identifiers)
                for method, details in methods.items():
                    if method.lower() == 'get':  # Only check GET methods
                        responses = details.get('responses', {})
                        for status_code, response in responses.items():
                            content = response.get('content', {})
                            for content_type, schema in content.items():
                                if schema.get('schema', {}).get('type') != 'array':
                                    issues.append(f"Path '{path}' for method '{method}' should return an array but it does not.")
        if issues:
            return False, " | ".join(issues), 'error'
        return True, "All appropriate GET paths return arrays.", 'success'
    except Exception as e:
        return False, f"Exception in check_array_response_for_get: {e}", 'error'
