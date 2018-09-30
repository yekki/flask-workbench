#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from common.exts import db
from main import app

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
