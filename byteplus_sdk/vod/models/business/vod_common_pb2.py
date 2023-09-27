# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: byteplus/vod/business/vod_common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&byteplus/vod/business/vod_common.proto\x12\x1c\x42yteplus.Vod.Models.Business\"\xdc\x03\n\rVodSourceInfo\x12\x0e\n\x06\x46ileId\x18\x01 \x01(\t\x12\x0b\n\x03Md5\x18\x02 \x01(\t\x12\x10\n\x08\x46ileType\x18\x03 \x01(\t\x12\r\n\x05\x43odec\x18\x04 \x01(\t\x12\x0e\n\x06Height\x18\x05 \x01(\x05\x12\r\n\x05Width\x18\x06 \x01(\x05\x12\x0e\n\x06\x46ormat\x18\x07 \x01(\t\x12\x10\n\x08\x44uration\x18\x08 \x01(\x02\x12\x0c\n\x04Size\x18\t \x01(\x01\x12\x10\n\x08StoreUri\x18\n \x01(\t\x12\x12\n\nDefinition\x18\x0b \x01(\t\x12\x0f\n\x07\x42itrate\x18\x0c \x01(\x05\x12\x0b\n\x03\x46ps\x18\r \x01(\x02\x12\x12\n\nCreateTime\x18\x0e \x01(\t\x12\x0f\n\x07Quality\x18\x0f \x01(\t\x12\x14\n\x0c\x44ynamicRange\x18\x10 \x01(\t\x12I\n\x0fVideoStreamMeta\x18\x11 \x01(\x0b\x32\x30.Byteplus.Vod.Models.Business.VodVideoStreamMeta\x12I\n\x0f\x41udioStreamMeta\x18\x12 \x01(\x0b\x32\x30.Byteplus.Vod.Models.Business.VodAudioStreamMeta\x12\x17\n\x0fTosStorageClass\x18\x13 \x01(\t\x12\x10\n\x08\x46ileName\x18\x14 \x01(\t\"k\n\x12VodAudioStreamMeta\x12\r\n\x05\x43odec\x18\x01 \x01(\t\x12\x10\n\x08\x44uration\x18\x02 \x01(\x02\x12\x12\n\nSampleRate\x18\x03 \x01(\x05\x12\x0f\n\x07\x42itrate\x18\x04 \x01(\x05\x12\x0f\n\x07Quality\x18\x05 \x01(\t\"\x86\x01\n\x12VodVideoStreamMeta\x12\r\n\x05\x43odec\x18\x01 \x01(\t\x12\x0e\n\x06Height\x18\x02 \x01(\x05\x12\r\n\x05Width\x18\x03 \x01(\x05\x12\x10\n\x08\x44uration\x18\x04 \x01(\x02\x12\x12\n\nDefinition\x18\x05 \x01(\t\x12\x0f\n\x07\x42itrate\x18\x06 \x01(\x05\x12\x0b\n\x03\x46ps\x18\x07 \x01(\x02\"\xff\x02\n\x10VodTranscodeInfo\x12\x0e\n\x06\x46ileId\x18\x01 \x01(\t\x12\x0b\n\x03Md5\x18\x02 \x01(\t\x12\x10\n\x08\x46ileType\x18\x03 \x01(\t\x12\x10\n\x08LogoType\x18\x04 \x01(\t\x12\x0f\n\x07\x45ncrypt\x18\x05 \x01(\x08\x12\x0e\n\x06\x46ormat\x18\x06 \x01(\t\x12\x10\n\x08\x44uration\x18\x07 \x01(\x02\x12\x0c\n\x04Size\x18\x08 \x01(\x01\x12\x10\n\x08StoreUri\x18\t \x01(\t\x12I\n\x0fVideoStreamMeta\x18\n \x01(\x0b\x32\x30.Byteplus.Vod.Models.Business.VodVideoStreamMeta\x12I\n\x0f\x41udioStreamMeta\x18\x0b \x01(\x0b\x32\x30.Byteplus.Vod.Models.Business.VodAudioStreamMeta\x12\x12\n\nCreateTime\x18\x0c \x01(\t\x12\x14\n\x0c\x44ynamicRange\x18\r \x01(\t\x12\x17\n\x0fTosStorageClass\x18\x0e \x01(\t\"S\n\x0fVodAdaptiveInfo\x12\x13\n\x0bMainPlayUrl\x18\x01 \x01(\t\x12\x15\n\rBackupPlayUrl\x18\x02 \x01(\t\x12\x14\n\x0c\x41\x64\x61ptiveType\x18\x03 \x01(\t\"\xe1\x03\n\x0bVodPlayInfo\x12\x0e\n\x06\x46ileId\x18\x01 \x01(\t\x12\x0b\n\x03Md5\x18\x02 \x01(\t\x12\x10\n\x08\x46ileType\x18\x03 \x01(\t\x12\x0e\n\x06\x46ormat\x18\x04 \x01(\t\x12\r\n\x05\x43odec\x18\x05 \x01(\t\x12\x12\n\nDefinition\x18\x06 \x01(\t\x12\x13\n\x0bMainPlayUrl\x18\x07 \x01(\t\x12\x15\n\rBackupPlayUrl\x18\x08 \x01(\t\x12\x0f\n\x07\x42itrate\x18\t \x01(\x05\x12\r\n\x05Width\x18\n \x01(\x05\x12\x0e\n\x06Height\x18\x0b \x01(\x05\x12\x0c\n\x04Size\x18\x0c \x01(\x01\x12\x11\n\tCheckInfo\x18\r \x01(\t\x12\x12\n\nIndexRange\x18\x0e \x01(\t\x12\x11\n\tInitRange\x18\x0f \x01(\t\x12\x10\n\x08PlayAuth\x18\x10 \x01(\t\x12\x12\n\nPlayAuthId\x18\x11 \x01(\t\x12\x10\n\x08LogoType\x18\x12 \x01(\t\x12\x0f\n\x07Quality\x18\x13 \x01(\t\x12\x19\n\x11\x42\x61rrageMaskOffset\x18\x14 \x01(\t\x12\x10\n\x08\x44uration\x18\x15 \x01(\x02\x12\x19\n\x11KeyFrameAlignment\x18\x16 \x01(\t\x12;\n\x06Volume\x18\x17 \x01(\x0b\x32+.Byteplus.Vod.Models.Business.VodVolumeInfo\"/\n\rVodVolumeInfo\x12\x10\n\x08Loudness\x18\x01 \x01(\x01\x12\x0c\n\x04Peak\x18\x02 \x01(\x01\"\xa3\x01\n\x0f\x42\x61rrageMaskInfo\x12\x0f\n\x07Version\x18\x01 \x01(\t\x12\x16\n\x0e\x42\x61rrageMaskUrl\x18\x02 \x01(\t\x12\x0e\n\x06\x46ileId\x18\x03 \x01(\t\x12\x10\n\x08\x46ileSize\x18\x04 \x01(\x01\x12\x10\n\x08\x46ileHash\x18\x05 \x01(\t\x12\x11\n\tUpdatedAt\x18\x06 \x01(\t\x12\x0f\n\x07\x42itrate\x18\x07 \x01(\x05\x12\x0f\n\x07HeadLen\x18\x08 \x01(\x01\"\xa0\x01\n\x0cVodThumbInfo\x12\x12\n\nCaptureNum\x18\x01 \x01(\x05\x12\x11\n\tStoreUrls\x18\x02 \x03(\t\x12\x11\n\tCellWidth\x18\x03 \x01(\x05\x12\x12\n\nCellHeight\x18\x04 \x01(\x05\x12\x0f\n\x07ImgXLen\x18\x05 \x01(\x05\x12\x0f\n\x07ImgYLen\x18\x06 \x01(\x05\x12\x10\n\x08Interval\x18\x07 \x01(\x01\x12\x0e\n\x06\x46ormat\x18\x08 \x01(\t\"\x80\x02\n\x0fVodSubtitleInfo\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0e\n\x06\x46ileId\x18\x02 \x01(\t\x12\x10\n\x08Language\x18\x03 \x01(\t\x12\x12\n\nLanguageId\x18\x04 \x01(\x05\x12\x0e\n\x06\x46ormat\x18\x05 \x01(\t\x12\x12\n\nSubtitleId\x18\x06 \x01(\t\x12\r\n\x05Title\x18\x07 \x01(\t\x12\x0b\n\x03Tag\x18\x08 \x01(\t\x12\x0e\n\x06Status\x18\t \x01(\t\x12\x0e\n\x06Source\x18\n \x01(\t\x12\x10\n\x08StoreUri\x18\x0b \x01(\t\x12\x13\n\x0bSubtitleUrl\x18\x0c \x01(\t\x12\x12\n\nCreateTime\x18\r \x01(\t\x12\x0f\n\x07Version\x18\x0e \x01(\t\"A\n\x13VodCommonConfigInfo\x12\x0e\n\x06Module\x18\x01 \x01(\t\x12\x0b\n\x03Key\x18\x02 \x01(\t\x12\r\n\x05Value\x18\x03 \x01(\t\"\xcc\x04\n\x10VodPlayInfoModel\x12\x46\n\x07Version\x18\n \x01(\x0e\x32\x35.Byteplus.Vod.Models.Business.VodPlayInfoModelVersion\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0e\n\x06Status\x18\x02 \x01(\x05\x12\x11\n\tPosterUrl\x18\x03 \x01(\t\x12\x10\n\x08\x44uration\x18\x04 \x01(\x02\x12\x10\n\x08\x46ileType\x18\x05 \x01(\t\x12\x16\n\x0e\x45nableAdaptive\x18\x06 \x01(\x08\x12\x12\n\nTotalCount\x18\x07 \x01(\x05\x12\x43\n\x0c\x41\x64\x61ptiveInfo\x18\x08 \x01(\x0b\x32-.Byteplus.Vod.Models.Business.VodAdaptiveInfo\x12?\n\x0cPlayInfoList\x18\t \x03(\x0b\x32).Byteplus.Vod.Models.Business.VodPlayInfo\x12\x41\n\rThumbInfoList\x18\x0b \x03(\x0b\x32*.Byteplus.Vod.Models.Business.VodThumbInfo\x12\x16\n\x0e\x42\x61rrageMaskUrl\x18\x0c \x01(\t\x12G\n\x10SubtitleInfoList\x18\r \x03(\x0b\x32-.Byteplus.Vod.Models.Business.VodSubtitleInfo\x12\x46\n\x0f\x42\x61rrageMaskInfo\x18\x0e \x01(\x0b\x32-.Byteplus.Vod.Models.Business.BarrageMaskInfo\",\n\x08VodPoint\x12\x11\n\tTimestamp\x18\x01 \x01(\x01\x12\r\n\x05Value\x18\x02 \x01(\x01\"\x94\x01\n\x14VodAllPlayInfoResult\x12R\n\x17VodAllPlayInfoModelList\x18\x01 \x03(\x0b\x32\x31.Byteplus.Vod.Models.Business.VodAllPlayInfoModel\x12\x12\n\nTotalCount\x18\x02 \x01(\x05\x12\x14\n\x0cNotFoundVids\x18\x03 \x03(\t\"\xb4\x04\n\x13VodAllPlayInfoModel\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0e\n\x06Status\x18\x02 \x01(\x05\x12\x11\n\tPosterUrl\x18\x03 \x01(\t\x12\x12\n\nTotalCount\x18\x04 \x01(\x05\x12\x16\n\x0e\x45nableAdaptive\x18\x05 \x01(\x08\x12G\n\x14VodTranscodePlayInfo\x18\x06 \x03(\x0b\x32).Byteplus.Vod.Models.Business.VodPlayInfo\x12\x44\n\x11VodSourcePlayInfo\x18\x07 \x01(\x0b\x32).Byteplus.Vod.Models.Business.VodPlayInfo\x12\x46\n\x07Version\x18\x08 \x01(\x0e\x32\x35.Byteplus.Vod.Models.Business.VodPlayInfoModelVersion\x12\x41\n\rThumbInfoList\x18\t \x03(\x0b\x32*.Byteplus.Vod.Models.Business.VodThumbInfo\x12\x16\n\x0e\x42\x61rrageMaskUrl\x18\n \x01(\t\x12G\n\x10SubtitleInfoList\x18\x0b \x03(\x0b\x32-.Byteplus.Vod.Models.Business.VodSubtitleInfo\x12\x46\n\x0f\x42\x61rrageMaskInfo\x18\x0c \x01(\x0b\x32-.Byteplus.Vod.Models.Business.BarrageMaskInfo*\xd6\x01\n\x17VodPlayInfoModelVersion\x12$\n UndefinedVodPlayInfoModelVersion\x10\x00\x12%\n!InternalV1VodPlayInfoModelVersion\x10\x01\x12%\n!InternalV2VodPlayInfoModelVersion\x10\x02\x12%\n!InternalV3VodPlayInfoModelVersion\x10\x03\x12 \n\x1cToBV1VodPlayInfoModelVersion\x10\x04\x42\xd9\x01\n\'com.byteplus.service.vod.model.businessB\tVodCommonP\x01ZGgithub.com/byteplus-sdk/byteplus-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02$Byteplus\\Service\\Vod\\Models\\Business\xe2\x02\'Byteplus\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')

