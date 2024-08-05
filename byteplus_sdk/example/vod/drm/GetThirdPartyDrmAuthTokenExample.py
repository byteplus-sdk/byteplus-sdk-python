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
        vid = 'your vid'
        drmType = "your drm type"
        req = VodGetDrmLicenseRequest()
        req.Vid = vid
        req.ThirdPartyDrmType = drmType
        expire = 60  # seconds
        resp = vod_service.get_third_party_drm_auth_token(req, expire)
    except Exception:
        raise
    else:
        print(resp)
    print('*' * 100)
