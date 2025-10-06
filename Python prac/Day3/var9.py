app_name = "AnalyticsApp"
version = "2.5.0"
replicas = 1
environment = "dev"      # can be "dev", "staging", or "production"
is_debug_mode = True
 
#Steps to perform:
#If the environment is "production", replicas should be at least 3.
#If the environment is "staging", set replicas to 2.
#In "dev", replicas should stay as they are.
#Debug mode must be off (False) in production, otherwise it stays as-is.
if environment == "production":
    replicas = 3
    is_debug_mode = False
elif environment == "staging":
    replicas = 2
#Print a deployment message in this format:
print(f"Deploying {app_name} version {version} with {replicas} replicas in {environment} environment. Debug: {is_debug_mode}")