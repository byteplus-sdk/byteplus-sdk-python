# coding:utf-8
from __future__ import print_function

from byteplus_sdk.vod.VodService import VodService
import byteplus_sdk.vod.models.request.request_vod_pb2 as rq
import byteplus_sdk.vod.models.response.response_vod_pb2 as rsp

if __name__ == '__main__':
    service = VodService()
    subFilter = rq.GetVodMediaPlayDataFilter(
        Op='in',
        Field='your field',
        Values=['your value'],
    )
    filter = rq.GetVodMediaPlayDataFilter(
        Logic='and',
        Filters=[subFilter]
    )
    req = rq.GetVodMediaPlayDataRequest(
        AppID='your app_id',
        StartTime='2025-07-16T00:00:00+00:00',
        EndTime='2025-07-16T08:00:00+00:00',
        Platform='xxx',
        Metrics=['aaa', 'bbb'],
        Dimensions=['ccc', 'ddd'],
        Filter=filter
    )
    resp =  rsp.GetVodMediaPlayDataResponse()
    resp = service.get_vod_media_play_data(req)
    print(resp)
    print(resp.Result.Data[0]['aaa'])
    print(resp.Result.Data[0]['ccc'])
