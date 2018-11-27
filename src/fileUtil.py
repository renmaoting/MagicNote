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
    def getNoteRecords(filePath = NOTES_FILE_PATH):
        json_data = io.open(filePath, encoding='utf-8').read()
        print(type(json_data))
        # json调用loads()方法将字符串数据转换成列表
        data = json.loads(json_data)
        return data

    @staticmethod
    def setNoteRecords(data, filePath = NOTES_FILE_PATH):
        dic_json = json.dumps(data, ensure_ascii=False, indent=4)
        fw = io.open(filePath, 'w', encoding='utf-8')
        fw.write(dic_json)
        fw.close()
