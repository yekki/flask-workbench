#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect
from flask.views import MethodView

from common.exts import db
from database import db_bp
from database.models import User, load_data


class HomeView(MethodView):
    def get(self):
        return render_template('database/index.html', users=User.query.all())


class UserView(MethodView):
    def get(self, id):
        User.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('db.home'))


def load():
    load_data()
    return redirect(url_for('db.home'))


db_bp.add_url_rule('/', view_func=HomeView.as_view('home'))
db_bp.add_url_rule('/load', view_func=load, endpoint='load')
db_bp.add_url_rule('/user/<int:id>', view_func=UserView.as_view('user'))
