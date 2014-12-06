#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 06, 2014 '
__author__= 'samuel'

from flask import jsonify
from cerebro import cerebro_app
from cerebro.utils.base import ConstEnum

class Root(ConstEnum):
    route_path = '/'
    route_methods = ['GET']
    route_permission = ''
    @classmethod
    def api(cls):
        #return '<h1>Welcome<br/> Flask root: / </h1>'
        rtn_dict = {'greeting': 'Welcome', 'path': '/'}
        return jsonify(**rtn_dict)

