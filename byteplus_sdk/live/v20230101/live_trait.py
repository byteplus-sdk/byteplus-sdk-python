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
        res = self.api_post('DeleteTranscodePreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_transcode_preset(self, body):
        res = self.api_post('UpdateTranscodePreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_common_trans_preset_detail(self, body):
        res = self.api_post('ListCommonTransPresetDetail', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_trans_code_preset(self, body):
        res = self.api_post('ListVhostTransCodePreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_transcode_preset(self, body):
        res = self.api_post('CreateTranscodePreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_watermark_preset(self, body):
        res = self.api_post('CreateWatermarkPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_watermark_preset(self, body):
        res = self.api_post('UpdateWatermarkPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_watermark_preset(self, body):
        res = self.api_post('DeleteWatermarkPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_watermark_preset(self, body):
        res = self.api_post('ListWatermarkPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_watermark_preset(self, body):
        res = self.api_post('ListVhostWatermarkPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_record_preset(self, body):
        res = self.api_post('DeleteRecordPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_record_preset_v2(self, body):
        res = self.api_post('UpdateRecordPresetV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_record_task_file_history(self, body):
        res = self.api_post('DescribeRecordTaskFileHistory', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_record_preset_v2(self, body):
        res = self.api_post('ListVhostRecordPresetV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_record_preset_v2(self, body):
        res = self.api_post('CreateRecordPresetV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_snapshot_preset(self, body):
        res = self.api_post('DeleteSnapshotPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_snapshot_preset(self, body):
        res = self.api_post('UpdateSnapshotPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cdn_snapshot_history(self, body):
        res = self.api_post('DescribeCDNSnapshotHistory', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_snapshot_preset(self, body):
        res = self.api_post('ListVhostSnapshotPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_snapshot_preset(self, body):
        res = self.api_post('CreateSnapshotPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_time_shift_preset_v2(self, body):
        res = self.api_post('DeleteTimeShiftPresetV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_time_shift_preset_v2(self, body):
        res = self.api_post('CreateTimeShiftPresetV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_time_shift_preset_v2(self, body):
        res = self.api_post('UpdateTimeShiftPresetV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_time_shift_preset_v2(self, body):
        res = self.api_post('ListTimeShiftPresetV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_callback(self, body):
        res = self.api_post('DeleteCallback', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_callback(self, body):
        res = self.api_post('DescribeCallback', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_callback(self, body):
        res = self.api_post('UpdateCallback', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_cert(self, body):
        res = self.api_post('DeleteCert', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cert_detail_secret_v2(self, body):
        res = self.api_post('DescribeCertDetailSecretV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_cert_v2(self, body):
        res = self.api_post('ListCertV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_cert(self, body):
        res = self.api_post('CreateCert', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def bind_cert(self, body):
        res = self.api_post('BindCert', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def unbind_cert(self, body):
        res = self.api_post('UnbindCert', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_domain(self, body):
        res = self.api_post('DeleteDomain', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def enable_domain(self, body):
        res = self.api_post('EnableDomain', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_domain_v2(self, body):
        res = self.api_post('CreateDomainV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_domain_vhost(self, body):
        res = self.api_post('UpdateDomainVhost', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_domain(self, body):
        res = self.api_post('DescribeDomain', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_domain_detail(self, body):
        res = self.api_post('ListDomainDetail', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def disable_domain(self, body):
        res = self.api_post('DisableDomain', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_live_video_quality_analysis_task(self, body):
        res = self.api_post('CreateLiveVideoQualityAnalysisTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_live_video_quality_analysis_task(self, body):
        res = self.api_post('DeleteLiveVideoQualityAnalysisTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_live_video_quality_analysis_task_detail(self, body):
        res = self.api_post('GetLiveVideoQualityAnalysisTaskDetail', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_live_video_quality_analysis_tasks(self, body):
        res = self.api_post('ListLiveVideoQualityAnalysisTasks', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def stop_pull_to_push_task(self, body):
        res = self.api_post('StopPullToPushTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_pull_to_push_task(self, body):
        res = self.api_post('CreatePullToPushTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_pull_to_push_group(self, body):
        res = self.api_post('CreatePullToPushGroup', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_pull_to_push_task(self, body):
        res = self.api_post('DeletePullToPushTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_pull_to_push_group(self, body):
        res = self.api_post('DeletePullToPushGroup', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def restart_pull_to_push_task(self, body):
        res = self.api_post('RestartPullToPushTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_pull_to_push_task(self, body):
        res = self.api_post('UpdatePullToPushTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_pull_to_push_group(self, body):
        res = self.api_post('ListPullToPushGroup', [], body)
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
            
    def list_pull_to_push_task_v2(self, body):
        res = self.api_post('ListPullToPushTaskV2', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_relay_source_rewrite(self, body):
        res = self.api_post('DeleteRelaySourceRewrite', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_relay_source_v3(self, body):
        res = self.api_post('DeleteRelaySourceV3', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_relay_source_rewrite(self, body):
        res = self.api_post('UpdateRelaySourceRewrite', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_relay_source_rewrite(self, body):
        res = self.api_post('DescribeRelaySourceRewrite', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_relay_source_v3(self, body):
        res = self.api_post('DescribeRelaySourceV3', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_relay_source_v3(self, body):
        res = self.api_post('UpdateRelaySourceV3', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def kill_stream(self, body):
        res = self.api_post('KillStream', [], body)
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
        res = self.api_post('ForbidStream', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def resume_stream(self, body):
        res = self.api_post('ResumeStream', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def generate_play_url(self, body):
        res = self.api_post('GeneratePlayURL', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def generate_push_url(self, body):
        res = self.api_post('GeneratePushURL', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_top_play_data(self, body):
        res = self.api_post('DescribeLiveTopPlayData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_region_data(self, body):
        res = self.api_post('DescribeLiveRegionData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_source_stream_metrics(self, body):
        res = self.api_post('DescribeLiveSourceStreamMetrics', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_push_stream_metrics(self, body):
        res = self.api_post('DescribeLivePushStreamMetrics', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_stream_session_data(self, body):
        res = self.api_post('DescribeLiveStreamSessionData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_play_status_code_data(self, body):
        res = self.api_post('DescribeLivePlayStatusCodeData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_batch_push_stream_metrics(self, body):
        res = self.api_post('DescribeLiveBatchPushStreamMetrics', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_push_stream_info_data(self, body):
        res = self.api_post('DescribeLivePushStreamInfoData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_transcode_info_data(self, body):
        res = self.api_post('DescribeLiveTranscodeInfoData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_source_bandwidth_data(self, body):
        res = self.api_post('DescribeLiveSourceBandwidthData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_source_traffic_data(self, body):
        res = self.api_post('DescribeLiveSourceTrafficData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_metric_bandwidth_data(self, body):
        res = self.api_post('DescribeLiveMetricBandwidthData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_metric_traffic_data(self, body):
        res = self.api_post('DescribeLiveMetricTrafficData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_edge_stat_data(self, body):
        res = self.api_post('DescribeLiveEdgeStatData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_isp_data(self, body):
        res = self.api_post('DescribeLiveISPData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_p95_peak_bandwidth_data(self, body):
        res = self.api_post('DescribeLiveP95PeakBandwidthData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_asr_duration_data(self, body):
        res = self.api_post('DescribeLiveASRDurationData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_pull_to_push_bandwidth_data(self, body):
        res = self.api_post('DescribeLivePullToPushBandwidthData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_pull_to_push_data(self, body):
        res = self.api_post('DescribeLivePullToPushData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_bandwidth_data(self, body):
        res = self.api_post('DescribeLiveBandwidthData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_record_data(self, body):
        res = self.api_post('DescribeLiveRecordData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_snapshot_data(self, body):
        res = self.api_post('DescribeLiveSnapshotData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_traffic_data(self, body):
        res = self.api_post('DescribeLiveTrafficData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_transcode_data(self, body):
        res = self.api_post('DescribeLiveTranscodeData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_storage_space_data(self, body):
        res = self.api_post('DescribeLiveStorageSpaceData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_log_data(self, body):
        res = self.api_post('DescribeLiveLogData', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_referer(self, body):
        res = self.api_post('DeleteReferer', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_referer(self, body):
        res = self.api_post('DescribeReferer', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_auth(self, body):
        res = self.api_post('DescribeAuth', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_referer(self, body):
        res = self.api_post('UpdateReferer', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_auth_key(self, body):
        res = self.api_post('UpdateAuthKey', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_hls_config(self, body):
        res = self.api_post('DeleteHLSConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_hls_config(self, body):
        res = self.api_post('UpdateHLSConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_hls_config(self, body):
        res = self.api_post('DescribeHLSConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_http_header_config(self, body):
        res = self.api_post('DeleteHTTPHeaderConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def enable_http_header_config(self, body):
        res = self.api_post('EnableHTTPHeaderConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_http_header_config(self, body):
        res = self.api_post('DescribeHTTPHeaderConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_http_header_config(self, body):
        res = self.api_post('UpdateHTTPHeaderConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_encrypt_drm(self, body):
        res = self.api_post('UpdateEncryptDRM', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_encrypt_hls(self, body):
        res = self.api_post('UpdateEncryptHLS', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_hls_encrypt_data_key(self, query):
        res = self.api_get('GetHLSEncryptDataKey', query)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_encrypt_hls(self, body):
        res = self.api_post('DescribeEncryptHLS', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_license_drm(self, query, body):
        res = self.api_post('DescribeLicenseDRM', query, body)
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
            
    def describe_encrypt_drm(self, body):
        res = self.api_post('DescribeEncryptDRM', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def bind_encrypt_drm(self, body):
        res = self.api_post('BindEncryptDRM', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def un_bind_encrypt_drm(self, body):
        res = self.api_post('UnBindEncryptDRM', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_bind_encrypt_drm(self, body):
        res = self.api_post('ListBindEncryptDRM', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_transcode_preset_batch(self, body):
        res = self.api_post('CreateTranscodePresetBatch', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_transcode_preset_batch(self, body):
        res = self.api_post('DeleteTranscodePresetBatch', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_ip_access_rule(self, body):
        res = self.api_post('DeleteIPAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_region_access_rule(self, body):
        res = self.api_post('DeleteRegionAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_ip_access_rule(self, body):
        res = self.api_post('UpdateIPAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_region_access_rule(self, body):
        res = self.api_post('UpdateRegionAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_ip_access_rule(self, body):
        res = self.api_post('DescribeIPAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_region_access_rule(self, body):
        res = self.api_post('DescribeRegionAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_cmaf_config(self, body):
        res = self.api_post('DeleteCMAFConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_cmaf_config(self, body):
        res = self.api_post('UpdateCMAFConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cmaf_config(self, body):
        res = self.api_post('DescribeCMAFConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_latency_config(self, body):
        res = self.api_post('DeleteLatencyConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_latency_config(self, body):
        res = self.api_post('DescribeLatencyConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_latency_config(self, body):
        res = self.api_post('UpdateLatencyConfig', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_cloud_mix_task(self, body):
        res = self.api_post('CreateCloudMixTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_cloud_mix_task(self, body):
        res = self.api_post('UpdateCloudMixTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def get_cloud_mix_task_detail(self, body):
        res = self.api_post('GetCloudMixTaskDetail', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_cloud_mix_task(self, body):
        res = self.api_post('ListCloudMixTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_cloud_mix_task(self, body):
        res = self.api_post('DeleteCloudMixTask', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_cluster_rate_limit(self, body):
        res = self.api_post('DeleteClusterRateLimit', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_cluster_rate_limit(self, body):
        res = self.api_post('DescribeClusterRateLimit', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_cluster_rate_limit(self, body):
        res = self.api_post('UpdateClusterRateLimit', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_user_agent_access_rule(self, body):
        res = self.api_post('DeleteUserAgentAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_user_agent_access_rule(self, body):
        res = self.api_post('DescribeUserAgentAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_user_agent_access_rule(self, body):
        res = self.api_post('UpdateUserAgentAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_format_access_rule(self, body):
        res = self.api_post('DeleteFormatAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_format_access_rule(self, body):
        res = self.api_post('DescribeFormatAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_format_access_rule(self, body):
        res = self.api_post('UpdateFormatAccessRule', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_subtitle_transcode_preset(self, body):
        res = self.api_post('DeleteSubtitleTranscodePreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_subtitle_transcode_preset(self, body):
        res = self.api_post('UpdateSubtitleTranscodePreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def list_vhost_subtitle_transcode_preset(self, body):
        res = self.api_post('ListVhostSubtitleTranscodePreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_subtitle_transcode_preset(self, body):
        res = self.api_post('CreateSubtitleTranscodePreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def create_live_pad_preset(self, body):
        res = self.api_post('CreateLivePadPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def delete_live_pad_preset(self, body):
        res = self.api_post('DeleteLivePadPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def stop_live_pad_stream(self, body):
        res = self.api_post('StopLivePadStream', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def update_live_pad_preset(self, body):
        res = self.api_post('UpdateLivePadPreset', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_pad_stream_list(self, body):
        res = self.api_post('DescribeLivePadStreamList', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json
            
    def describe_live_pad_preset_detail(self, body):
        res = self.api_post('DescribeLivePadPresetDetail', [], body)
        if res == '':
            raise Exception("empty response")
        res_json = json.loads(res)
        return res_json