# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: GPL-3.0

import os

from six.moves import configparser

from column.api_runner import APIRunner
from column.callback import AnsibleCallback
from column.runner import Runner
from column.subprocess_runner import SubprocessRunner


DEFAULT_CONF_FILE = os.path.join(os.sep, 'etc', 'column', 'column.conf')

__all__ = [
    'APIRunner', 'Runner', 'SubprocessRunner', 'AnsibleCallback'
]


__version__ = '0.5.2'

DEFAULTS = {
    'log_file': os.path.join(os.sep, 'var', 'log', 'column.log'),
    'log_level': 'DEBUG',
    'server': '127.0.0.1',
    'port': '48620'
}

cfg = configparser.ConfigParser(DEFAULTS)
cfg.read(DEFAULT_CONF_FILE)
