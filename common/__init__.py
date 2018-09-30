#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from database import db_bp
from .exts import bootstrap, db


def create_app(config, name):
    app = Flask(name)
    app.config.from_object(config)
    return app


def register_bps(app):
    app.register_blueprint(db_bp, url_prefix='/db')


def register_exts(app):
    bootstrap.init_app(app)
    db.init_app(app)
