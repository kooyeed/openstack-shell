# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack LLC
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import routes

from mytest import config
from mytest import controllers
from mytest.common import logging
from mytest.common import wsgi
from mytest import routers

from mytest.kooyeed import hiworld



CONF = config.CONF
LOG = logging.getLogger(__name__)

DRIVERS = dict()


@logging.fail_gracefully
def admin_version_app_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return wsgi.ComposingRouter(routes.Mapper(),
                                [routers.Versions('admin')])


@logging.fail_gracefully
def admin_v1_app_factory(global_conf, **local_conf):
    controllers.register_version('v1')
    conf = global_conf.copy()
    conf.update(local_conf)
    mapper = routes.Mapper()
    v1routers = []
    for module in [hiworld]:
        module.routers.append_v1_routers(mapper, v1routers)

    v1routers.append(routers.VersionV1('admin'))    
    
    return wsgi.ComposingRouter(mapper, v1routers)
