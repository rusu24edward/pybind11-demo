

from build.simple_corridor import SimpleCorridor

from gym.spaces import Discrete
from gym.core import Wrapper

class CppWrapper(Wrapper):
    def __init__(self, env, action_space, observation_space):
        self.env = env
        self.action_space = action_space
        self.observation_space = observation_space
    

env = SimpleCorridor({'corridor_length': 5})

env = CppWrapper(env, Discrete(2), Discrete(5))

obs = env.reset()
obs, reward, done = env.step(1)

print(reward)