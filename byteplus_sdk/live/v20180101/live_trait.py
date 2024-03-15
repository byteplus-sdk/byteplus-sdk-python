# coding:utf-8

import json
from byteplus_sdk.base.Service import Service
from byteplus_sdk.const.Const import *
from byteplus_sdk.util.Util import *
from byteplus_sdk.Policy import *
from byteplus_sdk.live.v20180101.live_config import *  # Modify it if necessary


class LiveTrait(Service):
    def __init__(self, param=None):
        if param is None:
            param = {}
        self.param = param
        region = param.get('region', REGION_CN_NORTH1)
        self.service_info = LiveTrait.get_service_info(region)
        self.api_info = LiveTrait.get_api_info()
        if param.get('ak', None) and param.get('sk', None):
            self.set_ak(param['ak'])
            self.set_sk(param['sk'])
        super(LiveTrait, self).__init__(self.service_info, self.api_info)

    @staticmethod
    def get_service_info(region):
        service_info = service_info_map.get(region, None)
        if not service_info:
            raise Exception('Not support region %s' % region)
        return service_info

    @staticmethod
    def get_api_info():
        return api_info

    def api_get(self, action, params, doseq=0):
        res = self.get(action, params, doseq)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(json.dumps(res))
        return res_json

    def api_post(self, action, params, body):
        res = self.json(action, params, body)
        if res == '':
            raise Exception("%s: empty response" % action)
        res_json = json.loads(json.dumps(res))
        return res_json


    def copy_caster_pvw_to_pgm(self, body):
        res = self.api_post('CopyCasterPVWToPGM', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_caster_image_collection(self, body):
        res = self.api_post('UpdateCasterImageCollection', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_caster_resource(self, body):
        res = self.api_post('GetCasterResource', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def stop_caster(self, body):
        res = self.api_post('StopCaster', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def switch_caster_resource_image(self, body):
        res = self.api_post('SwitchCasterResourceImage', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def switch_caster_layout(self, body):
        res = self.api_post('SwitchCasterLayout', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def switch_caster_resource_oped(self, body):
        res = self.api_post('SwitchCasterResourceOPED', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def switch_caster_resource(self, body):
        res = self.api_post('SwitchCasterResource', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_caster_resource_images(self, body):
        res = self.api_post('CreateCasterResourceImages', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_caster_layout(self, body):
        res = self.api_post('UpdateCasterLayout', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_caster(self, body):
        res = self.api_post('CreateCaster', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_caster_arrange(self, body):
        res = self.api_post('CreateCasterArrange', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_caster_resource_image(self, body):
        res = self.api_post('CreateCasterResourceImage', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_caster_resource(self, body):
        res = self.api_post('CreateCasterResource', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_caster_layout(self, body):
        res = self.api_post('DeleteCasterLayout', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_caster_arrange(self, body):
        res = self.api_post('DeleteCasterArrange', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_caster_resource_image(self, body):
        res = self.api_post('DeleteCasterResourceImage', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_caster_resource_oped(self, body):
        res = self.api_post('DeleteCasterResourceOPED', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def remove_caster_resource(self, body):
        res = self.api_post('RemoveCasterResource', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def start_caster(self, body):
        res = self.api_post('StartCaster', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def start_caster_oped_arrange(self, body):
        res = self.api_post('StartCasterOPEDArrange', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_caster_arrange(self, body):
        res = self.api_post('UpdateCasterArrange', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_caster_config(self, body):
        res = self.api_post('UpdateCasterConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_casters(self, body):
        res = self.api_post('ListCasters', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_caster_resource_oped(self, body):
        res = self.api_post('CreateCasterResourceOPED', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_caster_layout(self, body):
        res = self.api_post('GetCasterLayout', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_caster_arrange(self, body):
        res = self.api_post('GetCasterArrange', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_caster_config(self, body):
        res = self.api_post('GetCasterConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_caster_resource_vod_info(self, body):
        res = self.api_post('GetCasterResourceVodInfo', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json