# Licensed to Tomaz Muraus under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# Tomaz muraus licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from os.path import join as pjoin

from django.conf import settings

BASE_DIR = os.path.realpath(os.path.dirname(__file__))
DEFAULT_GEOIP_DATABASE_PATH = pjoin(BASE_DIR,
                                    'static/GeoLiteCity.dat')

# Path to the geoip database file
VISITOR_INFO_GEOIP_DATABASE_PATH = getattr(settings,
                                           'VISITOR_INFO_GEOIP_DATABASE_PATH',
                                           DEFAULT_GEOIP_DATABASE_PATH)

# Field on the user profile model which stores a timezone
VISITOR_INFO_PROFILE_TIMEZONE_FIELD = getattr(settings,
                                              'PROFILE_TIMEZONE_FIELD',
                                              'timezone')
# Field on the user profile model which stores unit system
VISITOR_INFO_PROFILE_UNIT_SYSTEM_FIELD = getattr(settings,
                                                 'PROFILE_UNIT_SYSTEM_FIELD',
                                                 'unit_system')
