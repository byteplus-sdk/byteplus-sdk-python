#  -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../")

from byteplus_sdk.example.cdn import ak, sk
from byteplus_sdk.cdn.service import CDNService

# pip3 install cdn_rule_engine_sdk
from cdn_rule_engine_sdk.rule_engine.Const import Const
from cdn_rule_engine_sdk.rule_engine.Rule import Rule, Condition, Action

def example():
    cdn_service = CDNService()
    cdn_service.set_ak(ak)
    cdn_service.set_sk(sk)

    rule = Rule()
    rule.desc = "example"
    rule.if_block.condition = Condition({
        "IsGroup": False,
        "Connective": Const.ConnectiveAnd,
        "Condition": {
            "Object": Const.ConditionAlways,
        }
    })
    rule.if_block.actions.append(Action({
        "Action": Const.ActionCacheTime,
        "Groups": [{
            "Dimension": Const.ActionCacheTime,
            "GroupParameters": [{
                "Parameters": [
                    {
                        "Name": "ttl",
                        "Values": ["0"]
                    },
                    {
                        "Name": "ttl_unit",
                        "Values": ["sec"]
                    },
                    {
                        "Name": "cache_policy",
                        "Values": [Const.CacheDefault]
                    },
                    {
                        "Name": "force_cache",
                        "Values": ["true"]
                    }
                ]
            }]
        }]
    }))
    rsp = cdn_service.update_rule_engine_template({
        "TemplateId": "tpl-example",
        "TemplateVersion": "draft",
        "Rule": rule.encode_to_string()
    })
    print(rsp)

if __name__ == '__main__':
    example()
