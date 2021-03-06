#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 06, 2014 '
__author__= 'samuel'

from flask import Flask
app = Flask(__name__)

app.debug= True


# GET /
# response:
# Hello World
@app.route('/')
def root():
    return "Hello World!"

# GET /abc
# response:
# Hello World! This is: /abc
@app.route('/<route_name>')
def route_name(route_name):
    return "Hello World! This is: /%s" % route_name

if __name__ == "__main__":
    app.run()

