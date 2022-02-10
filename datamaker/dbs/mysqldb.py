#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datamaker.dbs.basedb import BaseDB
# from drivers import load_sqlalchemy
from datamaker.dbs.rdbdb import RdbDB
from datamaker.drivers import load_sqlalchemy
from datamaker.utils import save2db


class MysqlDB(RdbDB):

    def construct_self_rows(self):
        session = load_sqlalchemy(self.args.connect)
        sql = 'show full columns from %s' % self.args.table
        rows = session.execute(sql)
        return rows

