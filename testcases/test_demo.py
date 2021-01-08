import allure

from common import LogConf

class TestDemo01:

    log = LogConf.LogConf()

    @allure.story("test01")
    def test_demo_01(self):
        print('this is the first testcase.')
        self.log.info("first test run over.")
        assert 1 == 1

    @allure.story("test02")
    def test_demo_02(self):
        print('this is the second testcase.')
        self.log.info("second test run over.")
        assert 1 >= 2