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

    body = {
        'Domain': 'example.com',
    }

    resp = svc.stop_cdn_domain(body)
    print(resp)
