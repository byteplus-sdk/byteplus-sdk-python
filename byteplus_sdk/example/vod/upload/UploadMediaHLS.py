# coding:utf-8
from __future__ import print_function

import json

from byteplus_sdk.util.Functions import Function
from byteplus_sdk.vod.VodService import VodService
from byteplus_sdk.vod.models.request.request_vod_pb2 import VodUploadMediaRequest

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('your ak')
    vod_service.set_sk('your sk')

    space_name = 'your space name'
    file_path = 'your m3u8 file path'  # e.g., /path/to/video.m3u8

    get_meta_function = Function.get_meta_func()
    snapshot_function = Function.get_snapshot_func(2.3)
    apply_function = Function.get_add_option_info_func("title1", "tag1", "desc1")

    try:
        req = VodUploadMediaRequest()
        req.SpaceName = space_name
        req.FilePath = file_path
        req.Functions = json.dumps([get_meta_function, snapshot_function])
        req.CallbackArgs = ''
        # The path in the storage space, should be set to prevent overwriting existing hls ts files
        req.FileName = 'hello/video.m3u8'
        req.FileExtension = '.m3u8'
        req.StorageClass = 0
        # Set SupportParseManifest to True to enable HLS manifest parsing and segment uploading
        req.SupportParseManifest = True
        resp = vod_service.upload_media(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code == '':
            print(resp.Result.Data)
            print(resp.Result.Data.Vid)
            print(resp.Result.Data.PosterUri)
            print(resp.Result.Data.SourceInfo.FileName)
            print(resp.Result.Data.SourceInfo.Height)
            print(resp.Result.Data.SourceInfo.Width)
        else:
            print(resp.ResponseMetadata.Error)
            print(resp.ResponseMetadata.RequestId)
