#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.exts import db

__all__ = ['User']


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False, cascade='delete')


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))


def load_data():
    db.session.query(User).delete()
    for i in range(5):
        user = User(username=f'user{i}', password='password')
        user.profile = Profile(address='Shanghai', phone='13816807866', email=f'user{i}@me.com')
        db.session.add(user)
    db.session.commit()
