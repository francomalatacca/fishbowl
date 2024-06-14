from .check_query_string_format import check_query_string_format
from .check_path_format import check_path_format
from .check_required_headers import check_required_headers
from .check_get_plural_noun import check_get_plural_noun
from .check_post_verb import check_post_verb
from .check_resource_version import check_resource_version
from .check_resource_lowercase import check_resource_lowercase
from .check_date_format import check_date_format
from .check_array_response_for_get import check_array_response_for_get

rules = [
    {
        'target': 'paths',
        'func': check_query_string_format,
        'name': 'querystring_format',
        'description': 'Query parameter names must be in camelCase or kebab-case based on configuration.',
        'doc_url': 'https://example.com/docs/querystring_format'
    },
    {
        'target': 'paths',
        'func': check_path_format,
        'name': 'path_format',
        'description': 'Path segments must be in kebab-case.',
        'doc_url': 'https://example.com/docs/path_format'
    },
    {
        'target': 'paths',
        'func': check_required_headers,
        'name': 'required_headers',
        'description': 'Certain headers must be present in request and response headers.',
        'doc_url': 'https://example.com/docs/required_headers'
    },
    {
        'target': 'paths',
        'func': check_get_plural_noun,
        'name': 'get_plural_noun',
        'description': 'Resource names for GET methods must be plural nouns.',
        'doc_url': 'https://example.com/docs/get_plural_noun'
    },
    {
        'target': 'paths',
        'func': check_post_verb,
        'name': 'post_verb',
        'description': 'Resource names that are verbs must use POST method.',
        'doc_url': 'https://example.com/docs/post_verb'
    },
    {
        'target': 'paths',
        'func': check_resource_version,
        'name': 'resource_version',
        'description': 'Paths must start with a valid version segment (e.g., "v1").',
        'doc_url': 'https://example.com/docs/resource_version'
    },
    {
        'target': 'paths',
        'func': check_resource_lowercase,
        'name': 'resource_lowercase',
        'description': 'Resource names must be lowercase.',
        'doc_url': 'https://example.com/docs/resource_lowercase'
    },
    {
        'target': 'paths',
        'func': check_date_format,
        'name': 'date_format',
        'description': 'Date fields must follow the YYYY-MM-DD format.',
        'doc_url': 'https://example.com/docs/date_format'
    },
    {
        'target': 'paths',
        'func': check_array_response_for_get,
        'name': 'array_response_for_get',
        'description': 'GET methods without identifiers in the path must return an array.',
        'doc_url': 'https://example.com/docs/array_response_for_get'
    }
]
