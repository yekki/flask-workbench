#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_table import Table, Col


class UserTable(Table):
    classes = ['table', 'table-bordered', 'table-hover']
    no_items = '没有数据'
    thead_classes = ['thead-dark']
    id = Col('ID')
    username = Col('用户名')
