#!/user/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:   config
   Description:
   Author:      allen
   Date:        4/14/19 4:45 PM

---------------------
"""
__author__ = "zx"

import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_YAML = os.path.join(BASE_DIR, 'log.yaml')
RESOURCE_PATH = os.path.join(BASE_DIR, 'resources')
COLOR_MAP_PAth = os.path.join(RESOURCE_PATH, "454色按78色关键字归类(1).xlsx")
COLOR_XLSX = os.path.join(RESOURCE_PATH, "color.xlsx")
model_path = f'{RESOURCE_PATH}{os.sep}pb_model{os.sep}model.pb'
style_model_path = f'{RESOURCE_PATH}{os.sep}pb_model{os.sep}style_model'
style_class_name_path = f'{RESOURCE_PATH}{os.sep}pb_model{os.sep}style_model{os.sep}class_names.txt'
# 百度在线翻译账户密码
baidu_key = "20190808000324931"
baidu_passwd = "K52NIO04wx20O8gV1YF7"


class Config(object):
    DEBUG = False
    TESTING = False

    JSONSCHEMA_DIR = os.path.join(BASE_DIR, "schemas")


def read_file(path):
    with open(path, encoding="utf8") as file:
        data = ''.join(file.readlines())
    return data


def save_excel(model, path):
    df = pd.DataFrame(model)
    df.to_excel(path, index=False)


def read_map_excel():
    num_to_id_color_name_dict = {}
    df = pd.read_excel(COLOR_MAP_PAth)
    df = df.replace(to_replace=np.nan, value="")
    for _, row in df.iterrows():
        nums = str(row["序号"]).replace(",", "，")
        for num in nums.split("，"):
            num_to_id_color_name_dict[num] = f"{row['编号']}_{row['中文名称']}"

    return num_to_id_color_name_dict


def read_color_excel():
    num_to_rgb_dict = {}
    df = pd.read_excel(COLOR_XLSX)
    df = df.replace(to_replace=np.nan, value="")
    for i, row in df.iterrows():
        num_to_rgb_dict[i] = row["颜色RGB"]
    return num_to_rgb_dict
