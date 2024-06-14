
# Contributing to OpenAPI Specification Validator

Thank you for considering contributing to the OpenAPI Specification Validator project! We welcome contributions from the community to help improve the project.

## Workflow

1. **Fork the repository**: Click the "Fork" button at the top right of the repository page to create a copy of the repository under your GitHub account.

2. **Clone your fork**: Clone your fork to your local machine using the following command:
   ```sh
   git clone https://github.com/yourusername/openapi-validator.git
   cd openapi-validator
   ```

3. **Create a branch**: Create a new branch for your work. Use a descriptive name for your branch:
   ```sh
   git checkout -b feature-name
   ```

4. **Make your changes**: Implement your changes in the newly created branch.

5. **Add tests**: Ensure that you add unit tests for any new features or changes. See the section below for details on writing unit tests for rules.

6. **Commit your changes**: Commit your changes with a meaningful commit message:
   ```sh
   git add .
   git commit -m "Add feature name"
   ```

7. **Push to your fork**: Push your changes to your forked repository:
   ```sh
   git push origin feature-name
   ```

8. **Open a Pull Request**: Go to the original repository and open a Pull Request. Provide a clear description of your changes and the motivation behind them.

## Writing New Rules

To write a new rule, follow these steps:

1. **Create the rule function**: Implement the rule function in a new file under the `api_standards_rules` directory. The function should take the relevant part of the OpenAPI spec as input and return a tuple `(bool, str, str)` where:
   - The first value is a boolean indicating if the rule passed or failed.
   - The second value is a message string.
   - The third value is the level of the rule (error, warning, info).

2. **Update the rule definitions**: Add an entry for your new rule in the `api_standards_rules/__init__.py` file. Include a description and a link to the relevant documentation.

   Example:
   ```python
   from .check_new_rule import check_new_rule

   rules = [
       {
           'target': 'paths',
           'func': check_new_rule,
           'name': 'new_rule',
           'description': 'Description of the new rule.',
           'doc_url': 'https://example.com/docs/new_rule'
       },
   ]
   ```

3. **Add configuration options**: If your rule requires configuration options, update the `config.json` file and include an example in the README.

## Writing Unit Tests

To write unit tests for your new rule:

1. **Create a test file**: Create a new test file in the `tests` directory, named `test_<rule_name>.py`.

2. **Write test cases**: Use the `unittest` framework to write test cases for your rule. Include tests for both passing and failing cases, as well as any edge cases.

   Example:
   ```python
   import unittest
   from api_standards_rules.check_new_rule import check_new_rule

   class TestCheckNewRule(unittest.TestCase):
       def test_rule_pass(self):
           spec = { ... }  # Example spec that should pass
           result, message, level = check_new_rule(spec)
           self.assertTrue(result)
           self.assertEqual(level, 'success')

       def test_rule_fail(self):
           spec = { ... }  # Example spec that should fail
           result, message, level = check_new_rule(spec)
           self.assertFalse(result)
           self.assertEqual(level, 'error')

   if __name__ == '__main__':
       unittest.main()
   ```

3. **Run tests**: Run the tests to ensure they pass:
   ```sh
   python3 -m unittest discover -s tests
   ```

## Contact

If you have any questions or need further assistance, please feel free to open an issue or contact the maintainers.

Thank you for your contributions!
