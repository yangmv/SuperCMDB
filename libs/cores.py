#!/usr/bin/env python
#encoding:utf-8
'''
@author: yangmv
@file: cores.py
@time: 18/12/13下午3:35
'''

from ops.settings import STORAGE_API_URL
from libs.Aliyun.oss import OSSApi

def get_oss_config():
    '''从接口获取OSS配置'''
    try:
        # ret = requests.get(STORAGE_API_URL)
        # data = json.loads(ret.text)['data']
        # 接口暂时不可用
        data = {
            "STORAGE_REGION":"cn-shanghai",
            "STORAGE_NAME":"test01",
            "STORAGE_PATH":"record",
            "STORAGE_KEY_ID":"11111111111111",
            "STORAGE_KEY_SECRET":"222222222222222"
        }
    except Exception as e:
        data = None
    return data

def initOSS_obj():
    '''实例化OSS obj'''
    oss_config = get_oss_config()
    if oss_config:
        # 回放日志存储到OSS
        obj = OSSApi(
        oss_config.get('STORAGE_KEY_ID'),oss_config.get('STORAGE_KEY_SECRET'),oss_config.get('STORAGE_REGION'),
        oss_config.get('STORAGE_NAME'),oss_config.get('STORAGE_PATH'))
        return obj
    else:
        return None