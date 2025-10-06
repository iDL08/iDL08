import re

log_data = "2025-09-23 10:00:01 ERROR Disk full on /dev/sda1"

pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+)"

results = re.search(pattern, log_data)

print ("Time stamp: ", results.group(1))
print ("error log: ", results.group(2))