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
