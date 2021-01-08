# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : huangdq
# @File    : Test_Basic.py

import allure

from common.tools import LoadFiles
from common import Consts
from common import Assert


class TestBasic:

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Basic')
    def test_basic_01(self, action):
        """
            用例描述：未登陆状态下查看基础设置
        """

        asert = Assert.Assertions()
        #发送请求
        respon = LoadFiles.assembed_request()
        code = respon.__getattribute__('status_code')

        #测试断言
        assert asert.assert_code(code, 200)
        Consts.RESULT_LIST.append('True')

