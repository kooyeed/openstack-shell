# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2011 OpenStack LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Base model for keystone internal services

Unless marked otherwise, all fields are strings.

"""


class Model(dict):
    """Base model class."""
    def __hash__(self):
        return self['id'].__hash__()

    @property
    def known_keys(cls):
        return cls.required_keys + cls.optional_keys


class Token(Model):
    """Token object.

    Required keys:
        id
        expires (datetime)

    Optional keys:
        user
        tenant
        metadata
        trust_id
    """

    required_keys = ('id', 'expires')
    optional_keys = ('extra',)


