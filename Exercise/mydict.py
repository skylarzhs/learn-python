#!/usr/bin/env python3
# -*- encoding : utf-8 -*-


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __setattr__(self,key,val):
        self[key] = val

    def __getattribute__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute %s" % key)