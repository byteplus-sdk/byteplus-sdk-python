# coding:utf-8
from __future__ import print_function

import json

from byteplus_sdk.sms.SmsService import SmsService
from byteplus_sdk.const.Const import *

if __name__ == '__main__':
    # oversea
    sms_service = SmsService(REGION_AP_SINGAPORE1)
    # cn
    # sms_service = SmsService()

    # call below method if you dont set ak and sk in $HOME/.volc/config
    sms_service.set_ak('ak')
    sms_service.set_sk('sk')
    # sms_service.set_scheme("http")
    # sms_service.set_scheme("https")
    # sms_service.set_host('host')

    # body = {
    #     "SmsAccount": "smsAccount",
    #     "From": "BytePlus",
    #     "TemplateID": "ST_xxx",
    #     "TemplateParam": "{\"code\": \"111\"}",
    #     "PhoneNumbers": "+65xxxxxxxx",
    #     "Tag": "tag",
    # }
    #
    # resp = sms_service.send_sms(body)
    # print(resp)

    body = {
        "SmsAccount": "smsAccount",
        "Sign": "signature",
        "From": "BytePlus",
        "TemplateID": "ST_xxx",
        "Messages": [{"TemplateParam": "{\"code\": \"1234\"}", "PhoneNumber": "+65xxxxxxxx"}],
        "Tag": "tag",
    }

    resp = sms_service.send_batch_sms(body)
    print(resp)

    # body = {
    #     "SmsAccount": "smsAccount",
    #     "From": "BytePlus",
    #     "TemplateID": "ST_xxx",
    #     "PhoneNumber": "+65xxxxxxxx",
    #     "CodeType": 6,
    #     "TryCount": 3,
    #     "ExpireTime": 240,
    #     "Scene": "Test"
    # }
    #
    # resp = sms_service.send_sms_verify_code(body)
    # print(resp)
    #
    # body = {
    #     "SmsAccount": "smsAccount",
    #     "PhoneNumber": "+65xxxxxxxx",
    #     "Scene": "Test",
    #     "Code": "123456"
    # }
    #
    # resp = sms_service.check_sms_verify_code(body)
    # print(resp)
    #
    # body = {
    #     "MessageIDs": ["test_msg_id"]
    # }
    # resp = sms_service.conversion(body)
    # print(resp)
