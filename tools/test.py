#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import greenlet
import eventlet
import logging
import os
import signal
import sys
from paste import deploy


app = deploy.loadapp('./test.conf')
