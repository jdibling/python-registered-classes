__author__ = 'john'

from base.exceptions import *

class ClassRegistrar(object):
    __registry = dict()
    def __init__(self):
        super(ClassRegistrar, self).__init__()
    @classmethod
    def register_class(self, cls, name):
        if name in self.__registry:
            raise MultipleRegistrationError(name, ClassRegistrar.__registrycls[name])
        ClassRegistrar.__registry[name] = cls
    @classmethod
    def class_from_name(self, name):
        if name not in ClassRegistrar.__registry:
            raise NotRegisteredError(name)
        return ClassRegistrar.__registry[name]
    @classmethod
    def is_registered(self, name):
        return name in ClassRegistrar.__registry

class GizmoRegistrarMeta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)

        # make sure this class isn't already registered
        if cls.is_registered(name) == True:
            raise MultipleRegistrationError(name, Gizmo.registry[name])
        # python-registered-classes it
        cls.register_class(cls, name)
        print "Registered {0} as {1}".format(cls.__name__, cls)

        return cls

class Gizmo(ClassRegistrar):
    __metaclass__ = GizmoRegistrarMeta
    registry = dict()

    def __init__(self):
        super(Gizmo, self).__init__()
        print "Init Gizmo"


