#  -*- coding: utf-8 -*-
import json
import threading

from byteplus_sdk.ApiInfo import ApiInfo
from byteplus_sdk.Credentials import Credentials
from byteplus_sdk.base.Service import Service
from byteplus_sdk.ServiceInfo import ServiceInfo

GET = "GET"
POST = "POST"
SERVICE_VERSION = "2021-03-01"

service_info_map = {
    "ap-singapore-1": ServiceInfo("open.byteplusapi.com", {'accept': 'application/json', },
                              Credentials('', '', "CDN", "ap-singapore-1"), 60 * 1, 60 * 5, "https"),
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

    "DescribeDistrictIspData": ApiInfo("POST", "/", {
        "Action": "DescribeDistrictIspData", "Version": SERVICE_VERSION}, {}, {}),

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

    "ListResourceTags": ApiInfo("POST", "/", {
        "Action": "ListResourceTags", "Version": SERVICE_VERSION}, {}, {}),

    "AddCdnCertificate": ApiInfo("POST", "/", {
        "Action": "AddCdnCertificate", "Version": SERVICE_VERSION}, {}, {}),

    "ListCertInfo": ApiInfo("POST", "/", {
        "Action": "ListCertInfo", "Version": SERVICE_VERSION}, {}, {}),

    "ListCdnCertInfo": ApiInfo("POST", "/", {
        "Action": "ListCdnCertInfo", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCertConfig": ApiInfo("POST", "/", {
        "Action": "DescribeCertConfig", "Version": SERVICE_VERSION}, {}, {}),

    "BatchDeployCert": ApiInfo("POST", "/", {
        "Action": "BatchDeployCert", "Version": SERVICE_VERSION}, {}, {}),

    "DeleteCdnCertificate": ApiInfo("POST", "/", {
        "Action": "DeleteCdnCertificate", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeAccountingSummary": ApiInfo("POST", "/", {
        "Action": "DescribeAccountingSummary", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeTemplates": ApiInfo("POST", "/", {
        "Action": "DescribeTemplates", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeServiceTemplate": ApiInfo("POST", "/", {
        "Action": "DescribeServiceTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCipherTemplate": ApiInfo("POST", "/", {
        "Action": "DescribeCipherTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "CreateCipherTemplate": ApiInfo("POST", "/", {
        "Action": "CreateCipherTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "UpdateServiceTemplate": ApiInfo("POST", "/", {
        "Action": "UpdateServiceTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "UpdateCipherTemplate": ApiInfo("POST", "/", {
        "Action": "UpdateCipherTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "DuplicateTemplate": ApiInfo("POST", "/", {
        "Action": "DuplicateTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "LockTemplate": ApiInfo("POST", "/", {
        "Action": "LockTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "DeleteTemplate": ApiInfo("POST", "/", {
        "Action": "DeleteTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeTemplateDomains": ApiInfo("POST", "/", {
        "Action": "DescribeTemplateDomains", "Version": SERVICE_VERSION}, {}, {}),

    "AddTemplateDomain": ApiInfo("POST", "/", {
        "Action": "AddTemplateDomain", "Version": SERVICE_VERSION}, {}, {}),

    "UpdateTemplateDomain": ApiInfo("POST", "/", {
        "Action": "UpdateTemplateDomain", "Version": SERVICE_VERSION}, {}, {}),

    "CreateServiceTemplate": ApiInfo("POST", "/", {
        "Action": "CreateServiceTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "CreateTemplateVersion": ApiInfo("POST", "/", {
        "Action": "CreateTemplateVersion", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeTemplateReleaseVersions": ApiInfo("POST", "/", {
        "Action": "DescribeTemplateReleaseVersions", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeDomainShared": ApiInfo("POST", "/", {
        "Action": "DescribeDomainShared", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeCdnIP": ApiInfo("POST", "/", {
        "Action": "DescribeCdnIP", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeDistrictData": ApiInfo("POST", "/", {
        "Action": "DescribeDistrictData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeEdgeData": ApiInfo("POST", "/", {
        "Action": "DescribeEdgeData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeDistrictSummary": ApiInfo("POST", "/", {
        "Action": "DescribeDistrictSummary", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeEdgeSummary": ApiInfo("POST", "/", {
        "Action": "DescribeEdgeSummary", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeOriginData": ApiInfo("POST", "/", {
        "Action": "DescribeOriginData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeOriginSummary": ApiInfo("POST", "/", {
        "Action": "DescribeOriginSummary", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeUserData": ApiInfo("POST", "/", {
        "Action": "DescribeUserData", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeDistrictRanking": ApiInfo("POST", "/", {
        "Action": "DescribeDistrictRanking", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeEdgeRanking": ApiInfo("POST", "/", {
        "Action": "DescribeEdgeRanking", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeOriginRanking": ApiInfo("POST", "/", {
        "Action": "DescribeOriginRanking", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeEdgeStatusCodeRanking": ApiInfo("POST", "/", {
        "Action": "DescribeEdgeStatusCodeRanking", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeOriginStatusCodeRanking": ApiInfo("POST", "/", {
        "Action": "DescribeOriginStatusCodeRanking", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeStatisticalRanking": ApiInfo("POST", "/", {
        "Action": "DescribeStatisticalRanking", "Version": SERVICE_VERSION}, {}, {}),

    "BatchUpdateCdnConfig": ApiInfo("POST", "/", {
        "Action": "BatchUpdateCdnConfig", "Version": SERVICE_VERSION}, {}, {}),

    "AddCertificate": ApiInfo("POST", "/", {
        "Action": "AddCertificate", "Version": SERVICE_VERSION}, {}, {}),

    "DeleteUsageReport": ApiInfo("POST", "/", {
        "Action": "DeleteUsageReport", "Version": SERVICE_VERSION}, {}, {}),

    "CreateUsageReport": ApiInfo("POST", "/", {
        "Action": "CreateUsageReport", "Version": SERVICE_VERSION}, {}, {}),

    "ListUsageReports": ApiInfo("POST", "/", {
        "Action": "ListUsageReports", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeSharedConfig": ApiInfo("POST", "/", {
        "Action": "DescribeSharedConfig", "Version": SERVICE_VERSION}, {}, {}),

    "ListSharedConfig": ApiInfo("POST", "/", {
        "Action": "ListSharedConfig", "Version": SERVICE_VERSION}, {}, {}),

    "DeleteSharedConfig": ApiInfo("POST", "/", {
        "Action": "DeleteSharedConfig", "Version": SERVICE_VERSION}, {}, {}),

    "UpdateSharedConfig": ApiInfo("POST", "/", {
        "Action": "UpdateSharedConfig", "Version": SERVICE_VERSION}, {}, {}),

    "AddSharedConfig": ApiInfo("POST", "/", {
        "Action": "AddSharedConfig", "Version": SERVICE_VERSION}, {}, {}),

    "TagResources": ApiInfo("POST", "/", {
        "Action": "TagResources", "Version": SERVICE_VERSION}, {}, {}),

    "UntagResources": ApiInfo("POST", "/", {
        "Action": "UntagResources", "Version": SERVICE_VERSION}, {}, {}),

    "ReleaseTemplate": ApiInfo("POST", "/", {
        "Action": "ReleaseTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "CreateRuleEngineTemplate": ApiInfo("POST", "/", {
        "Action": "CreateRuleEngineTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "UpdateRuleEngineTemplate": ApiInfo("POST", "/", {
        "Action": "UpdateRuleEngineTemplate", "Version": SERVICE_VERSION}, {}, {}),

    "DescribeRuleEngineTemplate": ApiInfo("POST", "/", {
        "Action": "DescribeRuleEngineTemplate", "Version": SERVICE_VERSION}, {}, {}),


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
        
    @staticmethod
    def use_post():
        return POST

    @staticmethod
    def use_get():
        return GET

    def send_request(self, action, params, method=POST):
        method = str(method).upper()
        if method == 'POST':
            res = self.json(action, [], json.dumps(params))
        elif method == "GET":
            self.get_api_info()[action].method = self.use_get()
            res = self.request(action, params, json.dumps({}))
            self.get_api_info()[action].method = self.use_post()
        else:
            raise Exception("not support method %s" % method)
        return res

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

    def describe_district_isp_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeDistrictIspData"
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

    def list_resource_tags(self, params=None):
        if params is None:
            params = {}
        action = "ListResourceTags"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def add_cdn_certificate(self, params=None):
        if params is None:
            params = {}
        action = "AddCdnCertificate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def list_cert_info(self, params=None):
        if params is None:
            params = {}
        action = "ListCertInfo"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def list_cdn_cert_info(self, params=None):
        if params is None:
            params = {}
        action = "ListCdnCertInfo"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cert_config(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCertConfig"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def batch_deploy_cert(self, params=None):
        if params is None:
            params = {}
        action = "BatchDeployCert"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def delete_cdn_certificate(self, params=None):
        if params is None:
            params = {}
        action = "DeleteCdnCertificate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_accounting_summary(self, params=None):
        if params is None:
            params = {}
        action = "DescribeAccountingSummary"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_templates(self, params=None):
        if params is None:
            params = {}
        action = "DescribeTemplates"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_service_template(self, params=None):
        if params is None:
            params = {}
        action = "DescribeServiceTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cipher_template(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCipherTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def create_cipher_template(self, params=None):
        if params is None:
            params = {}
        action = "CreateCipherTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def update_service_template(self, params=None):
        if params is None:
            params = {}
        action = "UpdateServiceTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def update_cipher_template(self, params=None):
        if params is None:
            params = {}
        action = "UpdateCipherTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def duplicate_template(self, params=None):
        if params is None:
            params = {}
        action = "DuplicateTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def lock_template(self, params=None):
        if params is None:
            params = {}
        action = "LockTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def delete_template(self, params=None):
        if params is None:
            params = {}
        action = "DeleteTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_template_domains(self, params=None):
        if params is None:
            params = {}
        action = "DescribeTemplateDomains"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def add_template_domain(self, params=None):
        if params is None:
            params = {}
        action = "AddTemplateDomain"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def update_template_domain(self, params=None):
        if params is None:
            params = {}
        action = "UpdateTemplateDomain"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def create_service_template(self, params=None):
        if params is None:
            params = {}
        action = "CreateServiceTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def create_template_version(self, params=None):
        if params is None:
            params = {}
        action = "CreateTemplateVersion"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_template_release_versions(self, params=None):
        if params is None:
            params = {}
        action = "DescribeTemplateReleaseVersions"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_domain_shared(self, params=None):
        if params is None:
            params = {}
        action = "DescribeDomainShared"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_cdn_ip(self, params=None):
        if params is None:
            params = {}
        action = "DescribeCdnIP"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_district_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeDistrictData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_edge_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeEdgeData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_district_summary(self, params=None):
        if params is None:
            params = {}
        action = "DescribeDistrictSummary"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_edge_summary(self, params=None):
        if params is None:
            params = {}
        action = "DescribeEdgeSummary"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_origin_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeOriginData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_origin_summary(self, params=None):
        if params is None:
            params = {}
        action = "DescribeOriginSummary"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_user_data(self, params=None):
        if params is None:
            params = {}
        action = "DescribeUserData"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_district_ranking(self, params=None):
        if params is None:
            params = {}
        action = "DescribeDistrictRanking"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_edge_ranking(self, params=None):
        if params is None:
            params = {}
        action = "DescribeEdgeRanking"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_origin_ranking(self, params=None):
        if params is None:
            params = {}
        action = "DescribeOriginRanking"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_edge_status_code_ranking(self, params=None):
        if params is None:
            params = {}
        action = "DescribeEdgeStatusCodeRanking"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_origin_status_code_ranking(self, params=None):
        if params is None:
            params = {}
        action = "DescribeOriginStatusCodeRanking"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_statistical_ranking(self, params=None):
        if params is None:
            params = {}
        action = "DescribeStatisticalRanking"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def batch_update_cdn_config(self, params=None):
        if params is None:
            params = {}
        action = "BatchUpdateCdnConfig"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def add_certificate(self, params=None):
        if params is None:
            params = {}
        action = "AddCertificate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def delete_usage_report(self, params=None):
        if params is None:
            params = {}
        action = "DeleteUsageReport"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def create_usage_report(self, params=None):
        if params is None:
            params = {}
        action = "CreateUsageReport"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def list_usage_reports(self, params=None):
        if params is None:
            params = {}
        action = "ListUsageReports"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_shared_config(self, params=None):
        if params is None:
            params = {}
        action = "DescribeSharedConfig"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def list_shared_config(self, params=None):
        if params is None:
            params = {}
        action = "ListSharedConfig"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def delete_shared_config(self, params=None):
        if params is None:
            params = {}
        action = "DeleteSharedConfig"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def update_shared_config(self, params=None):
        if params is None:
            params = {}
        action = "UpdateSharedConfig"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def add_shared_config(self, params=None):
        if params is None:
            params = {}
        action = "AddSharedConfig"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def tag_resources(self, params=None):
        if params is None:
            params = {}
        action = "TagResources"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def untag_resources(self, params=None):
        if params is None:
            params = {}
        action = "UntagResources"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def release_template(self, params=None):
        if params is None:
            params = {}
        action = "ReleaseTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def create_rule_engine_template(self, params=None):
        if params is None:
            params = {}
        action = "CreateRuleEngineTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def update_rule_engine_template(self, params=None):
        if params is None:
            params = {}
        action = "UpdateRuleEngineTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json

    def describe_rule_engine_template(self, params=None):
        if params is None:
            params = {}
        action = "DescribeRuleEngineTemplate"
        res = self.json(action, [], params)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(res)
        return res_json
