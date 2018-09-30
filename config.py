#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/flask_study'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)
