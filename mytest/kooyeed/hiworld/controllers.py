# vim: tabstop=4 shiftwidth=4 softtabstop=4


import json

from mytest.common import controller
from mytest.common import cms
from mytest.common import logging
from mytest import config
from mytest import exception
from mytest.openstack.common import importutils


LOG = logging.getLogger(__name__)

CONF = config.CONF

# registry of authentication methods
AUTH_METHODS = {}

class HiTony(controller.V1Controller):
    def __init__(self, *args, **kw):
        super(HiTony, self).__init__(*args, **kw)               

    def tony(self, context):
        print("context:", context)
        return {'signed': "hi, I am Tony."}
