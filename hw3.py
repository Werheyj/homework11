import inspect


def introspection_info(obj):
    obj_type = type(obj)
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = inspect.getmodule(obj)
    if module is None:
        module = '__main__'

    info = {'type': obj_type, 'attributes': attributes,
            'methods': methods, 'module': module}

    return info


number_info = introspection_info(42)
print(number_info)
