

from build.simple_corridor import SimpleCorridor

my_cor = SimpleCorridor({'corridor_length': 5})
obs = my_cor.reset()
obs, reward, done = my_cor.step(1)

print(reward)