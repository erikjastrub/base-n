def error(message):

    def decorator(cls: Exception):

        cls.__init__ = lambda self: Exception.__init__(self, message) 

        return cls

    return decorator

@error("Duplicate character found")
class DuplicateError(Exception): pass

@error("2 or more bases must be passed in")
class InvalidBasesError(Exception): pass
