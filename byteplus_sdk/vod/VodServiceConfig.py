# coding:utf-8

from __future__ import print_function

import threading
from zlib import crc32

from byteplus_sdk.ApiInfo import ApiInfo
from byteplus_sdk.Credentials import Credentials
from byteplus_sdk.ServiceInfo import ServiceInfo
from byteplus_sdk.base.Service import Service


class VodServiceConfig(Service):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, region='ap-singapore-1'):
        self.service_info = VodServiceConfig.get_service_info(region)
        self.api_info = VodServiceConfig.get_api_info()
        self.domain_cache = {}
        self.fallback_domain_weights = {}
        self.update_interval = 10
        self.lock = threading.Lock()
        super(VodServiceConfig, self).__init__(self.service_info, self.api_info)

    @staticmethod
    def get_service_info(region):
        service_info_map = {
            'ap-singapore-1': ServiceInfo("vod.byteplusapi.com", {'Accept': 'application/json'},
                                      Credentials('', '', 'vod', 'ap-singapore-1'), 60, 60,"https"),
        }
        service_info = service_info_map.get(region, None)
        if not service_info:
            raise Exception('Cant find the region, please check it carefully')

        return service_info

    @staticmethod
    def get_api_info():
        api_info = {
            # 播放
            "GetPlayInfo": ApiInfo("GET", "/", {"Action": "GetPlayInfo", "Version": "2023-01-01"}, {}, {}),
            "GetPrivateDrmPlayAuth": ApiInfo("GET", "/", {"Action": "GetPrivateDrmPlayAuth", "Version": "2023-01-01"},
                                             {}, {}),
            # 上传
            "UploadMediaByUrl": ApiInfo("GET", "/", {"Action": "UploadMediaByUrl", "Version": "2023-01-01"}, {}, {}),
            "QueryUploadTaskInfo": ApiInfo("GET", "/", {"Action": "QueryUploadTaskInfo", "Version": "2023-01-01"}, {}, {}),
            "ApplyUploadInfo": ApiInfo("GET", "/", {"Action": "ApplyUploadInfo", "Version": "2023-01-01"}, {}, {}),
            "CommitUploadInfo": ApiInfo("GET", "/", {"Action": "CommitUploadInfo", "Version": "2023-01-01"}, {}, {}),
            # 媒资
            "UpdateMediaInfo": ApiInfo("GET", "/", {"Action": "UpdateMediaInfo", "Version": "2023-01-01"}, {}, {}),
            "UpdateMediaPublishStatus": ApiInfo("GET", "/", {"Action": "UpdateMediaPublishStatus", "Version": "2023-01-01"}, {}, {}),
            "GetMediaInfos": ApiInfo("GET", "/", {"Action": "GetMediaInfos", "Version": "2023-01-01"}, {}, {}),
            "DeleteMedia": ApiInfo("GET", "/", {"Action": "DeleteMedia", "Version": "2023-01-01"}, {}, {}),
            "DeleteTranscodes": ApiInfo("GET", "/", {"Action": "DeleteTranscodes", "Version": "2023-01-01"}, {}, {}),
            "GetMediaList": ApiInfo("GET", "/", {"Action": "GetMediaList", "Version": "2023-01-01"}, {}, {}),
            "GetSubtitleInfoList": ApiInfo("GET", "/", {"Action": "GetSubtitleInfoList", "Version": "2023-01-01"}, {}, {}),
            "UpdateSubtitleStatus": ApiInfo("GET", "/", {"Action": "UpdateSubtitleStatus", "Version": "2023-01-01"}, {}, {}),
            "UpdateSubtitleInfo": ApiInfo("GET", "/", {"Action": "UpdateSubtitleInfo", "Version": "2023-01-01"}, {}, {}),
            "ListVideoClassifications": ApiInfo("GET", "/",{"Action": "ListVideoClassifications", "Version": "2023-01-01"}, {},{}),
            "CreatePlaylist": ApiInfo("GET", "/",{"Action": "CreatePlaylist", "Version": "2023-01-01"}, {},{}),
            "GetPlaylists": ApiInfo("GET", "/",{"Action": "GetPlaylists", "Version": "2023-01-01"}, {},{}),
            "UpdatePlaylist": ApiInfo("GET", "/",{"Action": "UpdatePlaylist", "Version": "2023-01-01"}, {},{}),
            "DeletePlaylist": ApiInfo("GET", "/",{"Action": "DeletePlaylist", "Version": "2023-01-01"}, {},{}),

            # 转码
            "StartWorkflow": ApiInfo("GET", "/", {"Action": "StartWorkflow", "Version": "2023-01-01"}, {}, {}),
            "RetrieveTranscodeResult": ApiInfo("GET", "/", {"Action": "RetrieveTranscodeResult", "Version": "2023-01-01"}, {}, {}),
            "GetWorkflowExecution": ApiInfo("GET", "/", {"Action": "GetWorkflowExecution", "Version": "2023-01-01"}, {}, {}),
            # 空间管理
            "CreateSpace": ApiInfo("GET", "/", {"Action": "CreateSpace", "Version": "2023-01-01"}, {}, {}),
            "ListSpace": ApiInfo("GET", "/", {"Action": "ListSpace", "Version": "2023-01-01"}, {}, {}),
            "GetSpaceDetail": ApiInfo("GET", "/", {"Action": "GetSpaceDetail", "Version": "2023-01-01"}, {}, {}),
            "UpdateSpaceUploadConfig": ApiInfo("GET", "/", {"Action": "UpdateSpaceUploadConfig", "Version": "2023-01-01"}, {}, {}),
            "DescribeVodSpaceStorageData": ApiInfo("GET", "/", {"Action": "DescribeVodSpaceStorageData", "Version": "2023-01-01"},{}, {}),
            # 分发加速
            "ListDomain": ApiInfo("GET", "/", {"Action": "ListDomain", "Version": "2023-01-01"}, {}, {}),
            "CreateCdnRefreshTask": ApiInfo("GET", "/", {"Action": "CreateCdnRefreshTask", "Version": "2023-01-01"}, {}, {}),
            "CreateCdnPreloadTask": ApiInfo("GET", "/", {"Action": "CreateCdnPreloadTask", "Version": "2023-01-01"}, {}, {}),
            "ListCdnTasks": ApiInfo("GET", "/", {"Action": "ListCDNTasks", "Version": "2023-01-01"}, {}, {}),
            "ListCdnAccessLog": ApiInfo("GET", "/", {"Action": "ListCdnAccessLog", "Version": "2023-01-01"}, {}, {}),
            "ListCdnTopAccessUrl": ApiInfo("GET", "/", {"Action": "ListCdnTopAccessUrl", "Version": "2023-01-01"}, {}, {}),
            "DescribeVodDomainBandwidthData": ApiInfo("GET", "/", {"Action": "DescribeVodDomainBandwidthData", "Version": "2023-01-01"}, {}, {}),
            "DescribeVodDomainTrafficData": ApiInfo("GET", "/", {"Action": "DescribeVodDomainTrafficData", "Version": "2023-01-01"}, {}, {}),
            "ListCdnUsageData": ApiInfo("GET", "/", {"Action": "ListCdnUsageData", "Version": "2023-01-01"}, {}, {}),
            "ListCdnStatusData": ApiInfo("GET", "/", {"Action": "ListCdnStatusData", "Version": "2023-01-01"}, {}, {}),
            "DescribeIpInfo": ApiInfo("GET", "/", {"Action": "DescribeIpInfo", "Version": "2023-01-01"}, {}, {}),
            "ListCdnPvData": ApiInfo("GET", "/", {"Action": "ListCdnPvData", "Version": "2023-01-01"}, {}, {}),
            # 回调管理
            "AddCallbackSubscription": ApiInfo("GET", "/", {"Action": "AddCallbackSubscription", "Version": "2023-01-01"}, {}, {}),
            "SetCallbackEvent": ApiInfo("GET", "/", {"Action": "SetCallbackEvent", "Version": "2023-01-01"}, {}, {}),
            # 计量计费
            "DescribeVodSpaceTranscodeData": ApiInfo("GET", "/", {"Action": "DescribeVodSpaceTranscodeData", "Version": "2023-01-01"}, {}, {}),
            "DescribeVodSnapshotData": ApiInfo("GET", "/", {"Action": "DescribeVodSnapshotData", "Version": "2023-01-01"}, {}, {}),
            # 商业drm
            "GetDrmLicense": ApiInfo("POST", "/", {"Action": "GetDrmLicense", "Version": "2023-01-01"}, {}, {}),
            "GetFairPlayCert": ApiInfo("GET", "/", {"Action": "GetFairPlayCert", "Version": "2023-01-01"}, {}, {}),
        }
        return api_info

    @staticmethod
    def crc32(file_path):
        prev = 0
        for eachLine in open(file_path, "rb"):
            prev = crc32(eachLine, prev)
        return prev & 0xFFFFFFFF
