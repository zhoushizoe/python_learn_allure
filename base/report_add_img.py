from airtest.cli.parser import cli_setup
from airtest.core.api import *
import allure
import os
import tempfile

# 暂时关闭截图
ST.SAVE_IMAGE = False
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90


def add_img_report_with_airtest(step_name,  max_size=None):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        # 使用Airtest的snapshot函数生成截图并保存到临时文件
        snapshot(filename=tmpfile.name,  max_size=max_size)
        # 读取临时文件内容以获取截图的字节流
        tmpfile.seek(0)
        image_data = tmpfile.read()
    # 使用Allure的attach方法将截图的字节流附加到报告中
    allure.attach(image_data, step_name + ".png", allure.attachment_type.PNG)
    # 删除临时文件
    os.unlink(tmpfile.name)
