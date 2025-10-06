def current_env():
    env = "dev"
    return env

def current_env_update_one():
    env = "staging"
    return env

def current_env_update_two():
    env = "production"
    return env

print("Current environment: ", current_env())
print("Current environment: ", current_env_update_one())
print("Current environment: ", current_env_update_two())

env = "dev"
print("Current environment:", env)

env = "staging"
print("Current environment:", env)

env = "production"
print("Current environment:", env)


def set_env(env_name):
    print(f"Current environment: {env_name}")

set_env("dev")
set_env("staging")
set_env("production")
