#You are managing deployment configs.
 
app_name = "PaymentsService"
version = "3.0.0"
replicas = 1
environment = "production"   # can be "dev", "staging", or "production"
region = "us-east"
is_debug_mode = True

#version auto-increase to 3.0.1 only if the env is prof
if environment == "production":
    one, two, three = version.split(".")
    three = str(int(three) + 1)
    two = str(int(two) + 2)
    version = f"{one}.{two}.{three}"
    
#Rules to implement:
#If environment is "production", replicas must be at least 3 and debug mode must be False.
#If environment is "staging", set replicas to 2 and allow debug mode to stay as-is.
#In "dev", replicas stay 1, but debug mode should always be True.
#If the region is "us-east" and environment is "production", print an extra message:
if environment == "production":
    replicas = 3
    is_debug_mode = False
    if region == "us-east":
        print("Applying stricter monitoring for us-east production.")
elif environment == "staging":
    replicas = 2
elif environment == "dev":
   is_debug_mode = True
   replicas = 1
#Final output format:
print(f"Deploying {app_name} version {version} with {replicas} replicas in {environment} environment (region: {region}). Debug: {is_debug_mode}")
#Try solving it 💻 and share your code — I’ll review and refine it with you. Want me to give you a hint first or let you try fully on your own?
 