
!pip install gymnasium

import gymnasium as gym

env = gym.make("MountainCar-v0", render_mode="rgb_array")

num_episodes = 20
scores = []

for episode in range(1, num_episodes + 1):
    state, info = env.reset()
    done = False
    score = 0

    while not done:
        action = env.action_space.sample()
        state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        score += reward

    scores.append(score)
    print(f"Episode: {episode} | Total Reward: {score}")

print("\nMaximum Reward Achieved:", max(scores))
print("Minimum Reward Achieved:", min(scores))
print("Average Reward:", sum(scores) / len(scores))

env.close()
