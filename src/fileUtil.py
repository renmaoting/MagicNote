#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import io
import sys

from src.constants import PASSWORD_FILE_PATH, NOTES_FILE_PATH

reload(sys)
sys.setdefaultencoding("utf-8")

class FileUtil(object):

    @staticmethod
    def getPassword():
        with open(PASSWORD_FILE_PATH, 'r') as fileReader:
            ret = fileReader.read()
            fileReader.close()
            return ret

    @staticmethod
    def getNoteRecords():
        json_data = io.open(NOTES_FILE_PATH, encoding='utf-8').read()
        print(type(json_data))
        # json调用loads()方法将字符串数据转换成列表
        data = json.loads(json_data)
        return data
