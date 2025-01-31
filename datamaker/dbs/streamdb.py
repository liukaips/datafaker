#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

from datamaker.compat import safe_encode
from datamaker.constant import JSON_FORMAT, TEXT_FORMAT
from datamaker.dbs.basedb import BaseDB
from datamaker.utils import save2file, json_item


class StreamDB(BaseDB):

    def construct_self_rows(self):
        return []

    def save_data(self, lines):
        filepath = os.path.join(self.args.connect, self.args.table)

        items = []
        for line in lines:
            item = self.format_data(line)
            items.append(item+os.linesep)

        save2file(items, filepath)

    def format_data(self, columns):
        data = columns
        if self.args.metaj:
            data = self.metaj_content % tuple(columns)
        elif self.args.format == JSON_FORMAT:
            data = json_item(self.column_names, columns)
        elif self.args.format == TEXT_FORMAT:
            data = self.args.outspliter.join([str(safe_encode(word)) for word in columns])
        print(data)
        return data
