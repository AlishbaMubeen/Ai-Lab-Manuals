
!pip install gymnasium

import gymnasium as gym

env = gym.make("MountainCar-v0", render_mode="rgb_array")

state, info = env.reset()

print("Initial State Vector:", state)
print("Number of State Variables:", len(state))

env.close()
