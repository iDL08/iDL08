import re
log_data = "Connection from 192.168.1.10 at 10:00, then from 10.0.0.5 at 10:05"
pattern = r"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})"

results = re.findall(pattern, log_data)

if pattern:
    print(results)
else:
    print("No results found")