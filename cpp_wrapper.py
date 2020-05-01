
from gym.core import Wrapper

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