# coding:utf-8

from byteplus_sdk.ServiceInfo import ServiceInfo
from byteplus_sdk.Credentials import Credentials
from byteplus_sdk.ApiInfo import ApiInfo

service_info_map = {
    'cn-north-1': ServiceInfo(
        'open.byteplusapi.com',
        {'Accept': 'application/json'},
        Credentials('', '', 'live', 'cn-north-1'),
        10, 10, "https")
}

api_info = {
    "ListStorageSpace": ApiInfo("POST", "/", {"Action": "ListStorageSpace", "Version": "2020-08-01"}, {}, {}),
    "ListStorageSpaceDetail": ApiInfo("POST", "/", {"Action": "ListStorageSpaceDetail", "Version": "2020-08-01"}, {}, {})
}