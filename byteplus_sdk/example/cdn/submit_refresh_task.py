#  -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../../../")
from byteplus_sdk.example.cdn import ak, sk
from byteplus_sdk.cdn.service import CDNService

if __name__ == '__main__':
    svc = CDNService()
    svc.set_ak(ak)
    svc.set_sk(sk)
    print(ak, sk)
    body = {
        "Type": "file",
        "Urls": "http://example.com/1.txt\nhttp://example.com/2.jpg",
    }

    resp = svc.submit_refresh_task(body)
    print(resp)
