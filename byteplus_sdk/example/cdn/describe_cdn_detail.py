#  -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../")
import datetime

from byteplus_sdk.example.cdn import ak, sk
from byteplus_sdk.cdn.service import CDNService

if __name__ == '__main__':
    svc = CDNService()
    svc.set_ak(ak)
    svc.set_sk(sk)
    now = int(datetime.datetime.now().strftime("%s"))
    body = {
        'StartTime': now - 3600,
        'EndTime': now,
        'Metric': 'pv',
        'Domain': 'example.com',
        'Interval': '5min',
        'Protocol': 'http',
        'IpVersion': 'ipv4'
    }

    resp = svc.describe_cdn_data_detail(body)
    print(resp)
