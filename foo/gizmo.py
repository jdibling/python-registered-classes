__author__ = 'john'

from base import gizmo

class FooGizmo(gizmo.Gizmo):
    def __init__(self, **kwargs):
        super(FooGizmo, self).__init__(**kwargs)
        print "Init FooGizmo"
