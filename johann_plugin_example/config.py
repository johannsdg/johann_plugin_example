# Copyright (c) 2020-present, The Johann Plugin Example Authors. All Rights Reserved.
# Use of this source code is governed by a BSD-3-clause license that can
# be found in the LICENSE file. See the AUTHORS file for names of contributors.
import os

from johann.shared.config import JohannConfig
from johann.shared.logger import JohannLogger

config = JohannConfig.get_config()
logger = JohannLogger(__name__).logger

# Modifications of main johann config, if any
config.HOST_IMAGE_PARAMS["johann_player_alpine"] = {
    "user": None,
    "env_pwd": None,
    "os": "LINUX",
    "python_path": "/usr/local/bin/python",
    "python_ver": "3.8",
    "pmtr_variant": "NONE",
    "control_method": "DOCKER",
    "pip_offline_install": False,
}

# Plugin-specific shared/config vars, if any
RANDOM_SEED: int = int(os.getenv("EXAMPLE_RANDOM_SEED", "42"))
