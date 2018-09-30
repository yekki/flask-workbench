#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect
from flask.views import MethodView
from flask_table import LinkCol

from common.exts import db
from database import db_bp
from database.models import User
from database.widgets import UserTable


class HomeView(MethodView):
    def get(self):
        users = User.query.all()
        table = UserTable(items=users)
        table.add_column('action_panel', LinkCol('删除', endpoint='db.user', url_kwargs=dict(id='id')))
        return render_template('database/index.html', table=UserTable(items=users))


class UserView(MethodView):
    def get(self, id):
        User.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('db.home'))


def load():
    for i in range(5):
        db.session.add(User(username=f'user{i}', password='password', email=f'user{i}@me.com'))

    db.session.commit()
    return redirect(url_for('db.home'))


db_bp.add_url_rule('/', view_func=HomeView.as_view('home'))
db_bp.add_url_rule('/load', view_func=load, endpoint='load')
db_bp.add_url_rule('/user/<int:id>', view_func=UserView.as_view('user'))

