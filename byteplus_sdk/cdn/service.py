# coding=utf-8
import json
import threading
from byteplus_sdk.ApiInfo import ApiInfo
from byteplus_sdk.Credentials import Credentials
from byteplus_sdk.base.Service import Service
from byteplus_sdk.ServiceInfo import ServiceInfo

SERVICE_VERSION = "2021-03-01"

service_info_map = {
    "ap-singapore-1": ServiceInfo("open.byteplusapi.com", {'Accept': 'application/json', },
                                  Credentials('', '', "CDN", "ap-singapore-1"), 60 * 1, 60 * 5, 'https'),
}

api_info = {

    "AddCdnDomain": ApiInfo("POST", "/", {
        "Action": "AddCdnDomain", "Version": SERVICE_VERSION}, {}, {}),

    "StartCdnDomain": ApiInfo("POST", "/", {
        "Action": "StartCdnDomain", "Version": SERVICE_VERSION}, {}, {}),

    "StopCdnDomain": ApiInfo("POST", "/", {
        "Action": "StopCdnDomain", "Version": SERVICE_VERSION}, {}, {}),

    "DeleteCdnDomain": ApiInfo("POST", "/", {
        "Action": "DeleteCdnDomain", "Version": SERVICE_VERSION}, {}, {}),

    "ListCdnDomains": ApiInfo("POST", "/", {
        "Action": "ListCdnDomains", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnConfig": ApiInfo("POST", "/", {
        "Action": "DescribeCdnConfig", "Version": SERVICE_VERSION}, {}, {}),

    "UpdateCdnConfig": ApiInfo("POST", "/", {
        "Action": "UpdateCdnConfig", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnData": ApiInfo("POST", "/", {
        "Action": "DescribeCdnData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeEdgeNrtDataSummary": ApiInfo("POST", "/", {
        "Action": "DescribeEdgeNrtDataSummary", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnOriginData": ApiInfo("POST", "/", {
        "Action": "DescribeCdnOriginData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeOriginNrtDataSummary": ApiInfo("POST", "/", {
        "Action": "DescribeOriginNrtDataSummary", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnDataDetail": ApiInfo("POST", "/", {
        "Action": "DescribeCdnDataDetail", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeEdgeStatisticalData": ApiInfo("POST", "/", {
        "Action": "DescribeEdgeStatisticalData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeEdgeTopNrtData": ApiInfo("POST", "/", {
        "Action": "DescribeEdgeTopNrtData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeOriginTopNrtData": ApiInfo("POST", "/", {
        "Action": "DescribeOriginTopNrtData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeEdgeTopStatusCode": ApiInfo("POST", "/", {
        "Action": "DescribeEdgeTopStatusCode", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeOriginTopStatusCode": ApiInfo("POST", "/", {
        "Action": "DescribeOriginTopStatusCode", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeEdgeTopStatisticalData": ApiInfo("POST", "/", {
        "Action": "DescribeEdgeTopStatisticalData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnRegionAndIsp": ApiInfo("POST", "/", {
        "Action": "DescribeCdnRegionAndIsp", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnDomainTopData": ApiInfo("POST", "/", {
        "Action": "DescribeCdnDomainTopData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnService": ApiInfo("POST", "/", {
        "Action": "DescribeCdnService", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeAccountingData": ApiInfo("POST", "/", {
        "Action": "DescribeAccountingData", "Version": SERVICE_VERSION}, {}, {}),

    "SubmitRefreshTask": ApiInfo("POST", "/", {
        "Action": "SubmitRefreshTask", "Version": SERVICE_VERSION}, {}, {}),

    "SubmitPreloadTask": ApiInfo("POST", "/", {
        "Action": "SubmitPreloadTask", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeContentTasks": ApiInfo("POST", "/", {
        "Action": "DescribeContentTasks", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeContentQuota": ApiInfo("POST", "/", {
        "Action": "DescribeContentQuota", "Version": SERVICE_VERSION}, {}, {}),

    "SubmitBlockTask": ApiInfo("POST", "/", {
        "Action": "SubmitBlockTask", "Version": SERVICE_VERSION}, {}, {}),

    "SubmitUnblockTask": ApiInfo("POST", "/", {
        "Action": "SubmitUnblockTask", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeContentBlockTasks": ApiInfo("POST", "/", {
        "Action": "DescribeContentBlockTasks", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnAccessLog": ApiInfo("POST", "/", {
        "Action": "DescribeCdnAccessLog", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeIPInfo": ApiInfo("POST", "/", {
        "Action": "DescribeIPInfo", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeIPListInfo": ApiInfo("POST", "/", {
        "Action": "DescribeIPListInfo", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnUpperIp": ApiInfo("POST", "/", {
        "Action": "DescribeCdnUpperIp", "Version": SERVICE_VERSION}, {}, {}),
}


class CDNService(Service):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(CDNService, "_instance"):
            with CDNService._instance_lock:
                if not hasattr(CDNService, "_instance"):
                    CDNService._instance = object.__new__(cls)
        return CDNService._instance

    def __init__(self, region="ap-singapore-1"):
        self.service_info = CDNService.get_service_info(region)
        self.api_info = CDNService.get_api_info()
        super(CDNService, self).__init__(self.service_info, self.api_info)

    @staticmethod
    def get_service_info(region_name):
        service_info = service_info_map.get(region_name, None)
        if not service_info:
            raise Exception('do not support region %s' % region_name)
        return service_info

    @staticmethod
    def get_api_info():
        return api_info

    def add_cdn_domain(self, params=None):
        if params is None:
            params = {}
        action = "AddCdnDomain"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def start_cdn_domain(self, params=None):
        if params is None:
            params = {}
        action = "StartCdnDomain"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def stop_cdn_domain(self, params=None):
        if params is None:
            params = {}
        action = "StopCdnDomain"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def delete_cdn_domain(self, params=None):
        if params is None:
            params = {}
        action = "DeleteCdnDomain"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def list_cdn_domains(self, params=None):
        if params is None:
            params = {}
        action = "ListCdnDomains"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cdn_config(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnConfig"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def update_cdn_config(self, params=None):
        if params is None:
            params = {}
        action = "UpdateCdnConfig"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cdn_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_edge_nrt_data_summary(self, params=None):
        if params is None:
            params = {}
        action = "DescribeEdgeNrtDataSummary"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cdn_origin_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnOriginData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_origin_nrt_data_summary(self, params=None):
        if params is None:
            params = {}
        action = "DescribeOriginNrtDataSummary"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cdn_data_detail(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnDataDetail"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_edge_statistical_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeEdgeStatisticalData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_edge_top_nrt_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeEdgeTopNrtData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_origin_top_nrt_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeOriginTopNrtData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_edge_top_status_code(self, params=None):
        if params is None:
            params = {}
        action = "DescribeEdgeTopStatusCode"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_origin_top_status_code(self, params=None):
        if params is None:
            params = {}
        action = "DescribeOriginTopStatusCode"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_edge_top_statistical_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeEdgeTopStatisticalData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cdn_region_and_isp(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnRegionAndIsp"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cdn_domain_top_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnDomainTopData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cdn_service(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnService"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_accounting_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeAccountingData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def submit_refresh_task(self, params=None):
        if params is None:
            params = {}
        action = "SubmitRefreshTask"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def submit_preload_task(self, params=None):
        if params is None:
            params = {}
        action = "SubmitPreloadTask"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_content_tasks(self, params=None):
        if params is None:
            params = {}
        action = "DescribeContentTasks"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_content_quota(self, params=None):
        if params is None:
            params = {}
        action = "DescribeContentQuota"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def submit_block_task(self, params=None):
        if params is None:
            params = {}
        action = "SubmitBlockTask"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def submit_unblock_task(self, params=None):
        if params is None:
            params = {}
        action = "SubmitUnblockTask"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_content_block_tasks(self, params=None):
        if params is None:
            params = {}
        action = "DescribeContentBlockTasks"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cdn_access_log(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnAccessLog"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_ip_info(self, params=None):
        if params is None:
            params = {}
        action = "DescribeIPInfo"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_ip_list_info(self, params=None):
        if params is None:
            params = {}
        action = "DescribeIPListInfo"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    # deprecated, use describe_ip_list_info instead
    def describe_iplist_info(self, params=None):
        return self.describe_ip_list_info(params)

    def describe_cdn_upper_ip(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnUpperIp"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json
