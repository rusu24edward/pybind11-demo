"""Example of a custom gym environment and model. Run this for a demo.

This example shows:
  - using a custom environment
  - using a custom model
  - using Tune for grid search

You can visualize experiment results in ~/ray_results using TensorBoard.
"""

import gym
from gym.core import Wrapper
from gym.spaces import Discrete, Box
import numpy as np
import ray
from ray import tune
from ray.tune.registry import register_env

from build.simple_corridor import SimpleCorridor

class CppWrapper(Wrapper):
    def __init__(self, env, action_space, observation_space):
        self.env = env
        self.action_space = action_space
        self.observation_space = observation_space
    
    def step(self, action):
        obs, reward, done = self.env.step(action)
        return [obs], reward, done, {}
    
    def reset(self):
        return [self.env.reset()]
    
    def close(self):
        pass

def env_creator(env_config):
    env = SimpleCorridor(env_config)
    env = CppWrapper(env, Discrete(2), Box(0.0, 5, shape=(1, ), dtype=np.float32))
    return env  # return an env instance

register_env("SimpleCorridor-v0", env_creator)

if __name__ == "__main__":
    # Can also register the env creator function explicitly with:
    # register_env("corridor", lambda config: SimpleCorridor(config))
    ray.init()
    tune.run(
        "PPO",
        stop={
            "timesteps_total": 10000,
        },
        config={
            "env": "SimpleCorridor-v0",  # or "corridor" if registered above
            "num_workers": 1,  # parallelism
            "env_config": {
                "corridor_length": 5,
            },
        },
    )
