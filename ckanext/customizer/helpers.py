import os

# checks for required env vars or throws error
def get_env_var(env_var, default_value=None):
    if env_var not in os.environ and default_value is None:
        raise Exception("Missing required environment variable: {}".format(env_var))
    return os.getenv(env_var, default_value)