_VODPLAYINFOMODELVERSION = DESCRIPTOR.enum_types_by_name['VodPlayInfoModelVersion']
VodPlayInfoModelVersion = enum_type_wrapper.EnumTypeWrapper(_VODPLAYINFOMODELVERSION)
UndefinedVodPlayInfoModelVersion = 0
InternalV1VodPlayInfoModelVersion = 1
InternalV2VodPlayInfoModelVersion = 2
InternalV3VodPlayInfoModelVersion = 3
ToBV1VodPlayInfoModelVersion = 4


_VODSOURCEINFO = DESCRIPTOR.message_types_by_name['VodSourceInfo']
_VODAUDIOSTREAMMETA = DESCRIPTOR.message_types_by_name['VodAudioStreamMeta']
_VODVIDEOSTREAMMETA = DESCRIPTOR.message_types_by_name['VodVideoStreamMeta']
_VODTRANSCODEINFO = DESCRIPTOR.message_types_by_name['VodTranscodeInfo']
_VODADAPTIVEINFO = DESCRIPTOR.message_types_by_name['VodAdaptiveInfo']
_VODPLAYINFO = DESCRIPTOR.message_types_by_name['VodPlayInfo']
_VODVOLUMEINFO = DESCRIPTOR.message_types_by_name['VodVolumeInfo']
_BARRAGEMASKINFO = DESCRIPTOR.message_types_by_name['BarrageMaskInfo']
_VODTHUMBINFO = DESCRIPTOR.message_types_by_name['VodThumbInfo']
_VODSUBTITLEINFO = DESCRIPTOR.message_types_by_name['VodSubtitleInfo']
_VODCOMMONCONFIGINFO = DESCRIPTOR.message_types_by_name['VodCommonConfigInfo']
_VODPLAYINFOMODEL = DESCRIPTOR.message_types_by_name['VodPlayInfoModel']
_VODPOINT = DESCRIPTOR.message_types_by_name['VodPoint']
_VODALLPLAYINFORESULT = DESCRIPTOR.message_types_by_name['VodAllPlayInfoResult']
_VODALLPLAYINFOMODEL = DESCRIPTOR.message_types_by_name['VodAllPlayInfoModel']
VodSourceInfo = _reflection.GeneratedProtocolMessageType('VodSourceInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODSOURCEINFO,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodSourceInfo)
  })
