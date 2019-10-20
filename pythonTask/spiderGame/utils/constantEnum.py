#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
constantEnum.py by lcs
"""
import enum
class ConstantEnum(enum.Enum):
    # fetch 的一些常量
    Fetch_Html = "fetch_html"
    Fetch_Html_Succ = "fetch_html_succ"
    Fetch_Html_not = "fetch_html_not"

    # parser 常量
    Parse_Html = "parse_html"
    Parse_Html_Succ = "parse_html_succ"
    Parse_Html_not = "parse_html_not"

    # save 常量
    Save_Item = "save_item"
    Save_Item_Succ = "save_item_succ"
    Save_Item_not = "save_item_not"

