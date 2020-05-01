"""Example of a custom gym environment and model. Run this for a demo.

This example shows:
  - using a custom environment

You can visualize experiment results in ~/ray_results using TensorBoard.
"""

import gym
from gym.spaces import Discrete, Box
import numpy as np
import ray
from ray import tune

class SimpleCorridor(gym.Env):
    """Example of a custom env in which you have to walk down a corridor.

    You can configure the length of the corridor via the env config."""

    def __init__(self, config):
        self.end_pos = config["corridor_length"]
        self.cur_pos = 0
        self.action_space = Discrete(2)
        self.observation_space = Box(
            0.0, self.end_pos, shape=(1, ), dtype=np.float32)

    def reset(self):
        self.cur_pos = 0
        return [self.cur_pos]

    def step(self, action):
        assert action in [0, 1], action
        if action == 0 and self.cur_pos > 0:
            self.cur_pos -= 1
        elif action == 1:
            self.cur_pos += 1
        done = self.cur_pos >= self.end_pos
        return [self.cur_pos], 1 if done else 0, done, {}


if __name__ == "__main__":
    # Can also register the env creator function explicitly with:
    # register_env("corridor", lambda config: SimpleCorridor(config))
    ray.init()
    tune.run(
        "PPO",
        stop={
            "timesteps_total": 100000,
        },
        config={
            "env": SimpleCorridor,  # or "corridor" if registered above
            "num_workers": 4,  # parallelism
            "env_config": {
                "corridor_length": 5,
            },
        },
    )
