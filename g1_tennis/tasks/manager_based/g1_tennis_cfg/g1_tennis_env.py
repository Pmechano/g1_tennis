import torch
from isaaclab.envs.manager_based_rl_env import ManagerBasedRLEnv
from . import g1_tennis_cfg

class G1TennisEnv(ManagerBasedRLEnv):
    def __init__(self, cfg: g1_tennis_cfg.G1TennisEnvCfg, render_mode: str | None = None, **kwargs):
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.z_min = 0
        self.z_max = 0

        self.homie_command = torch.zeros(cfg.scene.num_envs, 3, device=cfg.sim.device, dtype=torch.float32)       
        self.last_homie_command = torch.zeros(cfg.scene.num_envs, 3, device=cfg.sim.device, dtype=torch.float32)
        self.hit_position = torch.zeros((cfg.scene.num_envs, 3), device=cfg.sim.device, dtype=torch.float32)
        self.hit_position_w = torch.zeros((cfg.scene.num_envs, 3), device=cfg.sim.device, dtype=torch.float32)
        self.target_intercept_time = torch.zeros((cfg.scene.num_envs, 1), device=cfg.sim.device, dtype=torch.float32)
        self.target_intercept_pos = torch.zeros((cfg.scene.num_envs, 3), device=cfg.sim.device, dtype=torch.float32)

        self.debug_mode = False
        
        super().__init__(cfg, render_mode, **kwargs)