#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import io
import os
import sys
from importlib import reload

from src.constants import PASSWORD_FILE_PATH, NOTES_FILE_PATH, DATA_PATH

reload(sys)


class FileUtil(object):

    @staticmethod
    def getPassword():
        if not os.path.exists(DATA_PATH):
            os.mkdir(DATA_PATH)
        if not os.path.exists(PASSWORD_FILE_PATH):
            with open(PASSWORD_FILE_PATH, 'w') as f:  # 初始密码是'12345'
                f.write('12345')
                return '12345'

        with open(PASSWORD_FILE_PATH, 'r') as fileReader:
            ret = fileReader.read()
            fileReader.close()
            return ret

    @staticmethod
    def getNoteRecords(filePath=NOTES_FILE_PATH):
        data = []
        if not os.path.exists(DATA_PATH):  # 初始情况下，由代码创建数据目录
            os.mkdir(DATA_PATH)
            print('Created data dir!')
        try:
            json_data = io.open(filePath, encoding='utf-8').read()
            # json调用loads()方法将字符串数据转换成列表
            data = json.loads(json_data)
            return data
        except:
            print('No item in file!')
            return data

    @staticmethod
    def clearNote(filePath=NOTES_FILE_PATH):
        with open(filePath, 'w') as f:
            f.write('')

    @staticmethod
    def setNoteRecords(data, filePath=NOTES_FILE_PATH):
        dic_json = json.dumps(data, ensure_ascii=False, indent=4)
        fw = io.open(filePath, 'w', encoding='utf-8')
        fw.write(dic_json)
        fw.close()
