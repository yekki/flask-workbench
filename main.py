#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template
from common import create_app, register_bps, register_exts
import config

app = create_app(config, __name__)
register_bps(app)
register_exts(app)

app.add_url_rule('/', endpoint='index', view_func=lambda: render_template('index.html'))

if __name__ == '__main__':
    app.run()
