def extract_log_level(log_line):
    import re
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+)"
    results = re.findall(pattern, log_line)
    for match in results:
        print(f"{match[1]}")