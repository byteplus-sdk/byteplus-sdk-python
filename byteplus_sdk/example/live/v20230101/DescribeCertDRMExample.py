# coding:utf-8
from byteplus_sdk.live.v20230101.live_service import LiveService

if __name__ == '__main__':
    service = LiveService()

    # call below method if you dont set ak and sk in $HOME/.byteplus/config
    service.set_ak('ak')
    service.set_sk('sk')

    query = {}

    resp = service.describe_cert_drm(query)
    print(resp)
