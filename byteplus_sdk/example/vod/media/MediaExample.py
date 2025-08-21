# coding:utf-8
from __future__ import print_function

from byteplus_sdk.vod.VodService import VodService
from byteplus_sdk.vod.models.request.request_vod_pb2 import VodGetMediaInfosRequest, VodGetRecommendedPosterRequest, \
    VodUpdateMediaPublishStatusRequest, VodUpdateMediaInfoRequest, VodDeleteMediaRequest, VodDeleteTranscodesRequest, \
    VodGetMediaListRequest, VodCreateVideoClassificationRequest, VodUpdateVideoClassificationRequest, \
    VodDeleteVideoClassificationRequest, VodListVideoClassificationsRequest, VodListSnapshotsRequest, \
    VodUpdateMediaStorageClassRequest, VodExtractMediaMetaTaskRequest, VodCreatePlaylistRequest, VodGetPlaylistsRequest, \
    VodUpdatePlaylistRequest, VodDeletePlaylistRequest, VodGetFileInfosRequest, VodDeleteMediaTosFileRequest

if __name__ == '__main__':
    vod_service = VodService()
    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('your ak')
    # vod_service.set_sk('your sk')

    try:
        vids = 'vid1,vid2'
        req = VodGetMediaInfosRequest()
        req.Vids = vids
        resp = vod_service.get_media_infos(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code == '':
            print(resp.Result)
        else:
            print(resp.ResponseMetadata.Error)
    print('*' * 100)


    try:
        vid = 'vid'
        status = 'Unpublished'
        req3 = VodUpdateMediaPublishStatusRequest()
        req3.Vid = vid
        req3.Status = status
        resp3 = vod_service.update_media_publish_status(req3)
    except Exception:
        raise
    else:
        print(resp3)
        if resp3.ResponseMetadata.Error.Code == '':
            print('update media publish status success')
        else:
            print(resp3.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req4 = VodUpdateMediaInfoRequest()
        req4.Vid = 'vid'
        req4.Title.value = 'title'
        req4.Description.value = 'description'
        req4.Tags.value = 'tag1,tag2'
        req4.ClassificationId.value = 0
        resp4 = vod_service.update_media_info(req4)
    except Exception:
        raise
    else:
        print(resp4)
        if resp4.ResponseMetadata.Error.Code == '':
            print('update media info success')
        else:
            print(resp4.ResponseMetadata.Error)

    print('*' * 100)

    try:
        vids = 'vid1,vid2'
        callBackArgs = 'CallBackArgs'
        req5 = VodDeleteMediaRequest()
        req5.Vids = vids
        req5.CallbackArgs = callBackArgs
        resp5 = vod_service.delete_media(req5)
    except Exception:
        raise
    else:
        print(resp5)
        if resp5.ResponseMetadata.Error.Code == '':
            print('delete media info success')
        else:
            print(resp5.ResponseMetadata.Error)

    print('*' * 100)

    try:
        vid = 'vid'
        fileIds = 'fileId1,fileId2'
        callBackArgs = 'CallBackArgs'
        req6 = VodDeleteTranscodesRequest()
        req6.Vid = vid
        req6.FileIds = fileIds
        req6.CallbackArgs = callBackArgs
        resp6 = vod_service.delete_transcodes(req6)
    except Exception:
        raise
    else:
        print(resp6)
        if resp6.ResponseMetadata.Error.Code == '':
            print('delete transcodes info success')
        else:
            print(resp6.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req7 = VodGetMediaListRequest()
        req7.SpaceName = 'your space name'
        req7.Vid = 'your vid'
        req7.Status = 'Published'  #Published/Unpublished
        req7.Order = 'Desc'        #Desc/Asc
        req7.StartTime = '1999-01-01T00:00:00Z'
        req7.EndTime = '2021-04-01T00:00:00Z'
        req7.Offset = '0'
        req7.PageSize = '10'
        req7.ClassificationIds = "1"
        resp7 = vod_service.get_media_list(req7)
    except Exception:
        raise
    else:
        print(resp7)
        if resp7.ResponseMetadata.Error.Code == '':
            print(resp7.Result)
        else:
            print(resp7.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req11 = VodListVideoClassificationsRequest()
        req11.SpaceName = 'your space'
        req11.ClassificationId = 0
        resp11 = vod_service.list_video_classifications(req11)
    except Exception:
        raise
    else:
        print(resp11)
        if resp11.ResponseMetadata.Error.Code == '':
            print(resp11.Result)
        else:
            print(resp11.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req12 = VodListSnapshotsRequest()
        req12.Vid = "your vid"
        resp12 = vod_service.list_snapshots(req12)
    except Exception:
        raise
    else:
        print(resp12)
        if resp12.ResponseMetadata.Error.Code == '':
            print(resp12.Result)
        else:
            print(resp12.ResponseMetadata.Error)

    try:
        vids = "vid1"
        fileIds = "fileid1"
        req13 = VodUpdateMediaStorageClassRequest()
        req13.Vids = vids
        req13.FileIds = fileIds
        req13.StorageClass = "your storage class"
        req13.CallbackArgs = "your callbackargs"
        resp13 = vod_service.update_media_storage_class(req13)
    except Exception:
        raise
    else:
        print(resp13)
        if resp13.ResponseMetadata.Error.Code == '':
            print(resp13.Result)
        else:
            print(resp13.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req14 = VodExtractMediaMetaTaskRequest()
        req14.Vid = "vid"
        resp14 = vod_service.extract_media_meta_task(req14)
    except Exception:
        raise
    else:
        print(resp14)
        if resp14.ResponseMetadata.Error.Code == '':
            print(resp14.Result)
        else:
            print(resp14.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req15 = VodCreatePlaylistRequest()
        req15.SpaceName = 'your space'
        req15.Name = "your Playlist Name"
        req15.Format = "your format"
        req15.Codec = "your codec"
        req15.Definition = "your definition"
        req15.Vids = "your vids"
        req15.StartTime = "your startTime"
        req15.EndTime = "your endTime"
        req15.Cycles = "your cycles"

        resp15 = vod_service.create_playlist(req15)
    except Exception:
        raise
    else:
        print(resp15)
        if resp15.ResponseMetadata.Error.Code == '':
            print(resp15.Result)
        else:
            print(resp15.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req16 = VodGetPlaylistsRequest()
        req16.SpaceName = 'your space'
        req16.Ids = "your Playlist Ids"
        req16.Limit = 0
        req16.Offset = 0

        resp16 = vod_service.get_playlists(req16)
    except Exception:
        raise
    else:
        print(resp16)
        if resp16.ResponseMetadata.Error.Code == '':
            print(resp16.Result)
        else:
            print(resp16.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req17 = VodUpdatePlaylistRequest()
        req17.SpaceName = 'your space'
        req17.Id = "your Playlist Id"
        req17.Name.value = "your Playlist Name"
        req17.Format.value = "your format"
        req17.Codec.value = "your codec"
        req17.Definition.value = "your definition"
        req17.Vids.value = "your vids"
        req17.StartTime.value = "your startTime"
        req17.EndTime.value = "your endTime"
        req17.Cycles.value = "your cycles"

        resp17 = vod_service.update_playlist(req17)
    except Exception:
        raise
    else:
        print(resp17)
        if resp17.ResponseMetadata.Error.Code == '':
            print("update playlist success")
        else:
            print(resp17.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req18 = VodDeletePlaylistRequest()
        req18.SpaceName = 'your space'
        req18.Id = "your Playlist Id"

        resp18 = vod_service.delete_playlist(req18)
    except Exception:
        raise
    else:
        print(resp18)
        if resp18.ResponseMetadata.Error.Code == '':
            print("delete playlist success")
        else:
            print(resp18.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req19 = VodGetFileInfosRequest()
        req19.SpaceName = 'your space'
        req19.EncodedFileNames = "your file names"

        resp19 = vod_service.get_file_infos(req19)
    except Exception:
        raise
    else:
        print(resp19)
        if resp19.ResponseMetadata.Error.Code == '':
            print("get file infos success")
        else:
            print(resp19.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req20 = VodListFileMetaInfosByFileNamesRequest()
        req20.SpaceName = 'your space'
        req20.FileNameEncodeds = "your file names"

        resp20 = vod_service.list_file_meta_infos_by_file_names(req20)
    except Exception:
        raise
    else:
        print(resp20)
        if resp20.ResponseMetadata.Error.Code == '':
            print("list file meta infos by file name success")
        else:
            print(resp20.ResponseMetadata.Error)

    print('*' * 100)

    try:
        req21 = VodDeleteMediaTosFileRequest()
        req21.SpaceName = 'your space'
        req21.FileNames = "your file names"

        resp21 = vod_service.delete_media_tos_file(req21)
    except Exception:
        raise
    else:
        print(resp21)
        if resp21.ResponseMetadata.Error.Code == '':
            print("delete media tos file success")
        else:
            print(resp21.ResponseMetadata.Error)

    print('*' * 100)