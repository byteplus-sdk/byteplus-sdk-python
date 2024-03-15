# coding:utf-8

from byteplus.ServiceInfo import ServiceInfo
from byteplus.Credentials import Credentials
from byteplus.ApiInfo import ApiInfo

service_info_map = {
    'cn-north-1': ServiceInfo(
        'open.byteplusapi.com',
        {'Accept': 'application/json'},
        Credentials('', '', 'live', 'cn-north-1'),
        10, 10, "https")
}

api_info = {
    "CopyCasterPVWToPGM": ApiInfo("POST", "/", {"Action": "CopyCasterPVWToPGM", "Version": "2018-01-01"}, {}, {}),
    "UpdateCasterImageCollection": ApiInfo("POST", "/", {"Action": "UpdateCasterImageCollection", "Version": "2018-01-01"}, {}, {}),
    "GetCasterResource": ApiInfo("POST", "/", {"Action": "GetCasterResource", "Version": "2018-01-01"}, {}, {}),
    "StopCaster": ApiInfo("POST", "/", {"Action": "StopCaster", "Version": "2018-01-01"}, {}, {}),
    "SwitchCasterResourceImage": ApiInfo("POST", "/", {"Action": "SwitchCasterResourceImage", "Version": "2018-01-01"}, {}, {}),
    "SwitchCasterLayout": ApiInfo("POST", "/", {"Action": "SwitchCasterLayout", "Version": "2018-01-01"}, {}, {}),
    "SwitchCasterResourceOPED": ApiInfo("POST", "/", {"Action": "SwitchCasterResourceOPED", "Version": "2018-01-01"}, {}, {}),
    "SwitchCasterResource": ApiInfo("POST", "/", {"Action": "SwitchCasterResource", "Version": "2018-01-01"}, {}, {}),
    "CreateCasterResourceImages": ApiInfo("POST", "/", {"Action": "CreateCasterResourceImages", "Version": "2018-01-01"}, {}, {}),
    "UpdateCasterLayout": ApiInfo("POST", "/", {"Action": "UpdateCasterLayout", "Version": "2018-01-01"}, {}, {}),
    "CreateCaster": ApiInfo("POST", "/", {"Action": "CreateCaster", "Version": "2018-01-01"}, {}, {}),
    "CreateCasterArrange": ApiInfo("POST", "/", {"Action": "CreateCasterArrange", "Version": "2018-01-01"}, {}, {}),
    "CreateCasterResourceImage": ApiInfo("POST", "/", {"Action": "CreateCasterResourceImage", "Version": "2018-01-01"}, {}, {}),
    "CreateCasterResource": ApiInfo("POST", "/", {"Action": "CreateCasterResource", "Version": "2018-01-01"}, {}, {}),
    "DeleteCasterLayout": ApiInfo("POST", "/", {"Action": "DeleteCasterLayout", "Version": "2018-01-01"}, {}, {}),
    "DeleteCasterArrange": ApiInfo("POST", "/", {"Action": "DeleteCasterArrange", "Version": "2018-01-01"}, {}, {}),
    "DeleteCasterResourceImage": ApiInfo("POST", "/", {"Action": "DeleteCasterResourceImage", "Version": "2018-01-01"}, {}, {}),
    "DeleteCasterResourceOPED": ApiInfo("POST", "/", {"Action": "DeleteCasterResourceOPED", "Version": "2018-01-01"}, {}, {}),
    "RemoveCasterResource": ApiInfo("POST", "/", {"Action": "RemoveCasterResource", "Version": "2018-01-01"}, {}, {}),
    "StartCaster": ApiInfo("POST", "/", {"Action": "StartCaster", "Version": "2018-01-01"}, {}, {}),
    "StartCasterOPEDArrange": ApiInfo("POST", "/", {"Action": "StartCasterOPEDArrange", "Version": "2018-01-01"}, {}, {}),
    "UpdateCasterArrange": ApiInfo("POST", "/", {"Action": "UpdateCasterArrange", "Version": "2018-01-01"}, {}, {}),
    "UpdateCasterConfig": ApiInfo("POST", "/", {"Action": "UpdateCasterConfig", "Version": "2018-01-01"}, {}, {}),
    "ListCasters": ApiInfo("POST", "/", {"Action": "ListCasters", "Version": "2018-01-01"}, {}, {}),
    "CreateCasterResourceOPED": ApiInfo("POST", "/", {"Action": "CreateCasterResourceOPED", "Version": "2018-01-01"}, {}, {}),
    "GetCasterLayout": ApiInfo("POST", "/", {"Action": "GetCasterLayout", "Version": "2018-01-01"}, {}, {}),
    "GetCasterArrange": ApiInfo("POST", "/", {"Action": "GetCasterArrange", "Version": "2018-01-01"}, {}, {}),
    "GetCasterConfig": ApiInfo("POST", "/", {"Action": "GetCasterConfig", "Version": "2018-01-01"}, {}, {}),
    "GetCasterResourceVodInfo": ApiInfo("POST", "/", {"Action": "GetCasterResourceVodInfo", "Version": "2018-01-01"}, {}, {})
}