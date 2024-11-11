# coding:utf-8
from __future__ import print_function

from byteplus_sdk.vod.VodService import VodService
from byteplus_sdk.vod.models.request.request_vod_pb2 import VodGetDrmLicenseRequest

if __name__ == '__main__':

    vod_service = VodService()
    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('your ak')
    vod_service.set_sk('your sk')
    try:
        certId = "your cert id"
        expire = 600  # seconds
        resp = vod_service.get_fairplay_cert_url(certId, expire)
    except Exception:
        raise
    else:
        print(resp)
    print('*' * 100)
