# coding:utf-8
from byteplus_sdk.live.v20230101.live_trait import LiveTrait  # Modify it if necessary


class LiveService(LiveTrait):
    def __init__(self, host='open.byteplusapi.com', ak=None, sk=None):
        super().__init__({
            'ak': ak,
            'sk': sk,
        })
        self.set_host(host)
  