_sym_db.RegisterMessage(VodSourceInfo)

VodAudioStreamMeta = _reflection.GeneratedProtocolMessageType('VodAudioStreamMeta', (_message.Message,), {
  'DESCRIPTOR' : _VODAUDIOSTREAMMETA,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodAudioStreamMeta)
  })
_sym_db.RegisterMessage(VodAudioStreamMeta)

VodVideoStreamMeta = _reflection.GeneratedProtocolMessageType('VodVideoStreamMeta', (_message.Message,), {
  'DESCRIPTOR' : _VODVIDEOSTREAMMETA,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodVideoStreamMeta)
  })
_sym_db.RegisterMessage(VodVideoStreamMeta)

VodTranscodeInfo = _reflection.GeneratedProtocolMessageType('VodTranscodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODTRANSCODEINFO,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodTranscodeInfo)
  })
_sym_db.RegisterMessage(VodTranscodeInfo)

VodAdaptiveInfo = _reflection.GeneratedProtocolMessageType('VodAdaptiveInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODADAPTIVEINFO,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodAdaptiveInfo)
  })
_sym_db.RegisterMessage(VodAdaptiveInfo)

VodPlayInfo = _reflection.GeneratedProtocolMessageType('VodPlayInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODPLAYINFO,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodPlayInfo)
  })
