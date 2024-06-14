import re

date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

def check_date_format(paths):
    try:
        issues = []
        for path, methods in paths.items():
            for method, details in methods.items():
                parameters = details.get('parameters', [])
                for param in parameters:
                    if param['in'] == 'query' and ('date' in param['name'].lower() or param['name'].lower().startswith('date') or param['name'].lower().endswith('date')):
                        if not date_pattern.match(param.get('example', '')):
                            issues.append(f"Query parameter '{param['name']}' in path '{path}' does not follow the YYYY-MM-DD format.")
                request_body = details.get('requestBody', {}).get('content', {}).get('application/json', {}).get('schema', {}).get('properties', {})
                for key, value in request_body.items():
                    if 'date' in key.lower() or key.lower().startswith('date') or key.lower().endswith('date'):
                        if 'example' in value and not date_pattern.match(value['example']):
                            issues.append(f"Model property '{key}' in path '{path}' does not follow the YYYY-MM-DD format.")
        if issues:
            return False, " | ".join(issues), 'error'
        return True, "All dates are in YYYY-MM-DD format.", 'success'
    except Exception as e:
        return False, f"Exception in check_date_format: {e}", 'error'
