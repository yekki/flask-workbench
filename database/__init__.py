#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_bootstrap import Blueprint

db_bp = Blueprint('db', __name__)

from . import views
from . import models
