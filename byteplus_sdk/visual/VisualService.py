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
        service_info = ServiceInfo("cv.byteplusapi.com", {'Accept': 'application/json'},
                                   Credentials('', '', 'cv', 'ap-singapore-1'), 30, 30, "https")
        return service_info

    @staticmethod
    def get_api_info():
        api_info = {
            "ComicPortrait": ApiInfo("POST", "/", {"Action": "ComicPortrait", "Version": "2022-08-24"}, {}, {}),
            "PortraitFusion": ApiInfo("POST", "/", {"Action": "PortraitFusion", "Version": "2022-08-24"}, {}, {}),
            "CVProcess": ApiInfo("POST", "/", {"Action": "CVProcess", "Version": "2024-06-06"}, {}, {}),
            "CVSubmitTask": ApiInfo("POST", "/", {"Action": "CVSubmitTask", "Version": "2024-06-06"}, {}, {}),
            "CVGetResult": ApiInfo("POST", "/", {"Action": "CVGetResult", "Version": "2024-06-06"}, {}, {}),
            "CVSync2AsyncSubmitTask": ApiInfo("POST", "/",{"Action": "CVSync2AsyncSubmitTask", "Version": "2024-06-06"}, {}, {}),
            "CVSync2AsyncGetResult": ApiInfo("POST", "/", {"Action": "CVSync2AsyncGetResult", "Version": "2024-06-06"},{}, {}),
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

    def common_json_handler(self, api, body):
        params = dict()
        try:
            res = self.json(api, params, body)
            res_json = json.loads(res)

            return res_json
        except Exception as e:
            res = str(e)
            try:
                res_json = json.loads(res)
                return res_json
            except:
                raise Exception(str(e))

    def cv_process(self, body):
        try:
            res_json = self.common_json_handler("CVProcess", body)
            return res_json
        except Exception as e:
            raise Exception(str(e))

    def cv_submit_task(self, body):
        try:
            res_json = self.common_json_handler("CVSubmitTask", body)
            return res_json
        except Exception as e:
            raise Exception(str(e))

    def cv_get_result(self, body):
        try:
            res_json = self.common_json_handler("CVGetResult", body)
            return res_json
        except Exception as e:
            raise Exception(str(e))

    def cv_sync2async_submit_task(self, body):
        try:
            res_json = self.common_json_handler("CVSync2AsyncSubmitTask", body)
            return res_json
        except Exception as e:
            raise Exception(str(e))

    def cv_sync2async_get_result(self, body):
        try:
            res_json = self.common_json_handler("CVSync2AsyncGetResult", body)
            return res_json
        except Exception as e:
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
