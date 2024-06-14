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
