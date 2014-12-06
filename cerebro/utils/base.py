#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 06, 2014 '
__author__= 'samuel'

class ConstEnum(object):
    class __metaclass__(type):
        def __setattribute__(cls, attr):
            raise AttributeError('<%s class> cannot set attribute' % cls.__name__)
        def __setattr__(cls, name, value):
            raise AttributeError('<%s class> cannot set attr' % cls.__name__)

