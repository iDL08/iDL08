service_name = "nginx"
env = "production"
config_path = "/etc/nginx/nginx.conf"


print(f"deploy --service {service_name} --env {env} --config {config_path}")