"""Example of a custom gym environment and model. Run this for a demo.

This example shows:
  - using a custom environment
  - using a custom model
  - using Tune for grid search

You can visualize experiment results in ~/ray_results using TensorBoard.
"""

import numpy as np
import gym
# from gym.spaces import Discrete, Box

import ray
from ray import tune


from build.simple_corridor import SimpleCorridor

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
            "env": SimpleCorridor,  # or "corridor" if registered above
            "num_workers": 1,  # parallelism
            "env_config": {
                "corridor_length": 5,
            },
        },
    )
