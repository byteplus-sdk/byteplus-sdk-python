# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: byteplus/vod/business/vod_measure.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'byteplus/vod/business/vod_measure.proto\x12\x1c\x42yteplus.Vod.Models.Business\"<\n\x1d\x44\x65scribeVodSpaceTranscodeItem\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\x03\"\x8d\x01\n%DescribeVodSpaceTranscodeDetailTVUnit\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12V\n\x11TranscodeItemList\x18\x02 \x03(\x0b\x32;.Byteplus.Vod.Models.Business.DescribeVodSpaceTranscodeItem\"\xb3\x01\n\x1f\x44\x65scribeVodSpaceTranscodeDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12\r\n\x05Total\x18\x03 \x01(\x03\x12_\n\x12TranscodeUsageList\x18\x04 \x03(\x0b\x32\x43.Byteplus.Vod.Models.Business.DescribeVodSpaceTranscodeDetailTVUnit\"\xa8\x03\n#DescribeVodSpaceTranscodeDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x15\n\rTranscodeType\x18\x04 \x01(\t\x12\x15\n\rSpecification\x18\x05 \x01(\t\x12\x15\n\rTaskStageList\x18\x06 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x07 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x08 \x03(\t\x12\x1a\n\x12TotalTranscodeData\x18\t \x01(\x03\x12[\n\x16TotalTranscodeDataList\x18\n \x03(\x0b\x32;.Byteplus.Vod.Models.Business.DescribeVodSpaceTranscodeItem\x12^\n\x17TranscodeDataDetailList\x18\x0b \x03(\x0b\x32=.Byteplus.Vod.Models.Business.DescribeVodSpaceTranscodeDetail\"B\n DescribeVodSpaceAIStatisDataItem\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\x10\n\x08\x44uration\x18\x02 \x01(\x03\"\x9f\x01\n\"DescribeVodSpaceAIStatisDataDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12W\n\x0f\x41iUsageDataList\x18\x03 \x03(\x0b\x32>.Byteplus.Vod.Models.Business.DescribeVodSpaceAIStatisDataItem\"\x89\x03\n\"DescribeVodSpaceAIStatisDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x13\n\x0bMediaAiType\x18\x04 \x01(\t\x12\x15\n\rTaskStageList\x18\x05 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x06 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x07 \x03(\t\x12\x18\n\x10TotalAiUsageData\x18\x08 \x01(\x03\x12W\n\x0f\x41iUsageDataList\x18\t \x03(\x0b\x32>.Byteplus.Vod.Models.Business.DescribeVodSpaceAIStatisDataItem\x12_\n\x15\x41iUsageDataDetailList\x18\n \x03(\x0b\x32@.Byteplus.Vod.Models.Business.DescribeVodSpaceAIStatisDataDetail\"E\n&DescribeVodSpaceSubtitleStatisDataItem\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\r\n\x05Usage\x18\x02 \x01(\x03\"\xb1\x01\n(DescribeVodSpaceSubtitleStatisDataDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12\x63\n\x15SubtitleUsageDataList\x18\x03 \x03(\x0b\x32\x44.Byteplus.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataItem\"\xae\x03\n(DescribeVodSpaceSubtitleStatisDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x14\n\x0cSubtitleType\x18\x04 \x01(\t\x12\x15\n\rTaskStageList\x18\x05 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x06 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x07 \x03(\t\x12\x1e\n\x16TotalSubtitleUsageData\x18\x08 \x01(\x03\x12\x63\n\x15SubtitleUsageDataList\x18\t \x03(\x0b\x32\x44.Byteplus.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataItem\x12k\n\x1bSubtitleUsageDataDetailList\x18\n \x03(\x0b\x32\x46.Byteplus.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataDetail\"C\n$DescribeVodSpaceDetectStatisDataItem\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\r\n\x05Usage\x18\x02 \x01(\x03\"\xab\x01\n&DescribeVodSpaceDetectStatisDataDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12_\n\x13\x44\x65tectUsageDataList\x18\x03 \x03(\x0b\x32\x42.Byteplus.Vod.Models.Business.DescribeVodSpaceDetectStatisDataItem\"\xa0\x03\n&DescribeVodSpaceDetectStatisDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x12\n\nDetectType\x18\x04 \x01(\t\x12\x15\n\rTaskStageList\x18\x05 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x06 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x07 \x03(\t\x12\x1c\n\x14TotalDetectUsageData\x18\x08 \x01(\x03\x12_\n\x13\x44\x65tectUsageDataList\x18\t \x03(\x0b\x32\x42.Byteplus.Vod.Models.Business.DescribeVodSpaceDetectStatisDataItem\x12g\n\x19\x44\x65tectUsageDataDetailList\x18\n \x03(\x0b\x32\x44.Byteplus.Vod.Models.Business.DescribeVodSpaceDetectStatisDataDetail\":\n\x1b\x44\x65scribeVodSnapshotDataItem\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\r\n\x05\x43ount\x18\x02 \x01(\x03\"\xa5\x01\n\x1d\x44\x65scribeVodSnapshotDataDetail\x12\r\n\x05Space\x18\x01 \x01(\t\x12\x11\n\tTaskStage\x18\x02 \x01(\t\x12\r\n\x05Total\x18\x03 \x01(\t\x12S\n\x10SnapshotDataList\x18\x04 \x03(\x0b\x32\x39.Byteplus.Vod.Models.Business.DescribeVodSnapshotDataItem\"\xfe\x02\n\x1d\x44\x65scribeVodSnapshotDataResult\x12\x11\n\tSpaceList\x18\x01 \x03(\t\x12\x11\n\tStartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\t\x12\x14\n\x0cSnapshotType\x18\x04 \x01(\t\x12\x15\n\rTaskStageList\x18\x05 \x03(\t\x12\x13\n\x0b\x41ggregation\x18\x06 \x01(\x03\x12\x17\n\x0f\x44\x65tailFieldList\x18\x07 \x03(\t\x12\x19\n\x11TotalSnapshotData\x18\x08 \x01(\x03\x12S\n\x10SnapshotDataList\x18\t \x03(\x0b\x32\x39.Byteplus.Vod.Models.Business.DescribeVodSnapshotDataItem\x12[\n\x16SnapshotDetailDataList\x18\n \x03(\x0b\x32;.Byteplus.Vod.Models.Business.DescribeVodSnapshotDataDetail\"\xd8\x01\n%DescribeVodSpaceWorkflowTranscodeInfo\x12\x14\n\x0cTemplateType\x18\x01 \x01(\t\x12\x10\n\x08\x46ileType\x18\x02 \x01(\t\x12\x10\n\x08\x44uration\x18\x03 \x01(\x03\x12\r\n\x05\x43odec\x18\x04 \x01(\t\x12\r\n\x05Remux\x18\x05 \x01(\x08\x12\x12\n\nDefinition\x18\x06 \x01(\t\x12\r\n\x05Width\x18\x07 \x01(\x03\x12\x0e\n\x06Height\x18\x08 \x01(\x03\x12\r\n\x05Slice\x18\t \x01(\x08\x12\x15\n\rIsLowPriority\x18\n \x01(\x08\"c\n$DescribeVodSpaceWorkflowSnapshotInfo\x12\x14\n\x0cTemplateType\x18\x01 \x01(\t\x12\x0e\n\x06Number\x18\x02 \x01(\x03\x12\x15\n\rIsLowPriority\x18\x03 \x01(\x08\"h\n\'DescribeVodSpaceWorkflowEnhanceExecInfo\x12\x14\n\x0cTemplateType\x18\x01 \x01(\t\x12\x10\n\x08\x44uration\x18\x02 \x01(\x03\x12\x15\n\rIsLowPriority\x18\x03 \x01(\x08\"t\n#DescribeVodSpaceWorkflowVideoAIInfo\x12\x14\n\x0cTemplateType\x18\x01 \x01(\t\x12\x10\n\x08\x44uration\x18\x02 \x01(\x03\x12\x0e\n\x06Number\x18\x03 \x01(\x03\x12\x15\n\rIsLowPriority\x18\x04 \x01(\x08\"\x85\x04\n\x1e\x44\x65scribeVodSpaceWorkflowDetail\x12\r\n\x05RunId\x18\x01 \x01(\t\x12\x0b\n\x03Vid\x18\x02 \x01(\t\x12\x12\n\nTemplateId\x18\x03 \x01(\t\x12\x11\n\tSpaceName\x18\x04 \x01(\t\x12\x0e\n\x06Status\x18\x05 \x01(\t\x12\x11\n\tStartTime\x18\x06 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x07 \x01(\t\x12Z\n\rTranscodeInfo\x18\x08 \x01(\x0b\x32\x43.Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowTranscodeInfo\x12X\n\x0cSnapshotInfo\x18\t \x01(\x0b\x32\x42.Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowSnapshotInfo\x12^\n\x0f\x45nhanceExecInfo\x18\n \x01(\x0b\x32\x45.Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowEnhanceExecInfo\x12V\n\x0bVideoAIInfo\x18\x0b \x01(\x0b\x32\x41.Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowVideoAIInfo\"\xf9\x01\n(DescribeVodSpaceWorkflowDetailDataResult\x12\x0e\n\x06Region\x18\x01 \x01(\t\x12\r\n\x05Space\x18\x02 \x01(\t\x12\x11\n\tStartTime\x18\x03 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x04 \x01(\t\x12\x10\n\x08PageSize\x18\x05 \x01(\x03\x12\x0f\n\x07PageNum\x18\x06 \x01(\x03\x12\r\n\x05Total\x18\x07 \x01(\x03\x12X\n\x12WorkflowDetailData\x18\x08 \x03(\x0b\x32<.Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowDetail\"\x81\x01\n\x1a\x44\x65scribeVodSpaceEditDetail\x12\x0c\n\x04Time\x18\x01 \x01(\t\x12\x11\n\tOutputVid\x18\x02 \x01(\t\x12\r\n\x05Space\x18\x03 \x01(\t\x12\r\n\x05\x43odec\x18\x04 \x01(\t\x12\x12\n\nDefinition\x18\x05 \x01(\t\x12\x10\n\x08\x44uration\x18\x06 \x01(\x03\"\xed\x01\n$DescribeVodSpaceEditDetailDataResult\x12\x0e\n\x06Region\x18\x01 \x01(\t\x12\r\n\x05Space\x18\x02 \x01(\t\x12\x11\n\tStartTime\x18\x03 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x04 \x01(\t\x12\x10\n\x08PageSize\x18\x05 \x01(\x03\x12\x0f\n\x07PageNum\x18\x06 \x01(\x03\x12\r\n\x05Total\x18\x07 \x01(\x03\x12P\n\x0e\x45\x64itDetailData\x18\x08 \x03(\x0b\x32\x38.Byteplus.Vod.Models.Business.DescribeVodSpaceEditDetail\"W\n\"DescribeVodPlayFileLogByDomainItem\x12\x0c\n\x04\x44\x61te\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x13\n\x0b\x44ownloadUrl\x18\x03 \x01(\t\"\xb2\x01\n$DescribeVodPlayFileLogByDomainResult\x12\x11\n\tStartTime\x18\x01 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x02 \x01(\t\x12\x12\n\nDomainList\x18\x03 \x03(\t\x12R\n\x08\x46ileList\x18\x04 \x03(\x0b\x32@.Byteplus.Vod.Models.Business.DescribeVodPlayFileLogByDomainItemB\xd7\x01\n\'com.byteplus.service.vod.model.businessB\nVodMeasureP\x01ZGgithub.com/byteplus-sdk/byteplus-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xca\x02$Byteplus\\Service\\Vod\\Models\\Business\xe2\x02\'Byteplus\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')



