import os


def get_env_variable_or_throw(name):
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable {name} is not set")
    return value


def get_boolean_env_variable(name):
    value = os.getenv(name)
    return value is not None and value.lower() in ["true", "t", "yes", "y", "1"]


def get_int_env_variable(name, is_required=True):
    value = os.getenv(name)
    if not value and is_required:
        raise ValueError(f"Environment variable {name} is not set")
    return int(value) if value is not None else None


if __name__ == "__main__":
    pass
