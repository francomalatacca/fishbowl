from config_loader import get_configuration

def check_required_headers(paths):
    description = "Certain headers must be present in request and response headers."
    try:
        config = get_configuration('required_headers', {})
        request_headers = config.get('request_headers', {})
        response_headers = config.get('response_headers', {})
        errors = []

        for path, methods in paths.items():
            for method, details in methods.items():
                # Check request headers
                if method.lower() == 'get' or method.lower() == 'post':  # Adjust methods as necessary
                    if 'parameters' in details:
                        headers = [param['name'] for param in details['parameters'] if param['in'] == 'header']
                        for header, level in request_headers.items():
                            if header not in headers:
                                errors.append((header, path, 'request', level))
                
                # Check response headers
                if 'responses' in details:
                    for response in details['responses'].values():
                        if 'headers' in response:
                            headers = response['headers'].keys()
                            for header, level in response_headers.items():
                                if header not in headers:
                                    errors.append((header, path, 'response', level))

        if errors:
            messages = []
            levels = []
            for header, path, req_res, level in errors:
                message = f"{req_res.capitalize()} header '{header}' missing in {req_res} for path '{path}'."
                messages.append(message)
                levels.append(level)

            # Determine the most severe level among errors
            if 'error' in levels:
                final_level = 'error'
            elif 'warning' in levels:
                final_level = 'warning'
            else:
                final_level = 'info'

            return False, " | ".join(messages), final_level
        return True, "All required headers are present.", 'success'
    except Exception as e:
        return False, f"Exception in check_required_headers: {e}", 'error'

rules = [
    {
        'target': 'paths',
        'func': check_required_headers,
        'name': 'required_headers',
        'description': 'Certain headers must be present in request and response headers.',
        'doc_url': 'https://example.com/docs/required_headers'
    }
]
