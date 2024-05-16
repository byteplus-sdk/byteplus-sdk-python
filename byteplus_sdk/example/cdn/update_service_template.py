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
        "OriginProtocol": "http",
        "OriginHost": "",
        "Origin": [
            {
                "OriginAction": {
                    "OriginLines": [
                        {
                            "Address": "example.com",
                            "HttpPort": "80",
                            "HttpsPort": "443",
                            "InstanceType": "domain",
                            "OriginHost": "",
                            "OriginType": "primary",
                            "Weight": "1"
                        }
                    ]
                }
            }
        ],
        "TemplateId": "tpl-example"
    }

    resp = svc.update_service_template(body)
    print(resp)
