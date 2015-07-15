__author__ = 'john'

class RegisterException(Exception):
    pass

class MultipleRegistrationError(RegisterException):
    def __init__(self, name, prevclass):
        super(MultipleRegistrationError, self).__init__()
        self.cls = prevclass
        self.name = name

    def __str__(self):
        return "Gizmo '{0}' previously registered as class {1}".format(self.name, self.cls)

class NotRegisteredError(RegisterException):
    def __init__(self, name):
        super(NotRegisteredError, self).__init__(self)
        self.name = name
    def __str__(self):
        return "Gizmo named '{0}' has not been registered".format(self.name)


