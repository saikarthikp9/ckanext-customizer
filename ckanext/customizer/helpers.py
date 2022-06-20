import os

# checks for required env vars or throws error
def get_env_var(env_var):
    if env_var in os.environ:
        return os.getenv(env_var)
    raise Exception("Missing required environment variable: {}".format(env_var))
