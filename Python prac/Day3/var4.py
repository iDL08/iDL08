env = "dev"
def set_env():
    global env
    env = "production"
    print(env)

set_env()

print("outside the function: ",env)