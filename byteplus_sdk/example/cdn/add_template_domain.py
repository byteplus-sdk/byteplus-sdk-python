#  -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../")

from byteplus_sdk.example.cdn import ak, sk
from byteplus_sdk.cdn.service import CDNService

if __name__ == '__main__':
    svc = CDNService()
    svc.set_ak(ak)
    svc.set_sk(sk)

    body = {
        "ServiceRegion": "global",
        "Project": "default",
        "ServiceTemplateId": "tpl-example",
        "CertId": "cert-example",
        "CipherTemplateId": "tpl-example",
        "Domain": "example.com",
        "HTTPSSwitch": "on"
    }

    resp = svc.add_template_domain(body)
    print(resp)
