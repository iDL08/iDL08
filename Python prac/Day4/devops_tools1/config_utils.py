#Scenario: You want to extend your devops_tools package to include another module for configuration parsing.
#Task:
#Inside your devops_tools/ folder, create a new file: config_utils.py
#In config_utils.py, write a function get_config_path(env) that:
def get_config_path(env):
    if env == "dev":
        config_path = "/etc/dev/config.yaml"
        print(config_path)
    elif env == "staging":
        config_path = "/etc/staging/config.yaml"
        print(config_path)
    elif env == "production":
        config_path = "/etc/prod/config.yaml"
        print(config_path)



#Takes an environment name (dev, staging, production)
#Returns the corresponding config path:
#dev → /etc/dev/config.yaml
#staging → /etc/staging/config.yaml
#production → /etc/prod/config.yaml
#In main.py, import and use both:

#extract_log_level() from log_utils
#get_config_path() from config_utils
#Print both the log level and the config path for "production".