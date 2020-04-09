# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import gym

environment = gym.make("MountainCar-v0")
environment.rest()
for _ in range(2000):
    environment.render()
    envaironment.step(envaironment.action_space.sample())
    
