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
        "Vhost": "",
        "App": "",
        "status": 1,
        "SuffixName": "",
        "Preset": "",
        "FPS": 30,
    }
    resp = live_service.create_transcode_preset(body)
    print(resp)
