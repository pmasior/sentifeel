import os


def get_env_variable_or_throw(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable {name} is not set")
    return value


def get_boolean_env_variable(name: str) -> bool:
    value = os.getenv(name)
    return value is not None and value.lower() in ["true", "t", "yes", "y", "1"]


def get_int_env_variable(name: str, is_required: bool = True) -> int | None:
    value = os.getenv(name)
    if not value and is_required:
        raise ValueError(f"Environment variable {name} is not set")
    return int(value) if value is not None else None


if __name__ == "__main__":
    pass
