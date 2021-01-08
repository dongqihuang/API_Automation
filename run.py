# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:42
# @Author  : WangJuan
# @File    : run.py

"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""

import pytest
import os

from common import LogConf, Shell
from config import Config

if __name__ == '__main__':
    conf = Config.Config()
    log = LogConf.LogConf()
    log.info('初始化配置文件, path=' + conf.conf_path)

    shell = Shell.Shell()
    #执行结果保存位置
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试执行方式，--alluredir 指定结果保存目录
    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)

    cmd = 'allure generate %s -o %s -c' % (xml_report_path, html_report_path)


    os.system(cmd)
    log.info('执行用例完成，请查看结果。')

    #try:
     #   shell.invoke(cmd)
    #except Exception:
     #   log.error('执行用例失败，请检查环境配置')
     #   raise



