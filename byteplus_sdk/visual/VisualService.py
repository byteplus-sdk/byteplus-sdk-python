# coding:utf-8
import json
import threading

from byteplus_sdk.ApiInfo import ApiInfo
from byteplus_sdk.Credentials import Credentials
from byteplus_sdk.base.Service import Service
from byteplus_sdk.ServiceInfo import ServiceInfo


class VisualService(Service):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(VisualService, "_instance"):
            with VisualService._instance_lock:
                if not hasattr(VisualService, "_instance"):
                    VisualService._instance = object.__new__(cls)
        return VisualService._instance

    def __init__(self):
        self.service_info = VisualService.get_service_info()
        self.api_info = VisualService.get_api_info()
        super(VisualService, self).__init__(self.service_info, self.api_info)

    @staticmethod
    def get_service_info():
        service_info = ServiceInfo("open.byteplusapi.com", {'Accept': 'application/json'},
                                   Credentials('', '', 'cv', 'ap-singapore-1'), 10, 30)
        return service_info

    @staticmethod
    def get_api_info():
        api_info = {
            "ComicPortrait": ApiInfo("POST", "/", {"Action": "ComicPortrait", "Version": "2022-08-24"}, {}, {}),
            "PortraitFusion": ApiInfo("POST", "/", {"Action": "PortraitFusion", "Version": "2022-08-24"}, {}, {}),
        }
        return api_info

    def common_handler(self, api, form):
        params = dict()
        try:
            res = self.post(api, params, form)
            res_json = json.loads(res)
            return res_json
        except Exception as e:
            res = str(e)
            try:
                res_json = json.loads(res)
                return res_json
            except:
                raise Exception(str(e))

    def common_get_handler(self, api, params):
        try:
            res = self.get(api, params)
            res_json = json.loads(res)
            return res_json
        except Exception as e:
            res = str(e)
            try:
                res_json = json.loads(res)
                return res_json
            except:
                raise Exception(str(e))

    def comic_portrait(self, form):
        try:
            res_json = self.common_handler("ComicPortrait", form)
            return res_json
        except Exception as e:
            raise Exception(str(e))

    def portrait_fusion(self, form):
        try:
            res_json = self.common_handler("PortraitFusion", form)
            return res_json
        except Exception as e:
            raise Exception(str(e))
