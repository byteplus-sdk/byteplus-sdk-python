#  -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../")

from byteplus_sdk.example.cdn import ak, sk
from byteplus_sdk.cdn.service import CDNService


def example():
    cdn_service = CDNService()
    cdn_service.set_ak(ak)
    cdn_service.set_sk(sk)

    rsp = cdn_service.release_template({
        "TemplateId": "tpl-example",
    })
    print(rsp)


if __name__ == '__main__':
    example()
