import unittest
from api_standards_rules.check_array_response_for_get import check_array_response_for_get

class TestCheckArrayResponseForGet(unittest.TestCase):
    def test_array_response_correct(self):
        paths = {
            '/v1/accounts': {
                'get': {
                    'responses': {
                        '200': {
                            'description': 'A list of accounts',
                            'content': {
                                'application/json': {
                                    'schema': {
                                        'type': 'array',
                                        'items': {
                                            '$ref': '#/components/schemas/Account'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        result, message, level = check_array_response_for_get(paths)
        self.assertTrue(result)
        self.assertEqual(message, "All appropriate GET paths return arrays.")
        self.assertEqual(level, 'success')

    def test_array_response_incorrect(self):
        paths = {
            '/v1/accounts': {
                'get': {
                    'responses': {
                        '200': {
                            'description': 'A list of accounts',
                            'content': {
                                'application/json': {
                                    'schema': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {'type': 'string'},
                                            'name': {'type': 'string'}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        result, message, level = check_array_response_for_get(paths)
        self.assertFalse(result)
        self.assertIn("Path '/v1/accounts' for method 'get' should return an array but it does not.", message)
        self.assertEqual(level, 'error')

    def test_array_response_with_identifier(self):
        paths = {
            '/v1/accounts/{accountId}': {
                'get': {
                    'responses': {
                        '200': {
                            'description': 'Account details',
                            'content': {
                                'application/json': {
                                    'schema': {
                                        '$ref': '#/components/schemas/Account'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        result, message, level = check_array_response_for_get(paths)
        self.assertTrue(result)
        self.assertEqual(message, "All appropriate GET paths return arrays.")
        self.assertEqual(level, 'success')

    def test_array_response_empty_paths(self):
        paths = {}
        result, message, level = check_array_response_for_get(paths)
        self.assertTrue(result)
        self.assertEqual(message, "All appropriate GET paths return arrays.")
        self.assertEqual(level, 'success')

if __name__ == '__main__':
    unittest.main()
