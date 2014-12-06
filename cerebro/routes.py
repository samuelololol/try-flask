#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 06, 2014 '
__author__= 'samuel'

from cerebro import cerebro_app
from cerebro.apis.root import Root

RootAPI = cerebro_app.route(Root.route_path, methods=Root.route_methods)(Root.api)
