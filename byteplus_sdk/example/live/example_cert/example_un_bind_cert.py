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
        "Domain": "",
    }
    resp = live_service.un_bind_cert(body)
    print(resp)
