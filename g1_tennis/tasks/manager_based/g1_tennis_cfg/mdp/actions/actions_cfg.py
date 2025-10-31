# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from dataclasses import MISSING

from isaaclab.controllers import DifferentialIKControllerCfg, OperationalSpaceControllerCfg
from isaaclab.managers.action_manager import ActionTerm, ActionTermCfg
from isaaclab.utils import configclass

from . import joint_actions
from isaaclab.envs.mdp import JointActionCfg

##
# Joint actions.
##

@configclass
class HomieJointPositionActionCfg(JointActionCfg):
    """Configuration for the Homie joint position action term.

    See :class:`HomieJointPositionAction` for more details.
    """

    class_type: type[ActionTerm] = joint_actions.HomieJointPositionAction

    use_default_offset: bool = True
    preserve_order: bool = True
    """Whether to use default joint positions configured in the articulation asset as offset.
    Defaults to True."""