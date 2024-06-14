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
