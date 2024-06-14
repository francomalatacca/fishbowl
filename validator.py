from collections import defaultdict
import json
from colorama import Fore, Style
from core_utils import CoreUtils  # Assuming CoreUtils is in a module named core_utils

def display_results(results):
    table_data = [["Rule", "Status", "OpenAPI Spec Section", "Description"]]
    success_count = 0
    warning_count = 0
    error_count = 0
    info_count = 0

    for result in results:
        rule_name = result['rule']
        valid = result['passed']
        section = result['path']
        message = result['message']
        level = result['level']
        
        if valid:
            status = f"{Fore.GREEN}✔{Style.RESET_ALL}"
            success_count += 1
            table_data.append([rule_name, status, section, message])
        else:
            if level == 'warning':
                status = f"{Fore.YELLOW}⚠{Style.RESET_ALL}"
                warning_count += 1
            elif level == 'info':
                status = f"{Fore.BLUE}ℹ{Style.RESET_ALL}"
                info_count += 1
            else:
                status = f"{Fore.RED}✘{Style.RESET_ALL}"
                error_count += 1
            
            # Split the message if it contains multiple issues separated by a pipe
            messages = message.split(' | ')
            for msg in messages:
                table_data.append([rule_name, status, section, msg.strip()])
    
    total_count = len(results)
    success_percentage = (success_count / total_count) * 100 if total_count > 0 else 0

    summary_data = [
        ["Summary", ""],
        ["Total Checks", total_count],
        ["Successes", success_count],
        ["Warnings", warning_count],
        ["Errors", error_count],
        ["Infos", info_count],
        ["Success Percentage", f"{success_percentage:.2f}%"]
    ]

    CoreUtils.print_table(table_data)
    print("\n")
    CoreUtils.print_table(summary_data)

    return results, summary_data  # Return the detailed results and summary for HTML report

def generate_html_report(detailed_issues, summary_data, report_file='report.html'):
    with open(report_file, 'w') as f:
        f.write("<html><body><h1>Validation Report</h1>\n")
        
        # Add Table of Contents
        f.write("<h2>Table of Contents</h2>\n")
        f.write("<ul>\n")
        for issue in detailed_issues:
            f.write(f"<li><a href='#{issue['rule']}'>{issue['rule']}</a></li>\n")
        f.write("</ul>\n")

        # Add Statistics
        f.write("<h2>Statistics</h2>\n")
        f.write("<table border='1'>\n")
        for item in summary_data:
            f.write(f"<tr><td>{item[0]}</td><td>{item[1]}</td></tr>\n")
        f.write("</table>\n")

        # Add Detailed Issues
        for issue in detailed_issues:
            f.write(f"<h2 id='{issue['rule']}'>{issue['rule']}</h2>\n")
            f.write(f"<p>Path: {issue['path']}</p>\n")
            f.write(f"<p>Description: {issue['message']}</p>\n")
            f.write(f"<p>Details: {issue['description']}</p>\n")
            f.write(f"<p><a href='{issue['doc_url']}'>Documentation</a></p>\n")
        f.write("</body></html>")
    print(f"Report generated: {report_file}")


def read_spec(spec_path):
    try:
        with open(spec_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading spec file {spec_path}: {e}")
        return None

def apply_rules(spec_data, rules):
    results = []
    for rule in rules:
        func = rule['func']
        target = rule['target']
        doc_url = rule.get('doc_url', '#')
        if target in spec_data:
            result, message, level = func(spec_data[target])
            results.append({
                'passed': result,
                'message': message,
                'level': level,
                'path': target,
                'rule': rule['name'],
                'description': rule['description'],
                'doc_url': doc_url
            })
    return results



def list_loaded_classes():
    # Placeholder for actual implementation
    print("List of loaded classes:")
    # Print or return the list of loaded classes if needed
