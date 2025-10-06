# Variables
app_name = "MyApp"
version = "1.0.2"
replicas = 2
environment = "staging"
is_debug_mode = False
 
# Task:
# 1. Bump the version to "1.0.3".
version = "1.0.3"
# 2. Scale replicas to double the current number.
replicas *= 2
# 3. Change environment to "production".
environment = "production"
# 4. Ensure debug mode is always False in production.
if environment == "production":
    is_debug_mode = False
else:
    is_debug_mode = True
# 5. Print a final deployment message with all the updated values.
print(f"Deploying {app_name} version {version} with {replicas} replicas. Debug mode: {is_debug_mode}")