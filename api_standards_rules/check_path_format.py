from config_loader import get_configuration
from utils.paths_utils import PathsUtils

paths_utils = PathsUtils()

def check_path_format(paths):
    try:
        for path in paths.keys():
            path_segments = path.strip('/').split('/')
            for segment in path_segments:
                format_type = get_configuration('path_format.format')
                if format_type == 'kebabCase' and not paths_utils.is_kebab_case(segment):
                    return False, f"Path segment '{segment}' in path '{path}' must be in kebab-case.", 'error'
        return True, "All path segments are correctly formatted in kebab-case.", 'success'
    except Exception as e:
        return False, f"Exception in check_path_format: {e}", 'error'
