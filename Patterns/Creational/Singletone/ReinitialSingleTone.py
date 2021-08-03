class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        params = (args, tuple(sorted(kwargs.items())))
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = {'instance': instance, 'params': (args, kwargs)}
        return cls._instances[cls]