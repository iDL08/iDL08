import re

log_data = """
2025-06-10 10:20:30 INFO Starting service
2025-06-10 10:20:31 ERROR Failed to connect to database
2025-06-10 10:20:32 INFO Service is running
2025-06-10 10:20:33 WARN High memory usage
2025-06-10 10:20:34 ERROR Disk full on /dev/sda1
2025-06-10 10:20:35 DEBUG Health check passed
"""
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (WARN|ERROR) (.*)"

results = re.findall(pattern, log_data)

for match in results:
    print(f"[{match[1]}] at {match[0]}: {match[2]}")