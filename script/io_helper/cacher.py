from pathlib import Path
from typing import Any, Callable, Dict

from . import cache_handler
from . import env_helper


def cache2(
    func: Callable[..., Any],
    label: str,
    filestem: str,
    file_extension: str,
    should_read_from_cache: bool = True,
) -> Callable[..., Any]:
    def wrapper_cache2(*args: Any, **kwargs: Any) -> Any:
        cache_handler.make_intermediate_directory(label)
        is_cached = cache_handler.check_existence_of_file(
            label, filestem, file_extension
        )
        if is_cached and should_read_from_cache:
            return cache_handler.open_from_intermediate_directory(
                label, filestem, file_extension
            )
        else:
            # before
            value = func(*args, **kwargs)
            # after
            cache_handler.save_to_intermediate_directory(
                value, label, filestem, file_extension
            )
        return value

    return wrapper_cache2


def cache3(
    func: Callable[..., Path], label: str, filestem: str, file_extension: str
) -> Callable[..., Path]:
    def wrapper_cache3(*args: Any, **kwargs: Any) -> Path:
        cache_handler.make_intermediate_directory(label)
        is_cached = cache_handler.check_existence_of_file(
            label, filestem, file_extension
        )
        if is_cached:
            return cache_handler.get_intermediate_file_path(
                label, filestem, file_extension
            )
        else:
            # before
            return func(*args, **kwargs)
            # after

    return wrapper_cache3


def cache_or_update(
    func: Callable[..., str],
    label: str,
    filestem: str,
    file_extension: str,
    env_variable_name: str,
) -> Callable[..., str]:
    def wrapper_cache_or_update(*args: Any, **kwargs: Any) -> str:
        cache_handler.make_intermediate_directory(label)
        is_cached = cache_handler.check_existence_of_file(
            label, filestem, file_extension
        )
        is_allowing_connect = env_helper.get_boolean_env_variable(env_variable_name)
        if is_cached:
            return cache_handler.open_from_intermediate_directory(
                label, filestem, file_extension
            )
        else:
            if is_allowing_connect:
                # before
                value = func(*args, **kwargs)
                # after
                cache_handler.save_to_intermediate_directory(
                    value, label, filestem, file_extension
                )
            else:
                raise FileNotFoundError(
                    f"Missing data for {label}/{filestem}.{file_extension}"
                )
        return value

    return wrapper_cache_or_update


if __name__ == "__main__":
    pass
