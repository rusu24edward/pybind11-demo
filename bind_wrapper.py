

from build.simple_corridor import SimpleCorridor

from gym.spaces import Discrete
from cpp_wrapper import CppWrapper
    

env = SimpleCorridor({'corridor_length': 5})

env = CppWrapper(env, Discrete(2), Discrete(5))

obs = env.reset()
obs, reward, done, info = env.step(1)

print(reward)