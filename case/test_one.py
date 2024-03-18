import allure
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from base.report_add_img import add_img_report_with_airtest
# 暂时关闭截图
ST.SAVE_IMAGE = False
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90


class TestAllure:
    auto_setup(__file__, logdir=True,
               devices=["android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    @allure.description("第一个allure")
    def test1_demo(self):
        with allure.step("进入游戏页面"):
            sleep(3)
            touch([717, 2047])
            add_img_report_with_airtest("游戏页面")

        with allure.step("进入设置页面"):
            sleep(2)
            touch([121, 214])
            add_img_report_with_airtest("设置页面")

        with allure.step("断言"):
            assert 1 == 1
