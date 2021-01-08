# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午5:23
# @Author  : huangdq
# @File    : LogConf.py

"""
封装log方法

"""

import logging
import os
import time

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

#初始化logger收集器
logger = logging.getLogger()
#设置日志级别，默认为DEFAULT
logger.setLevel('DEBUG')

def get_current_time():
    return time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))

def set_handler(lev):
    if lev == 'error':
        logger.addHandler(LogConf.fh_err)
    logger.addHandler(LogConf.fh)


def remove_handler(lev):
    if lev == 'error':
        logger.removeHandler(LogConf.fh_err)
    logger.removeHandler(LogConf.fh)


def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


class LogConf:
    """
        日志配置
    """

    def __init__(self):
        pass

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug("[DEBUG " + get_current_time() + "]" + log_meg)
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info("[INFO " + get_current_time() + "]" + log_meg)
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning("[WARNING " + get_current_time() + "]" + log_meg)
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error("[ERROR " + get_current_time() + "]" + log_meg)
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.error("[CRITICAL " + get_current_time() + "]" + log_meg)
        remove_handler('critical')


    log_file = path + '/logs/log.log'
    err_file = path + '/logs/err.log'
    create_file(log_file)
    create_file(err_file)

    #创建一个handler，写入所有的日志信息
    fh = logging.FileHandler(log_file, encoding='utf-8')

    #创建一个handler，写入error日志信息
    fh_err = logging.FileHandler(err_file, encoding='utf-8')

    #加入handler到日志中
    logger.addHandler(fh)
    logger.addHandler(fh_err)
