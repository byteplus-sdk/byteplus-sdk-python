# coding:utf-8
from __future__ import print_function

from byteplus_sdk.visual.VisualService import VisualService

if __name__ == '__main__':
    visual_service = VisualService()

    # call below method if you dont set ak and sk in $HOME/.volc/config
    visual_service.set_ak('ak')
    visual_service.set_sk('sk')

    # below shows the sdk usage for all common apis,
    # if you cannot find the needed one, please check other example files in the same dir
    # or contact us for further help
    form = dict()
    with open("image.jpg", "rb") as f:
        import base64
        image = f.read()
        form["image_base64"] = base64.b64encode(image)

    # comic portrait
    # form["cartoon_type"] = "jpcartoon_head"
    # form["rotation"] = 0 # this param is valid only when cartoon_type == jpcartoon_head
    # resp = visual_service.comic_portrait(form)

    # portrait fusion
    # form["template_base64"] = "template_base64_str"
    # form["action_id"] = "faceswap"
    # resp = visual_service.portrait_fusion(form)

    print(resp)
