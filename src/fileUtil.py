#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import io
import sys
from importlib import reload

from src.constants import PASSWORD_FILE_PATH, NOTES_FILE_PATH

reload(sys)


class FileUtil(object):

    @staticmethod
    def getPassword():
        with open(PASSWORD_FILE_PATH, 'r') as fileReader:
            ret = fileReader.read()
            fileReader.close()
            return ret

    @staticmethod
    def getNoteRecords(filePath=NOTES_FILE_PATH):
        data = []
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
