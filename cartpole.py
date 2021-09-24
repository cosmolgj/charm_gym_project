import gym
import numpy as np
import random

#env = gym.make('CartPole-v0')
#env = gym.make('MountainCar-v0')
#env = gym.make('Taxi-v3')
#env = gym.make('FrozenLake-v0')
#env = gym.make('Reverse-v0')
env = gym.make('Pong-v0')
#env = gym.make('MsPacman-v0')
#env = gym.make('Breakout-v0')
#env = gym.make('BreakoutDeterministic-v4')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
