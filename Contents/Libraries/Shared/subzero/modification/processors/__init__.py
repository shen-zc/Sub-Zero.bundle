# coding=utf-8


class Processor(object):
    """
    Processor base class
    """
    name = None
    parent = None
    supported = None

    def __init__(self, name=None, parent=None, supported=None):
        self.name = name
        self.parent = parent
        self.supported = supported if supported else lambda parent: True

    @property
    def info(self):
        return self.name

    def process(self, content, debug=False, **kwargs):
        return content

    def __repr__(self):
        return "Processor <%s %s>" % (self.__class__.__name__, self.info)

    def __str__(self):
        return repr(self)

    def __unicode__(self):
        return unicode(repr(self))
