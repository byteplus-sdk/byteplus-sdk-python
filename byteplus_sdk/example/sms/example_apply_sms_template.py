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
    # sms_service.set_host('host')

    body = {
        "SubAccount": "subAccount",
        "Area": AREA_OVERSEAS,
        "ChannelType": SMS_CHANNEL_TYPE_I18N_MKT,
        "Content": "We're offering our xxxx community 20% off with code THANKYOU. It's our way of showing our "
                   "appreciation to you for standing by us in this time. Shop Now: "
                   "https://webhook.site/edd2b39a-6c8d-4161-a310-36a470c840d4",
        "Desc": "Test SDK",
        "Name": "template_name",
        "ShortUrlConfig": {
            "IsEnabled": ENABLE_STATUS_ENABLE,
            "IsNeedClickDetails": ENABLE_STATUS_NOT_ENABLE
        }
    }

    resp = sms_service.apply_sms_template(body)
    print(resp)
