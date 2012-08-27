class GenericView (object):
    
    def __call__ (self, request, *k, **kw):
        callfn = getattr (self, request.method.upper())
        resp = callfn (request, *k, **kw)
        return resp


