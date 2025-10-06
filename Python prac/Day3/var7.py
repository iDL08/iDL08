#Task:
#You are deploying an application.
#Start with the same variables:
#app_name, version, replicas, is_debug_mode

app_name = "MyApp"
version = "1.0.2"
replicas = 3
is_debug_mode = True

#Then:
#Increase replicas by 2 (simulate scaling up).
replicas += 2
print(replicas)
#Toggle the debug mode (if it’s True, make it False; if False, make it True).
is_debug_mode = not is_debug_mode
#Print the updated deployment message.
print(f"Deploying {app_name} version {version} with {replicas} replicas. Debug mode: {is_debug_mode}")