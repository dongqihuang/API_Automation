# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:56
# @Author  : huangdq
# @File    : tools.py

"""
读取yaml测试数据

"""
import requests
import yaml
import os
import os.path

from common import LogConf
from config import Config

log = LogConf.LogConf()
conf = Config.Config()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class LoadFiles:

    @staticmethod
    def load_yaml_file():
        log.info('开始解析yaml文件，路径：' + path_dir + '/datafiles/basic.yml')
        file_path = path_dir + '/datafiles/basic.yml'
        with open(file_path, 'r') as loadfile:
            lf = yaml.load(loadfile)
        log.info('解析yaml文件完成')
        return lf

    @staticmethod
    def assembed_request():
        datas = LoadFiles.load_yaml_file()
        host = conf.host_debug
        api_url = datas['url']
        req_url = host + api_url
        req_method = datas.get('method')
        headers = datas.get('headers')
        params = datas.get('params')
        if req_method == 'GET':
            resp = requests.get(url=req_url, headers=headers, params=params)
        elif req_method == 'POST':
            resp = requests.post()
        elif req_method == 'PUT':
            resp = requests.put()

        return resp

    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = LoadFiles.parse()
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list

        return _page_list

    @staticmethod
    def parse():
        path_ya = path_dir + '/datafiles'
        pages = {}
        for root, dirs, files in os.walk(path_ya):
            for name in files:
                watch_file_path = os.path.join(root, name)
                with open(watch_file_path, 'r') as f:
                    page = yaml.safe_load(f)
                    pages.update(page)
            return pages