_DESCRIBEVODSPACETRANSCODEITEM = DESCRIPTOR.message_types_by_name['DescribeVodSpaceTranscodeItem']
_DESCRIBEVODSPACETRANSCODEDETAILTVUNIT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceTranscodeDetailTVUnit']
_DESCRIBEVODSPACETRANSCODEDETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceTranscodeDetail']
_DESCRIBEVODSPACETRANSCODEDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceTranscodeDataResult']
_DESCRIBEVODSPACEAISTATISDATAITEM = DESCRIPTOR.message_types_by_name['DescribeVodSpaceAIStatisDataItem']
_DESCRIBEVODSPACEAISTATISDATADETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceAIStatisDataDetail']
_DESCRIBEVODSPACEAISTATISDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceAIStatisDataResult']
_DESCRIBEVODSPACESUBTITLESTATISDATAITEM = DESCRIPTOR.message_types_by_name['DescribeVodSpaceSubtitleStatisDataItem']
_DESCRIBEVODSPACESUBTITLESTATISDATADETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceSubtitleStatisDataDetail']
_DESCRIBEVODSPACESUBTITLESTATISDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceSubtitleStatisDataResult']
_DESCRIBEVODSPACEDETECTSTATISDATAITEM = DESCRIPTOR.message_types_by_name['DescribeVodSpaceDetectStatisDataItem']
_DESCRIBEVODSPACEDETECTSTATISDATADETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceDetectStatisDataDetail']
_DESCRIBEVODSPACEDETECTSTATISDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceDetectStatisDataResult']
_DESCRIBEVODSNAPSHOTDATAITEM = DESCRIPTOR.message_types_by_name['DescribeVodSnapshotDataItem']
_DESCRIBEVODSNAPSHOTDATADETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSnapshotDataDetail']
_DESCRIBEVODSNAPSHOTDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSnapshotDataResult']
_DESCRIBEVODSPACEWORKFLOWTRANSCODEINFO = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowTranscodeInfo']
_DESCRIBEVODSPACEWORKFLOWSNAPSHOTINFO = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowSnapshotInfo']
_DESCRIBEVODSPACEWORKFLOWENHANCEEXECINFO = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowEnhanceExecInfo']
_DESCRIBEVODSPACEWORKFLOWVIDEOAIINFO = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowVideoAIInfo']
_DESCRIBEVODSPACEWORKFLOWDETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowDetail']
_DESCRIBEVODSPACEWORKFLOWDETAILDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceWorkflowDetailDataResult']
_DESCRIBEVODSPACEEDITDETAIL = DESCRIPTOR.message_types_by_name['DescribeVodSpaceEditDetail']
_DESCRIBEVODSPACEEDITDETAILDATARESULT = DESCRIPTOR.message_types_by_name['DescribeVodSpaceEditDetailDataResult']
_DESCRIBEVODPLAYFILELOGBYDOMAINITEM = DESCRIPTOR.message_types_by_name['DescribeVodPlayFileLogByDomainItem']
_DESCRIBEVODPLAYFILELOGBYDOMAINRESULT = DESCRIPTOR.message_types_by_name['DescribeVodPlayFileLogByDomainResult']
DescribeVodSpaceTranscodeItem = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceTranscodeItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACETRANSCODEITEM,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceTranscodeItem)
  })
