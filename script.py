

from build.simple_corridor import SimpleCorridor

my_cor = SimpleCorridor(5)
obs = my_cor.reset()
obs, reward, done = my_cor.step(0)

print(obs)
