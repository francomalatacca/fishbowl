
# OpenAPI Specification Validator

This project is an OpenAPI Specification Validator that checks for adherence to specified API standards. It supports configurable rules and generates a detailed HTML report with validation results, statistics, and documentation links.

## Features

- Validate OpenAPI specifications against custom rules.
- Configurable error, warning, and info levels for rules.
- Detailed HTML report with a table of contents, statistics, and links to documentation.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/openapi-validator.git
   cd openapi-validator
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the validator with the following command:
```sh
python3 main.py -f path/to/openapi_spec.json -c path/to/config.json -r
```

- `-f`, `--file`: Path to the OpenAPI spec file (required).
- `-c`, `--config`: Path to the configuration file (optional, defaults to `config.json`).
- `-r`, `--report`: Generate HTML report (optional).

## Configuration

The configuration file (`config.json`) allows specifying rules and their levels (error, warning, info). Example:
```json
{
    "required_headers": {
        "request_headers": {
            "Authorization": "error"
        },
        "response_headers": {
            "X-API-Request-Id": "warning",
            "Deprecate": "info"
        }
    }
}
```

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.