_sym_db.RegisterMessage(DescribeVodSpaceTranscodeItem)

DescribeVodSpaceTranscodeDetailTVUnit = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceTranscodeDetailTVUnit', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACETRANSCODEDETAILTVUNIT,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceTranscodeDetailTVUnit)
  })
_sym_db.RegisterMessage(DescribeVodSpaceTranscodeDetailTVUnit)

DescribeVodSpaceTranscodeDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceTranscodeDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACETRANSCODEDETAIL,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceTranscodeDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceTranscodeDetail)

DescribeVodSpaceTranscodeDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceTranscodeDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACETRANSCODEDATARESULT,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceTranscodeDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceTranscodeDataResult)

DescribeVodSpaceAIStatisDataItem = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceAIStatisDataItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEAISTATISDATAITEM,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceAIStatisDataItem)
  })
_sym_db.RegisterMessage(DescribeVodSpaceAIStatisDataItem)

DescribeVodSpaceAIStatisDataDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceAIStatisDataDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEAISTATISDATADETAIL,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceAIStatisDataDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceAIStatisDataDetail)

DescribeVodSpaceAIStatisDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceAIStatisDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEAISTATISDATARESULT,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceAIStatisDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceAIStatisDataResult)

