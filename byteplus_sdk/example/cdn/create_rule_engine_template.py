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

    # Create a rule engine policy that sets the cache time to 0 seconds under any conditions.
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

    rsp = cdn_service.create_rule_engine_template({
        "Project": "default",
        "Title": "example",
        "Message": "Under any conditions, set the cache time to 0 seconds",
        "Rule": rule.encode_to_string()
    })
    print(rsp)

def example2():
    cdn_service = CDNService()
    cdn_service.set_ak(ak)
    cdn_service.set_sk(sk)

    # When the Referer request header is equal to 'example', set the HTTP response header 'test' with a value of abc123.
    rule = Rule()
    rule.desc = "example"
    rule.if_block.condition = Condition({
        "IsGroup": False,
        "Connective": Const.ConnectiveAnd,
        "Condition": {
						"Object": Const.ConditionHTTPReferer,
						"Operator": Const.OperatorEqual,
						"Value": ["example"],
						"IgnoreCase":  True
					}
    })
    rule.if_block.actions.append(Action({
        "Action": Const.ConditionResponseHeader,
        "Groups": [{
            "Dimension": Const.ActionResponseHeader,
            "GroupParameters": [{
                "Parameters": [
                    {
                        "Name": "action",
                        "Values": ["set"]
                    },
                    {
                        "Name": "header_name",
                        "Values": ["test"]
                    },
                    {
                        "Name": "header_value",
                        "Values": ["abc123"]
                    }
                ]
            }]
        }]
    }))

    rsp = cdn_service.create_rule_engine_template({
        "Project": "default",
        "Title": "example2",
        "Message": "When the Referer request header is equal to 'example', set the HTTP response header 'test' with a value of abc123.",
        "Rule": rule.encode_to_string()
    })
    print(rsp)

def example3():
    cdn_service = CDNService()
    cdn_service.set_ak(ak)
    cdn_service.set_sk(sk)

    # URL matching, equal to http://www.example.com/path1?a=1 When case is ignored, the protocol forces a redirect, with a redirect status code of 301 and a redirect protocol of HTTPS
    rule = Rule()
    rule.desc = "example"
    rule.if_block.condition = Condition({
        "IsGroup": False,
        "Connective": Const.ConnectiveAnd,
        "Condition": {
						"Object": Const.ConditionHTTPUrl,
						"Operator": Const.OperatorEqual,
						"Value": ["http://www.test.com/path1?a=1"],
						"IgnoreCase":  True
					}
    })
    rule.if_block.actions.append(Action({
        "Action": Const.ActionRedirectProtocol,
        "Groups": [{
            "Dimension": Const.ActionRedirectProtocol,
            "GroupParameters": [{
                "Parameters": [
                    {
                        "Name": "status_code",
                        "Values": ["301"]
                    },
                    {
                        "Name": "protocol",
                        "Values": ["https"]
                    }
                ]
            }]
        }]
    }))

    rsp = cdn_service.create_rule_engine_template({
        "Project": "default",
        "Title": "example3",
        "Message": "",
        "Rule": rule.encode_to_string()
    })
    print(rsp)

if __name__ == '__main__':
    example1()
    example2()
    example3()
