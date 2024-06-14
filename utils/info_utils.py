from utils.core_utils import CoreUtils

class InfoUtils(CoreUtils):
    @staticmethod
    def is_camel_case(s):
        import re
        return bool(re.match(r'^[a-z]+([A-Z][a-z]*)*$', s))
