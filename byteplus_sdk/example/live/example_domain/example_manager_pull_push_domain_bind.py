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
        "PullDomain": "",
        "PushDomain": "",
    }
    resp = live_service.manager_pull_push_domain_bind(body)
    print(resp)
