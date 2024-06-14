from config_loader import get_configuration
from utils.paths_utils import PathsUtils

paths_utils = PathsUtils()

def check_query_string_format(paths):
    description = "Query parameter names must be in camelCase or kebab-case based on configuration."
    try:
        for path, methods in paths.items():
            for method, details in methods.items():
                parameters = details.get('parameters', [])
                for param in parameters:
                    if param['in'] == 'query':
                        format_type = get_configuration('querystring_format.format')
                        if format_type == 'camelCase' and not paths_utils.is_camel_case(param['name']):
                            return False, f"Query parameter '{param['name']}' in path '{path}' must be in camelCase.", 'error'
                        elif format_type == 'kebabCase' and not paths_utils.is_kebab_case(param['name']):
                            return False, f"Query parameter '{param['name']}' in path '{path}' must be in kebabCase.", 'error'
        return True, "All query parameters are correctly formatted.", 'success'
    except Exception as e:
        return False, f"Exception in check_query_string_format: {e}", 'error'

rules = [
    {
        'target': 'paths', 
        'func': check_query_string_format, 
        'name': 'querystring_format',
        'description': 'Query parameter names must be in camelCase or kebab-case based on configuration.'
    }
]
