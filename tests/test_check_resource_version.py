import unittest
from custom_rules.paths_rules import check_resource_version

class TestCheckResourceVersion(unittest.TestCase):
    def test_versioned_paths_correct(self):
        paths = {
            '/v1/banks': {'get': {}},
            '/v2/loans': {'get': {}},
            '/v1/accounts': {'post': {}}
        }
        result, message, level = check_resource_version(paths)
        self.assertTrue(result)
        self.assertEqual(message, "All paths start with a valid version segment.")
        self.assertEqual(level, 'success')

    def test_versioned_paths_incorrect(self):
        paths = {
            '/banks': {'get': {}},
            '/loans/v1': {'get': {}},
            '/v/accounts': {'post': {}},
            '/v1/accounts/v2': {'get': {}}
        }
        result, message, level = check_resource_version(paths)
        self.assertFalse(result)
        self.assertIn("'/banks'", message)
        self.assertIn("'/loans/v1'", message)
        self.assertIn("'/v/accounts'", message)
        self.assertIn("'/v1/accounts/v2'", message)
        self.assertEqual(level, 'error')

    def test_mixed_versioned_paths(self):
        paths = {
            '/v1/banks': {'get': {}},
            '/loans': {'get': {}},
            '/v2/accounts': {'post': {}},
            '/banking': {'get': {}}
        }
        result, message, level = check_resource_version(paths)
        self.assertFalse(result)
        self.assertIn("'/loans'", message)
        self.assertIn("'/banking'", message)
        self.assertEqual(level, 'error')

    def test_empty_paths(self):
        paths = {}
        result, message, level = check_resource_version(paths)
        self.assertTrue(result)
        self.assertEqual(message, "All paths start with a valid version segment.")
        self.assertEqual(level, 'success')

if __name__ == '__main__':
    unittest.main()
