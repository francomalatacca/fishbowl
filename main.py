import argparse
import webbrowser
from spec_loader import read_spec
from rule_applier import apply_rules
from result_display import display_results
from report_generator import generate_html_report
from api_standards_rules import rules
from config_loader import load_config, get_configuration

def main(verbose: bool, spec_file: str, config_file: str, report: bool):
    # Load the configuration file
    load_config(config_file)
    
    # Read the OpenAPI specification
    spec_data = read_spec(spec_file)

    if verbose:
        list_loaded_classes()

    # Apply the rules
    results = apply_rules(spec_data, rules)
    detailed_issues, summary_data = display_results(results)

    # Generate HTML report if the report option is specified
    if report:
        report_file = 'report.html'
        generate_html_report(detailed_issues, summary_data, report_file)
        webbrowser.open(report_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='OpenAPI Specification Validator')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode to list all loaded classes')
    parser.add_argument('--file', '-f', type=str, required=True, help='Path to the OpenAPI spec file')
    parser.add_argument('--config', '-c', type=str, default='config.json', help='Path to the configuration file')
    parser.add_argument('--report', '-r', action='store_true', help='Generate HTML report')
    args = parser.parse_args()
    main(args.verbose, args.file, args.config, args.report)
