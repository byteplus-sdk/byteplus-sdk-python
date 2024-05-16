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
        "Title": "example",
        "Message": "example",
        "Project": "default",
        "Quic": {
            "Switch": False
        },
        "HTTPS": {
            "HTTP2": False,
            "OCSP": False,
            "TlsVersion": [
                "tlsv1.1",
                "tlsv1.2",
                "tlsv1.3"
            ],
            "Hsts": {
                "Switch": True,
                "Ttl": 0,
                "Subdomain": "exclude"
            },
            "ForcedRedirect": {
                "EnableForcedRedirect": False,
                "StatusCode": ""
            }
        },
        "HttpForcedRedirect": {
            "EnableForcedRedirect": False,
            "StatusCode": ""
        },
        "TemplateId": "tpl-example"
    }

    resp = svc.update_cipher_template(body)
    print(resp)
