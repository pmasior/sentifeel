import functools

from . import cache_handler
from . import env_helper


def cache2(func, label, filestem, file_extension):
    def wrapper_cache2(*args, **kwargs):
        cache_handler.make_intermediate_directory(label)
        is_cached = cache_handler.check_existence_of_file(
            label, filestem, file_extension
        )
        if is_cached:
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


def cache_or_update(func, label, filestem, file_extension, env_variable_name):
    def wrapper_cache_or_update(*args, **kwargs):
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


# def cache(label, filestem, file_extension):
#     def decorator_cache(func):
#         @functools.wraps(func)
#         def wrapper_cache(*args, **kwargs):
#             cache_handler.make_intermediate_directory(label)
#             is_cached = cache_handler.check_existance_of_file(
#                 label, filestem, file_extension
#             )
#             if is_cached:
#                 return cache_handler.open_from_intermediate_directory(
#                     label, filestem, file_extension
#                 )
#             else:
#                 # before
#                 value = func(*args, **kwargs)
#                 cache_handler.save_to_intermediate_directory(
#                     value, label, filestem, file_extension
#                 )
#                 # after
#             return value

#         return wrapper_cache

#     return decorator_cache


if __name__ == "__main__":
    pass
