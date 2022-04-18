from functools import wraps

import sys
import traceback


def try_except_decorator(func):
    @wraps(func)
    def magic(self, *args, **kwards):
        try:
            return func(self, *args, **kwards)
        except Exception:
            # вывод желтым цветом
            sys.stdout.write(f'\r\033[33m{traceback.format_exc()}')
            sys.stdout.write(f"\r\033[38m")

    return magic


def check_method_args(*types):
    def check(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                if len(args) < len(types):
                    print(f'Not enough arguments for {func}')
                    return
                elif len(args) > len(types):
                    print(f'Too many arguments for {func}')
                    return
                for idx, arg in enumerate(args):
                    type_ = types[idx]
                    if type(arg) == type_ or type_ == arg.__class__ or type_ == arg.__class__.__base__:  # or type_ == arg.__base__:
                        pass
                        # func(self, *args, **kwargs)
                        # print(f'"{arg}" must be {type_}, not {type(arg)}')
                        # return
                    else:
                        # func(self, *args, **kwargs)
                        # print('Input error:')
                        print(f'"{arg}" must be {type_}, not {type(arg)}')
                        return
                    try:
                        return func(self, *args, **kwargs)
                    except Exception:
                        sys.stdout.write(f'\r\033[33m{traceback.format_exc()}')
                        sys.stdout.write(f"\r\033[38m")
            except TypeError:
                print('Wrong argument types')
            except IndexError:
                print('Not enough arguments')
            except Exception as ex:
                print(f'Unknown error: {ex}')

        return wrapper

    return check
