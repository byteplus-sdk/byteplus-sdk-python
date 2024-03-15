# coding:utf-8

import json
from byteplus_sdk.base.Service import Service
from byteplus_sdk.const.Const import *
from byteplus_sdk.util.Util import *
from byteplus_sdk.Policy import *
from byteplus_sdk.live.v20230101.live_config import *  # Modify it if necessary


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


    def delete_transcode_preset(self, body):
        res = self.api_post('DeleteTranscodePreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_common_trans_preset(self, body):
        res = self.api_post('DeleteCommonTransPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_transcode_preset_patch_by_admin(self, body):
        res = self.api_post('DeleteTranscodePresetPatchByAdmin', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def add_common_trans_preset(self, body):
        res = self.api_post('AddCommonTransPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_transcode_preset(self, body):
        res = self.api_post('UpdateTranscodePreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_common_trans_preset_detail(self, body):
        res = self.api_post('ListCommonTransPresetDetail', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_transcode_preset_detail(self, body):
        res = self.api_post('DescribeTranscodePresetDetail', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_trans_code_preset(self, body):
        res = self.api_post('ListVhostTransCodePreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_transcode_preset(self, body):
        res = self.api_post('CreateTranscodePreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_transcode_preset_patch_by_admin(self, body):
        res = self.api_post('CreateTranscodePresetPatchByAdmin', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_watermark_preset_v2(self, body):
        res = self.api_post('DeleteWatermarkPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_watermark_preset_v2(self, body):
        res = self.api_post('UpdateWatermarkPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_watermark_preset_detail(self, body):
        res = self.api_post('DescribeWatermarkPresetDetail', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_watermark_preset(self, body):
        res = self.api_post('CreateWatermarkPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_watermark_preset_v2(self, body):
        res = self.api_post('CreateWatermarkPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_watermark_preset(self, body):
        res = self.api_post('UpdateWatermarkPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_watermark_preset(self, body):
        res = self.api_post('DeleteWatermarkPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_watermark_preset(self, body):
        res = self.api_post('ListWatermarkPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_watermark_preset(self, body):
        res = self.api_post('ListVhostWatermarkPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def stop_pull_record_task(self, body):
        res = self.api_post('StopPullRecordTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_pull_record_task(self, body):
        res = self.api_post('CreatePullRecordTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_record_history(self, body):
        res = self.api_post('DeleteRecordHistory', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_record_preset(self, body):
        res = self.api_post('DeleteRecordPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_record_preset_v2(self, body):
        res = self.api_post('UpdateRecordPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_record_task_file_history(self, body):
        res = self.api_post('DescribeRecordTaskFileHistory', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_record_preset_v2(self, body):
        res = self.api_post('ListVhostRecordPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_pull_record_task(self, body):
        res = self.api_post('ListPullRecordTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_record_preset_v2(self, body):
        res = self.api_post('CreateRecordPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_video_classifications(self, body):
        res = self.api_post('ListVideoClassifications', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_snapshot_preset(self, body):
        res = self.api_post('DeleteSnapshotPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_snapshot_preset(self, body):
        res = self.api_post('UpdateSnapshotPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_snapshot_preset_v2(self, body):
        res = self.api_post('UpdateSnapshotPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cdn_snapshot_history(self, body):
        res = self.api_post('DescribeCDNSnapshotHistory', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_snapshot_preset(self, body):
        res = self.api_post('ListVhostSnapshotPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_snapshot_preset_v2(self, body):
        res = self.api_post('ListVhostSnapshotPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_snapshot_preset(self, body):
        res = self.api_post('CreateSnapshotPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_snapshot_preset_v2(self, body):
        res = self.api_post('CreateSnapshotPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_time_shift_preset_v2(self, body):
        res = self.api_post('DeleteTimeShiftPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_time_shift_preset_v3(self, body):
        res = self.api_post('DeleteTimeShiftPresetV3', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_time_shift_preset_v2(self, body):
        res = self.api_post('CreateTimeShiftPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_time_shift_preset_v2(self, body):
        res = self.api_post('UpdateTimeShiftPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_time_shift_preset_v3(self, body):
        res = self.api_post('UpdateTimeShiftPresetV3', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_time_shift_preset_detail(self, body):
        res = self.api_post('DescribeTimeShiftPresetDetail', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_time_shift_preset_v2(self, body):
        res = self.api_post('ListTimeShiftPresetV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_time_shift_preset_v3(self, body):
        res = self.api_post('CreateTimeShiftPresetV3', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def generate_time_shift_play_url(self, body):
        res = self.api_post('GenerateTimeShiftPlayURL', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_domain_detail_by_user_id(self, body):
        res = self.api_post('ListVhostDomainDetailByUserID', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_vhost_tags(self, body):
        res = self.api_post('UpdateVhostTags', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_detail(self, body):
        res = self.api_post('ListVhostDetail', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_detail_by_admin(self, body):
        res = self.api_post('ListVhostDetailByAdmin', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_vhost(self, body):
        res = self.api_post('DescribeVhost', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_tags(self):
        res = self.api_get('GetTags', {})
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_projects(self, body):
        res = self.api_post('ListProjects', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_callback(self, body):
        res = self.api_post('DeleteCallback', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_callback(self, body):
        res = self.api_post('DescribeCallback', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_callback(self, body):
        res = self.api_post('UpdateCallback', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_auth(self, body):
        res = self.api_post('DeleteAuth', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def enable_auth(self, body):
        res = self.api_post('EnableAuth', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_auth(self, body):
        res = self.api_post('DescribeAuth', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def disable_auth(self, body):
        res = self.api_post('DisableAuth', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_cert(self, body):
        res = self.api_post('DeleteCert', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_cert(self, body):
        res = self.api_post('UpdateCert', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cert_detail_secret_v2(self, body):
        res = self.api_post('DescribeCertDetailSecretV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_cert_v2(self, body):
        res = self.api_post('ListCertV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cert_detail_v2(self, body):
        res = self.api_post('DescribeCertDetailV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_cert(self, body):
        res = self.api_post('CreateCert', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def bind_cert(self, body):
        res = self.api_post('BindCert', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def unbind_cert(self, body):
        res = self.api_post('UnbindCert', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_object(self, body):
        res = self.api_post('ListObject', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def manager_pull_push_domain_bind(self, body):
        res = self.api_post('ManagerPullPushDomainBind', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cert_detail_secret(self, body):
        res = self.api_post('DescribeCertDetailSecret', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_domain_verify(self, body):
        res = self.api_post('DescribeDomainVerify', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_verify_content(self, body):
        res = self.api_post('CreateVerifyContent', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vqos_dimension_values(self, query, body):
        res = self.api_post('ListVqosDimensionValues', query, json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_cert(self, body):
        res = self.api_post('ListCert', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_cert_bind_info(self, body):
        res = self.api_post('ListCertBindInfo', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_free_time_interval(self, body):
        res = self.api_post('DescribeLiveFreeTimeInterval', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def verify_domain_owner(self, body):
        res = self.api_post('VerifyDomainOwner', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def validate_cert(self, body):
        res = self.api_post('ValidateCert', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_domain(self, body):
        res = self.api_post('DeleteDomain', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_domain_v2(self, body):
        res = self.api_post('DeleteDomainV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def enable_domain(self, body):
        res = self.api_post('EnableDomain', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_domain_v2(self, body):
        res = self.api_post('CreateDomainV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def reject_domain(self, body):
        res = self.api_post('RejectDomain', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_domain_vhost(self, body):
        res = self.api_post('UpdateDomainVhost', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_domain(self, body):
        res = self.api_post('UpdateDomain', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_domain(self, body):
        res = self.api_post('DescribeDomain', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_domain_detail(self, body):
        res = self.api_post('ListDomainDetail', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_domain(self, body):
        res = self.api_post('CreateDomain', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def disable_domain(self, body):
        res = self.api_post('DisableDomain', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_vq_score_task(self, body):
        res = self.api_post('CreateVQScoreTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_vq_score_task(self, body):
        res = self.api_post('DescribeVQScoreTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vq_score_task(self, body):
        res = self.api_post('ListVQScoreTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def stop_pull_to_push_task(self, body):
        res = self.api_post('StopPullToPushTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_pull_to_push_task(self, body):
        res = self.api_post('CreatePullToPushTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_pull_to_push_task(self, body):
        res = self.api_post('DeletePullToPushTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def restart_pull_to_push_task(self, body):
        res = self.api_post('RestartPullToPushTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_pull_to_push_task(self, body):
        res = self.api_post('UpdatePullToPushTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_pull_to_push_task(self, query):
        res = self.api_get('ListPullToPushTask', query)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_deny_config_v2(self, body):
        res = self.api_post('DeleteDenyConfigV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_deny_config_v2(self, body):
        res = self.api_post('DescribeDenyConfigV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_relay_source_rewrite(self, body):
        res = self.api_post('DeleteRelaySourceRewrite', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_relay_source_v4(self, body):
        res = self.api_post('DeleteRelaySourceV4', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_relay_source_v3(self, body):
        res = self.api_post('DeleteRelaySourceV3', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_relay_source_rewrite(self, body):
        res = self.api_post('UpdateRelaySourceRewrite', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_relay_source_v4(self, body):
        res = self.api_post('UpdateRelaySourceV4', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_relay_source_rewrite(self, body):
        res = self.api_post('DescribeRelaySourceRewrite', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_relay_source_v4(self, body):
        res = self.api_post('ListRelaySourceV4', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_relay_source_v3(self, body):
        res = self.api_post('DescribeRelaySourceV3', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_relay_source_v4(self, body):
        res = self.api_post('CreateRelaySourceV4', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_relay_source_v3(self, body):
        res = self.api_post('UpdateRelaySourceV3', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def kill_stream(self, body):
        res = self.api_post('KillStream', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_closed_stream_info_by_page(self, query):
        res = self.api_get('DescribeClosedStreamInfoByPage', query)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_stream_info_by_page(self, query):
        res = self.api_get('DescribeLiveStreamInfoByPage', query)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_stream_state(self, query):
        res = self.api_get('DescribeLiveStreamState', query)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_forbidden_stream_info_by_page(self, query):
        res = self.api_get('DescribeForbiddenStreamInfoByPage', query)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def forbid_stream(self, body):
        res = self.api_post('ForbidStream', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def resume_stream(self, body):
        res = self.api_post('ResumeStream', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def generate_play_url(self, body):
        res = self.api_post('GeneratePlayURL', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def generate_push_url(self, body):
        res = self.api_post('GeneratePushURL', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_sdk_license(self, body):
        res = self.api_post('UpdateSDKLicense', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_app(self, body):
        res = self.api_post('CreateApp', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_sdk(self, body):
        res = self.api_post('DeleteSDK', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_app(self, body):
        res = self.api_post('UpdateApp', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_sdk(self, body):
        res = self.api_post('UpdateSDK', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_sdk_detail(self, body):
        res = self.api_post('DescribeSDKDetail', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_sdk_params_available(self, body):
        res = self.api_post('DescribeSDKParamsAvailable', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_app_id_params_available(self, body):
        res = self.api_post('DescribeAppIDParamsAvailable', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_sdk(self, body):
        res = self.api_post('CreateSDK', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_sdk(self, body):
        res = self.api_post('ListSDK', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_sdk_admin(self, body):
        res = self.api_post('ListSDKAdmin', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_apps(self):
        res = self.api_get('GetApps', {})
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_service(self, body):
        res = self.api_post('UpdateService', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_services(self, body):
        res = self.api_post('ListServices', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_service(self, body):
        res = self.api_post('DescribeService', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_activity_billing(self, body):
        res = self.api_post('UpdateActivityBilling', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_billing(self, body):
        res = self.api_post('UpdateBilling', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_instance(self, body):
        res = self.api_post('ListInstance', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_billing_for_admin(self, body):
        res = self.api_post('DescribeBillingForAdmin', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_billing(self, body):
        res = self.api_post('DescribeBilling', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_billing_month_available(self, body):
        res = self.api_post('DescribeBillingMonthAvailable', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_resource_package(self, body):
        res = self.api_post('ListResourcePackage', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def terminate_instance(self, body):
        res = self.api_post('TerminateInstance', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_stream_quota_config(self, body):
        res = self.api_post('DeleteStreamQuotaConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_stream_quota_config_patch(self, body):
        res = self.api_post('UpdateStreamQuotaConfigPatch', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_stream_quota_config(self, body):
        res = self.api_post('DescribeStreamQuotaConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_stream_quota_config(self, body):
        res = self.api_post('UpdateStreamQuotaConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vqos_metrics_dimensions(self, query):
        res = self.api_get('ListVqosMetricsDimensions', query)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_vqos_raw_data(self, query, body):
        res = self.api_post('GetVqosRawData', query, json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def stop_pull_cdn_snapshot_task(self, body):
        res = self.api_post('StopPullCDNSnapshotTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_pull_cdn_snapshot_task(self, body):
        res = self.api_post('CreatePullCDNSnapshotTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_pull_cdn_snapshot_task(self, body):
        res = self.api_post('GetPullCDNSnapshotTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_pull_cdn_snapshot_task(self, body):
        res = self.api_post('ListPullCDNSnapshotTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_pull_record_task(self, body):
        res = self.api_post('GetPullRecordTask', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_snapshot_audit_preset(self, body):
        res = self.api_post('DeleteSnapshotAuditPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_snapshot_audit_preset(self, body):
        res = self.api_post('UpdateSnapshotAuditPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_snapshot_audit_preset_detail(self, body):
        res = self.api_post('DescribeSnapshotAuditPresetDetail', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_snapshot_audit_preset(self, body):
        res = self.api_post('ListVhostSnapshotAuditPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_snapshot_audit_preset(self, body):
        res = self.api_post('CreateSnapshotAuditPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_ip_info(self, body):
        res = self.api_post('DescribeIpInfo', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_region_data(self, body):
        res = self.api_post('DescribeLiveRegionData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_source_stream_metrics(self, body):
        res = self.api_post('DescribeLiveSourceStreamMetrics', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_push_stream_metrics(self, body):
        res = self.api_post('DescribeLivePushStreamMetrics', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_play_status_code_data(self, body):
        res = self.api_post('DescribeLivePlayStatusCodeData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_batch_source_stream_metrics(self, body):
        res = self.api_post('DescribeLiveBatchSourceStreamMetrics', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_batch_source_stream_avg_metrics(self, body):
        res = self.api_post('DescribeLiveBatchSourceStreamAvgMetrics', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_batch_online_stream_metrics(self, body):
        res = self.api_post('DescribeLiveBatchOnlineStreamMetrics', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_batch_push_stream_metrics(self, body):
        res = self.api_post('DescribeLiveBatchPushStreamMetrics', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_batch_push_stream_avg_metrics(self, body):
        res = self.api_post('DescribeLiveBatchPushStreamAvgMetrics', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_batch_stream_transcode_data(self, body):
        res = self.api_post('DescribeLiveBatchStreamTranscodeData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_stream_count_data(self, body):
        res = self.api_post('DescribeLiveStreamCountData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_push_stream_count_data(self, body):
        res = self.api_post('DescribeLivePushStreamCountData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_source_bandwidth_data(self, body):
        res = self.api_post('DescribeLiveSourceBandwidthData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_source_traffic_data(self, body):
        res = self.api_post('DescribeLiveSourceTrafficData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_metric_bandwidth_data(self, body):
        res = self.api_post('DescribeLiveMetricBandwidthData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_metric_traffic_data(self, body):
        res = self.api_post('DescribeLiveMetricTrafficData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_batch_stream_traffic_data(self, body):
        res = self.api_post('DescribeLiveBatchStreamTrafficData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_stream_session_data(self, body):
        res = self.api_post('DescribeLiveStreamSessionData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_isp_data(self, body):
        res = self.api_post('DescribeLiveISPData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_p95_peak_bandwidth_data(self, body):
        res = self.api_post('DescribeLiveP95PeakBandwidthData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_audit_data(self, body):
        res = self.api_post('DescribeLiveAuditData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_pull_to_push_bandwidth_data(self, body):
        res = self.api_post('DescribeLivePullToPushBandwidthData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_pull_to_push_data(self, body):
        res = self.api_post('DescribeLivePullToPushData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_bandwidth_data(self, body):
        res = self.api_post('DescribeLiveBandwidthData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_record_data(self, body):
        res = self.api_post('DescribeLiveRecordData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_snapshot_data(self, body):
        res = self.api_post('DescribeLiveSnapshotData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_traffic_data(self, body):
        res = self.api_post('DescribeLiveTrafficData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_transcode_data(self, body):
        res = self.api_post('DescribeLiveTranscodeData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_time_shift_data(self, body):
        res = self.api_post('DescribeLiveTimeShiftData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_action_history(self, body):
        res = self.api_post('DescribeActionHistory', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_action_history(self, body):
        res = self.api_post('ListActionHistory', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_dense_snapshot_preset(self, body):
        res = self.api_post('DeleteDenseSnapshotPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_dense_snapshot_preset(self, body):
        res = self.api_post('UpdateDenseSnapshotPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_dense_snapshot_preset(self, body):
        res = self.api_post('ListVhostDenseSnapshotPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def desc_dense_snapshot_preset_detail(self, body):
        res = self.api_post('DescDenseSnapshotPresetDetail', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_dense_snapshot_preset(self, body):
        res = self.api_post('CreateDenseSnapshotPreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_customized_log_data(self, body):
        res = self.api_post('DescribeLiveCustomizedLogData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_log_data(self, body):
        res = self.api_post('DescribeLiveLogData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def associate_preset(self, body):
        res = self.api_post('AssociatePreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def dis_associate_preset(self, body):
        res = self.api_post('DisAssociatePreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_preset_association(self, body):
        res = self.api_post('UpdatePresetAssociation', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_preset_association(self, body):
        res = self.api_post('DescribePresetAssociation', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_ticket(self, body):
        res = self.api_post('CreateTicket', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_referer(self, body):
        res = self.api_post('DeleteReferer', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_deny_config(self, body):
        res = self.api_post('DescribeDenyConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_referer(self, body):
        res = self.api_post('DescribeReferer', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_deny_config(self, body):
        res = self.api_post('UpdateDenyConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_deny_config_v2(self, body):
        res = self.api_post('UpdateDenyConfigV2', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_referer(self, body):
        res = self.api_post('UpdateReferer', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_auth_key(self, body):
        res = self.api_post('UpdateAuthKey', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_relay_sink(self, body):
        res = self.api_post('DeleteRelaySink', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_relay_sink(self, body):
        res = self.api_post('UpdateRelaySink', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_relay_sink(self, body):
        res = self.api_post('DescribeRelaySink', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_hls_config(self, body):
        res = self.api_post('DeleteHLSConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_hls_config(self, body):
        res = self.api_post('UpdateHLSConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_hls_config(self, body):
        res = self.api_post('DescribeHLSConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_http_header_config(self, body):
        res = self.api_post('DeleteHTTPHeaderConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_header_config(self, body):
        res = self.api_post('DeleteHeaderConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def enable_http_header_config(self, body):
        res = self.api_post('EnableHTTPHeaderConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_http_header_config(self, body):
        res = self.api_post('UpdateHTTPHeaderConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_header_config(self, body):
        res = self.api_post('UpdateHeaderConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_http_header_config(self, body):
        res = self.api_post('DescribeHTTPHeaderConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_header_config(self, body):
        res = self.api_post('DescribeHeaderConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_header_enum(self, body):
        res = self.api_post('ListHeaderEnum', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_nss_rewrite_config(self, body):
        res = self.api_post('DeleteNSSRewriteConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_nss_rewrite_config(self, body):
        res = self.api_post('UpdateNSSRewriteConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_nss_rewrite_config(self, body):
        res = self.api_post('DescribeNSSRewriteConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_activity_bandwidth_data(self, body):
        res = self.api_post('DescribeLiveActivityBandwidthData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_live_account_fee_config(self, body):
        res = self.api_post('CreateLiveAccountFeeConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_live_account_fee_config(self, body):
        res = self.api_post('DeleteLiveAccountFeeConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_account_fee_config(self, body):
        res = self.api_post('DescribeLiveAccountFeeConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_stream_usage_data(self, body):
        res = self.api_post('DescribeLiveStreamUsageData', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_fee_config(self, body):
        res = self.api_post('DescribeLiveFeeConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_account_fee_type(self, body):
        res = self.api_post('DescribeLiveAccountFeeType', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_encrypt_drm(self, body):
        res = self.api_post('UpdateEncryptDRM', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_content_key(self, body):
        res = self.api_post('DescribeContentKey', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cert_drm(self, query):
        res = self.api_get('DescribeCertDRM', query)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_license_drm(self, query, body):
        res = self.api_post('DescribeLicenseDRM', query, json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_encrypt_drm(self, body):
        res = self.api_post('DescribeEncryptDRM', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def bind_encrypt_drm(self, body):
        res = self.api_post('BindEncryptDRM', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def un_bind_encrypt_drm(self, body):
        res = self.api_post('UnBindEncryptDRM', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_bind_encrypt_drm(self, body):
        res = self.api_post('ListBindEncryptDRM', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_custom_log_config(self, body):
        res = self.api_post('CreateCustomLogConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_custom_log_config(self, body):
        res = self.api_post('DeleteCustomLogConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_custom_log_config(self, body):
        res = self.api_post('DescribeCustomLogConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def check_custom_log_config(self, body):
        res = self.api_post('CheckCustomLogConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_transcode_preset_batch(self, body):
        res = self.api_post('CreateTranscodePresetBatch', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_transcode_preset_batch(self, body):
        res = self.api_post('DeleteTranscodePresetBatch', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def associate_ref_config(self, body):
        res = self.api_post('AssociateRefConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def disassociate_ref_config(self, body):
        res = self.api_post('DisassociateRefConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_ref_config(self, body):
        res = self.api_post('DescribeRefConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_reference_names(self, body):
        res = self.api_post('ListReferenceNames', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_reference_types(self):
        res = self.api_get('ListReferenceTypes', {})
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_reference_info(self, body):
        res = self.api_post('ListReferenceInfo', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_av_slice_preset(self, body):
        res = self.api_post('CreateAvSlicePreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_av_slice_preset(self, body):
        res = self.api_post('DeleteAvSlicePreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_av_slice_preset(self, body):
        res = self.api_post('UpdateAvSlicePreset', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_ip_access_rule(self, body):
        res = self.api_post('DeleteIPAccessRule', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_ip_access_rule(self, body):
        res = self.api_post('UpdateIPAccessRule', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_ip_access_rule(self, body):
        res = self.api_post('DescribeIPAccessRule', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_proxy_config(self, body):
        res = self.api_post('CreateProxyConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_proxy_config_association(self, body):
        res = self.api_post('DeleteProxyConfigAssociation', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_proxy_config(self, body):
        res = self.api_post('DeleteProxyConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_proxy_config_association(self, body):
        res = self.api_post('UpdateProxyConfigAssociation', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_proxy_config(self, body):
        res = self.api_post('UpdateProxyConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_proxy_config_association(self, body):
        res = self.api_post('DescribeProxyConfigAssociation', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_proxy_config(self, body):
        res = self.api_post('ListProxyConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_cmaf_config(self, body):
        res = self.api_post('DeleteCMAFConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_cmaf_config(self, body):
        res = self.api_post('UpdateCMAFConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cmaf_config(self, body):
        res = self.api_post('DescribeCMAFConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_latency_config(self, body):
        res = self.api_post('DeleteLatencyConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_latency_config(self, body):
        res = self.api_post('UpdateLatencyConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_latency_config(self, body):
        res = self.api_post('DescribeLatencyConfig', [], json.dumps(body))
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json