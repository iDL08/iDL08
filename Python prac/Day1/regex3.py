import re

log_data = "Service apache started successfully on port 8081"
pattern = log_data.split()
output = f"{pattern[1]}:{pattern[6]}"
print (output)