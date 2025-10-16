# coding:utf-8
from __future__ import print_function

from byteplus_sdk import visual
from byteplus_sdk.visual.VisualService import VisualService

if __name__ == '__main__':
    visual_service = VisualService()

    # call below method if you don't set ak and sk in $HOME/.volc/config
    visual_service.set_ak('AK')
    visual_service.set_sk('Sk')

    form = {
        "req_key": "xxx",
        "task_id": "xxx"
    }
    resp = visual_service.cv_get_result(form)
    print(resp)