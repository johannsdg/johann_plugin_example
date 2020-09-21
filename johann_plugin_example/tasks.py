# Copyright (c) 2020-present, The Johann Plugin Example Authors. All Rights Reserved.
# Use of this source code is governed by a BSD-3-clause license that can
# be found in the LICENSE file. See the AUTHORS file for names of contributors.

import time
from typing import TYPE_CHECKING, Dict, Union

import numpy as np  # now we're doing data science!

from johann.shared.config import JohannConfig, celery_app
from johann.shared.logger import JohannLogger
from johann.util import TaskState
from johann_plugin_example import config as example_config

if TYPE_CHECKING:
    from celery import Task


config = JohannConfig.get_config()
logger = JohannLogger(__name__).logger


@celery_app.task(bind=True)
def baby_nap(
    self: "Task", desired_duration: int, random_seed: int = example_config.RANDOM_SEED
) -> Dict[str, Union[float, str]]:
    logger.info(f"The baby will nap for up to {desired_duration} seconds")

    # set random seed
    np.random.seed(random_seed)

    # book-keeping
    start: float = time.time()
    stop: float = start + desired_duration
    now: float = start
    actual_duration: float = 0.0

    while now < stop:
        time.sleep(1)
        now = time.time()
        actual_duration = now - start

        # 10% chance that she will wake up
        if np.random.randint(1, 10) == 3:
            logger.info(f"The baby is up! She slept for {actual_duration} seconds!")
            break

        # report incremental progress
        self.update_state(
            state=TaskState.PROGRESS,
            meta={"current": actual_duration, "total": desired_duration},
        )

    # return final progress
    return {
        "current": actual_duration,
        "total": desired_duration,
        "status": "The baby is up!",
        "result": actual_duration,
    }
