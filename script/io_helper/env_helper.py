import os


def get_env_variable_or_throw(name):
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable {name} is not set")
    return value


def get_boolean_env_variable(name):
    value = os.getenv(name)
    return value is not None and value.lower() in ["true", "t", "yes", "y", "1"]


if __name__ == "__main__":
    pass
