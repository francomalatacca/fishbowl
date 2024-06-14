import unittest
from api_standards_rules.check_date_format import check_date_format

class TestCheckDateFormat(unittest.TestCase):
    def test_dates_correct_format(self):
        paths = {
            '/v1/accounts': {
                'get': {
                    'parameters': [
                        {'name': 'start_date', 'in': 'query', 'example': '2023-05-01'},
                        {'name': 'end_date', 'in': 'query', 'example': '2023-06-01'}
                    ],
                    'requestBody': {
                        'content': {
                            'application/json': {
                                'schema': {
                                    'properties': {
                                        'creation_date': {'type': 'string', 'example': '2023-01-01'}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        result, message, level = check_date_format(paths)
        self.assertTrue(result)
        self.assertEqual(message, "All dates are in YYYY-MM-DD format.")
        self.assertEqual(level, 'success')

    def test_dates_incorrect_format(self):
        paths = {
            '/v1/accounts': {
                'get': {
                    'parameters': [
                        {'name': 'start_date', 'in': 'query', 'example': '2023-05-01'},
                        {'name': 'end_date', 'in': 'query', 'example': '06-01-2023'}
                    ],
                    'requestBody': {
                        'content': {
                            'application/json': {
                                'schema': {
                                    'properties': {
                                        'creation_date': {'type': 'string', 'example': '01-01-2023'}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        result, message, level = check_date_format(paths)
        self.assertFalse(result)
        self.assertIn("06-01-2023", message)
        self.assertIn("01-01-2023", message)
        self.assertEqual(level, 'error')

    def test_dates_incorrect_key_format(self):
        paths = {
            '/v1/accounts': {
                'get': {
                    'parameters': [
                        {'name': 'date_start', 'in': 'query', 'example': '2023-05-01'},
                        {'name': 'enddate', 'in': 'query', 'example': '06-01-2023'}
                    ],
                    'requestBody': {
                        'content': {
                            'application/json': {
                                'schema': {
                                    'properties': {
                                        'creationdate': {'type': 'string', 'example': '01-01-2023'}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        result, message, level = check_date_format(paths)
        self.assertFalse(result)
        self.assertIn("06-01-2023", message)
        self.assertIn("01-01-2023", message)
        self.assertEqual(level, 'error')

    def test_no_dates(self):
        paths = {
            '/v1/accounts': {
                'get': {
                    'parameters': [
                        {'name': 'account_name', 'in': 'query', 'example': 'test_account'}
                    ],
                    'requestBody': {
                        'content': {
                            'application/json': {
                                'schema': {
                                    'properties': {
                                        'account_name': {'type': 'string', 'example': 'test_account'}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        result, message, level = check_date_format(paths)
        self.assertTrue(result)
        self.assertEqual(message, "All dates are in YYYY-MM-DD format.")
        self.assertEqual(level, 'success')

if __name__ == '__main__':
    unittest.main()
