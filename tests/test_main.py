import unittest
import os
from unittest.mock import patch
from main import main

class TestMainFunction(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args')
    def test_main_with_spec_file(self, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            verbose=False, 
            file='tests/resources/openapi_spec.json', 
            config='config.json'
        )
        
        try:
            main(mock_parse_args.return_value.verbose, mock_parse_args.return_value.file, mock_parse_args.return_value.config)
        except SystemExit:
            pass

    @patch('argparse.ArgumentParser.parse_args')
    def test_main_with_verbose(self, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            verbose=True, 
            file='tests/resources/openapi_spec.json', 
            config='config.json'
        )
        
        try:
            main(mock_parse_args.return_value.verbose, mock_parse_args.return_value.file, mock_parse_args.return_value.config)
        except SystemExit:
            pass

if __name__ == '__main__':
    unittest.main()
