# coding:utf-8
from __future__ import print_function
from byteplus_sdk.vod.VodService import VodService
from byteplus_sdk.vod.models.request.request_vod_pb2 import VodGetPlayInfoRequest, VodCreateHlsDecryptionKeyRequest
if __name__ == '__main__':
    vod_service = VodService()
    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('ak')
    # vod_service.set_sk('sk')
    try:
        req = VodCreateHlsDecryptionKeyRequest()
        req.SpaceName = "your spaceName"
        resp = vod_service.create_hls_decryption_key(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code == '':
            print(resp)
        else:
            print(resp.ResponseMetadata.Error)
    print('*' * 100)