DescribeVodSpaceSubtitleStatisDataItem = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceSubtitleStatisDataItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACESUBTITLESTATISDATAITEM,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataItem)
  })
_sym_db.RegisterMessage(DescribeVodSpaceSubtitleStatisDataItem)

DescribeVodSpaceSubtitleStatisDataDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceSubtitleStatisDataDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACESUBTITLESTATISDATADETAIL,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceSubtitleStatisDataDetail)

DescribeVodSpaceSubtitleStatisDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceSubtitleStatisDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACESUBTITLESTATISDATARESULT,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceSubtitleStatisDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceSubtitleStatisDataResult)

DescribeVodSpaceDetectStatisDataItem = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceDetectStatisDataItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEDETECTSTATISDATAITEM,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceDetectStatisDataItem)
  })
_sym_db.RegisterMessage(DescribeVodSpaceDetectStatisDataItem)

DescribeVodSpaceDetectStatisDataDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceDetectStatisDataDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEDETECTSTATISDATADETAIL,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceDetectStatisDataDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceDetectStatisDataDetail)

DescribeVodSpaceDetectStatisDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceDetectStatisDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEDETECTSTATISDATARESULT,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceDetectStatisDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceDetectStatisDataResult)

DescribeVodSnapshotDataItem = _reflection.GeneratedProtocolMessageType('DescribeVodSnapshotDataItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSNAPSHOTDATAITEM,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSnapshotDataItem)
  })
