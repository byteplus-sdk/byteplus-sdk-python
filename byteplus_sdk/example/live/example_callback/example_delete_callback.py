# coding:utf-8
import json

from byteplus_sdk.live.LiveService import LiveService

if __name__ == '__main__':
    live_service = LiveService()
    ak = ""
    sk = ""
    live_service.set_ak(ak)
    live_service.set_sk(sk)
    body = {
        "MessageType": "record",
        "Vhost": "vhost",
    }
    resp = live_service.delete_callback(body)
    print(resp)