_sym_db.RegisterMessage(VodPlayInfo)

VodVolumeInfo = _reflection.GeneratedProtocolMessageType('VodVolumeInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODVOLUMEINFO,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodVolumeInfo)
  })
_sym_db.RegisterMessage(VodVolumeInfo)

BarrageMaskInfo = _reflection.GeneratedProtocolMessageType('BarrageMaskInfo', (_message.Message,), {
  'DESCRIPTOR' : _BARRAGEMASKINFO,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.BarrageMaskInfo)
  })
_sym_db.RegisterMessage(BarrageMaskInfo)

VodThumbInfo = _reflection.GeneratedProtocolMessageType('VodThumbInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODTHUMBINFO,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodThumbInfo)
  })
_sym_db.RegisterMessage(VodThumbInfo)

VodSubtitleInfo = _reflection.GeneratedProtocolMessageType('VodSubtitleInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODSUBTITLEINFO,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodSubtitleInfo)
  })
_sym_db.RegisterMessage(VodSubtitleInfo)

VodCommonConfigInfo = _reflection.GeneratedProtocolMessageType('VodCommonConfigInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMONCONFIGINFO,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodCommonConfigInfo)
  })
_sym_db.RegisterMessage(VodCommonConfigInfo)

VodPlayInfoModel = _reflection.GeneratedProtocolMessageType('VodPlayInfoModel', (_message.Message,), {
  'DESCRIPTOR' : _VODPLAYINFOMODEL,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodPlayInfoModel)
  })