_sym_db.RegisterMessage(DescribeVodSnapshotDataItem)

DescribeVodSnapshotDataDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSnapshotDataDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSNAPSHOTDATADETAIL,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSnapshotDataDetail)
  })
_sym_db.RegisterMessage(DescribeVodSnapshotDataDetail)

DescribeVodSnapshotDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSnapshotDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSNAPSHOTDATARESULT,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSnapshotDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSnapshotDataResult)

DescribeVodSpaceWorkflowTranscodeInfo = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowTranscodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWTRANSCODEINFO,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowTranscodeInfo)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowTranscodeInfo)

DescribeVodSpaceWorkflowSnapshotInfo = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowSnapshotInfo', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWSNAPSHOTINFO,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowSnapshotInfo)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowSnapshotInfo)

DescribeVodSpaceWorkflowEnhanceExecInfo = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowEnhanceExecInfo', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWENHANCEEXECINFO,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowEnhanceExecInfo)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowEnhanceExecInfo)

DescribeVodSpaceWorkflowVideoAIInfo = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowVideoAIInfo', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWVIDEOAIINFO,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowVideoAIInfo)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowVideoAIInfo)

DescribeVodSpaceWorkflowDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWDETAIL,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowDetail)

DescribeVodSpaceWorkflowDetailDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceWorkflowDetailDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEWORKFLOWDETAILDATARESULT,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceWorkflowDetailDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceWorkflowDetailDataResult)

DescribeVodSpaceEditDetail = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceEditDetail', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEEDITDETAIL,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceEditDetail)
  })
_sym_db.RegisterMessage(DescribeVodSpaceEditDetail)

DescribeVodSpaceEditDetailDataResult = _reflection.GeneratedProtocolMessageType('DescribeVodSpaceEditDetailDataResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODSPACEEDITDETAILDATARESULT,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodSpaceEditDetailDataResult)
  })
_sym_db.RegisterMessage(DescribeVodSpaceEditDetailDataResult)

DescribeVodPlayFileLogByDomainItem = _reflection.GeneratedProtocolMessageType('DescribeVodPlayFileLogByDomainItem', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODPLAYFILELOGBYDOMAINITEM,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodPlayFileLogByDomainItem)
  })
_sym_db.RegisterMessage(DescribeVodPlayFileLogByDomainItem)

DescribeVodPlayFileLogByDomainResult = _reflection.GeneratedProtocolMessageType('DescribeVodPlayFileLogByDomainResult', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVODPLAYFILELOGBYDOMAINRESULT,
  '__module__' : 'byteplus.vod.business.vod_measure_pb2'
  # @@protoc_insertion_point(class_scope:Byteplus.Vod.Models.Business.DescribeVodPlayFileLogByDomainResult)
  })
