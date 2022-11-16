# coding:utf-8

from byteplus_sdk.live.LiveService import LiveService


def example_list_storagespace(live_service):
    body = {
        "PageSize": 10,
        "PageNum": 1,
    }
    resp = live_service.list_storagespace(body)
    print(resp)


def example_describe_live_storagespace_data(live_service):
    body = {
        "DomainList": ["example.com", "example2.com"],
        "StartTime": "2022-07-13T00:00:00Z",
        "EndTime": "2022-07-17T00:00:00Z",
        "Aggregation": 86400,
    }
    resp = live_service.describe_live_storagespace_data(body)
    print(resp)


if __name__ == '__main__':
    live_service = LiveService()
    ak = ""
    sk = ""
    live_service.set_ak(ak)
    live_service.set_sk(sk)
    example_list_storagespace(live_service)
    example_describe_live_storagespace_data(live_service)
