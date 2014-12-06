#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 06, 2014 '
__author__= 'samuel'

from flask import Flask
cerebro_app = Flask(__name__)
cerebro_app.debug=True
import routes

def main():
    cerebro_app.run()

if __name__ == '__main__':
    main()