_sym_db.RegisterMessage(DescribeVodPlayFileLogByDomainResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'com.byteplus.service.vod.model.businessB\nVodMeasureP\001ZGgithub.com/byteplus-sdk/byteplus-sdk-golang/service/vod/models/business\240\001\001\330\001\001\312\002$Byteplus\\Service\\Vod\\Models\\Business\342\002\'Byteplus\\Service\\Vod\\Models\\GPBMetadata'
  _DESCRIBEVODSPACETRANSCODEITEM._serialized_start=73
  _DESCRIBEVODSPACETRANSCODEITEM._serialized_end=133
  _DESCRIBEVODSPACETRANSCODEDETAILTVUNIT._serialized_start=136
  _DESCRIBEVODSPACETRANSCODEDETAILTVUNIT._serialized_end=277
  _DESCRIBEVODSPACETRANSCODEDETAIL._serialized_start=280
  _DESCRIBEVODSPACETRANSCODEDETAIL._serialized_end=459
  _DESCRIBEVODSPACETRANSCODEDATARESULT._serialized_start=462
  _DESCRIBEVODSPACETRANSCODEDATARESULT._serialized_end=886
  _DESCRIBEVODSPACEAISTATISDATAITEM._serialized_start=888
  _DESCRIBEVODSPACEAISTATISDATAITEM._serialized_end=954
  _DESCRIBEVODSPACEAISTATISDATADETAIL._serialized_start=957
  _DESCRIBEVODSPACEAISTATISDATADETAIL._serialized_end=1116
  _DESCRIBEVODSPACEAISTATISDATARESULT._serialized_start=1119
  _DESCRIBEVODSPACEAISTATISDATARESULT._serialized_end=1512
  _DESCRIBEVODSPACESUBTITLESTATISDATAITEM._serialized_start=1514
  _DESCRIBEVODSPACESUBTITLESTATISDATAITEM._serialized_end=1583
  _DESCRIBEVODSPACESUBTITLESTATISDATADETAIL._serialized_start=1586
  _DESCRIBEVODSPACESUBTITLESTATISDATADETAIL._serialized_end=1763
  _DESCRIBEVODSPACESUBTITLESTATISDATARESULT._serialized_start=1766
  _DESCRIBEVODSPACESUBTITLESTATISDATARESULT._serialized_end=2196
  _DESCRIBEVODSPACEDETECTSTATISDATAITEM._serialized_start=2198
  _DESCRIBEVODSPACEDETECTSTATISDATAITEM._serialized_end=2265
  _DESCRIBEVODSPACEDETECTSTATISDATADETAIL._serialized_start=2268
  _DESCRIBEVODSPACEDETECTSTATISDATADETAIL._serialized_end=2439
  _DESCRIBEVODSPACEDETECTSTATISDATARESULT._serialized_start=2442
  _DESCRIBEVODSPACEDETECTSTATISDATARESULT._serialized_end=2858
  _DESCRIBEVODSNAPSHOTDATAITEM._serialized_start=2860
  _DESCRIBEVODSNAPSHOTDATAITEM._serialized_end=2918
  _DESCRIBEVODSNAPSHOTDATADETAIL._serialized_start=2921
  _DESCRIBEVODSNAPSHOTDATADETAIL._serialized_end=3086
  _DESCRIBEVODSNAPSHOTDATARESULT._serialized_start=3089
  _DESCRIBEVODSNAPSHOTDATARESULT._serialized_end=3471
  _DESCRIBEVODSPACEWORKFLOWTRANSCODEINFO._serialized_start=3474
  _DESCRIBEVODSPACEWORKFLOWTRANSCODEINFO._serialized_end=3690
  _DESCRIBEVODSPACEWORKFLOWSNAPSHOTINFO._serialized_start=3692
  _DESCRIBEVODSPACEWORKFLOWSNAPSHOTINFO._serialized_end=3791
  _DESCRIBEVODSPACEWORKFLOWENHANCEEXECINFO._serialized_start=3793
  _DESCRIBEVODSPACEWORKFLOWENHANCEEXECINFO._serialized_end=3897
  _DESCRIBEVODSPACEWORKFLOWVIDEOAIINFO._serialized_start=3899
  _DESCRIBEVODSPACEWORKFLOWVIDEOAIINFO._serialized_end=4015
  _DESCRIBEVODSPACEWORKFLOWDETAIL._serialized_start=4018
  _DESCRIBEVODSPACEWORKFLOWDETAIL._serialized_end=4535
  _DESCRIBEVODSPACEWORKFLOWDETAILDATARESULT._serialized_start=4538
  _DESCRIBEVODSPACEWORKFLOWDETAILDATARESULT._serialized_end=4787
  _DESCRIBEVODSPACEEDITDETAIL._serialized_start=4790
  _DESCRIBEVODSPACEEDITDETAIL._serialized_end=4919
  _DESCRIBEVODSPACEEDITDETAILDATARESULT._serialized_start=4922
  _DESCRIBEVODSPACEEDITDETAILDATARESULT._serialized_end=5159
  _DESCRIBEVODPLAYFILELOGBYDOMAINITEM._serialized_start=5161
  _DESCRIBEVODPLAYFILELOGBYDOMAINITEM._serialized_end=5248
  _DESCRIBEVODPLAYFILELOGBYDOMAINRESULT._serialized_start=5251
  _DESCRIBEVODPLAYFILELOGBYDOMAINRESULT._serialized_end=5429
# @@protoc_insertion_point(module_scope)
