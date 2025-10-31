# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""
Python module serving as a project/extension template.
"""

# Register Gym environments.
from . import g1_tennis_cfg as _g1_tennis_cfg  # noqa: F401  # side-effect: registers envs
from .tasks import *

# Register UI extensions.
from .ui_extension_example import *