_sym_db.RegisterMessage(VodPlayInfoModel)

VodPoint = _reflection.GeneratedProtocolMessageType('VodPoint', (_message.Message,), {
  'DESCRIPTOR' : _VODPOINT,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodPoint)
  })
_sym_db.RegisterMessage(VodPoint)

VodAllPlayInfoResult = _reflection.GeneratedProtocolMessageType('VodAllPlayInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODALLPLAYINFORESULT,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodAllPlayInfoResult)
  })
_sym_db.RegisterMessage(VodAllPlayInfoResult)

VodAllPlayInfoModel = _reflection.GeneratedProtocolMessageType('VodAllPlayInfoModel', (_message.Message,), {
  'DESCRIPTOR' : _VODALLPLAYINFOMODEL,
  '__module__' : 'byteplus.vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.VodAllPlayInfoModel)
  })
_sym_db.RegisterMessage(VodAllPlayInfoModel)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'com.byteplus.service.vod.model.businessB\tVodCommonP\001ZGgithub.com/byteplus-sdk/byteplus-sdk-golang/service/vod/models/business\240\001\001\330\001\001\302\002\000\312\002$Byteplus\\Service\\Vod\\Models\\Business\342\002\'Byteplus\\Service\\Vod\\Models\\GPBMetadata'
  _VODPLAYINFOMODELVERSION._serialized_start=3812
  _VODPLAYINFOMODELVERSION._serialized_end=4026
  _VODSOURCEINFO._serialized_start=73
  _VODSOURCEINFO._serialized_end=549
  _VODAUDIOSTREAMMETA._serialized_start=551
  _VODAUDIOSTREAMMETA._serialized_end=658
  _VODVIDEOSTREAMMETA._serialized_start=661
  _VODVIDEOSTREAMMETA._serialized_end=795
  _VODTRANSCODEINFO._serialized_start=798
  _VODTRANSCODEINFO._serialized_end=1181
  _VODADAPTIVEINFO._serialized_start=1183
  _VODADAPTIVEINFO._serialized_end=1266
  _VODPLAYINFO._serialized_start=1269
  _VODPLAYINFO._serialized_end=1750
  _VODVOLUMEINFO._serialized_start=1752
  _VODVOLUMEINFO._serialized_end=1799
  _BARRAGEMASKINFO._serialized_start=1802
  _BARRAGEMASKINFO._serialized_end=1965
  _VODTHUMBINFO._serialized_start=1968
  _VODTHUMBINFO._serialized_end=2128
  _VODSUBTITLEINFO._serialized_start=2131
  _VODSUBTITLEINFO._serialized_end=2387
  _VODCOMMONCONFIGINFO._serialized_start=2389
  _VODCOMMONCONFIGINFO._serialized_end=2454
  _VODPLAYINFOMODEL._serialized_start=2457
  _VODPLAYINFOMODEL._serialized_end=3045
  _VODPOINT._serialized_start=3047
  _VODPOINT._serialized_end=3091
  _VODALLPLAYINFORESULT._serialized_start=3094
  _VODALLPLAYINFORESULT._serialized_end=3242
  _VODALLPLAYINFOMODEL._serialized_start=3245
  _VODALLPLAYINFOMODEL._serialized_end=3809
# @@protoc_insertion_point(module_scope)