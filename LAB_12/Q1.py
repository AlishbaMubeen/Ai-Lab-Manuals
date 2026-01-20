
!pip install gymnasium
import gymnasium as gym
import numpy as np
env = gym.make("CartPole-v1", render_mode="rgb_array")
num_episodes = 50
scores = []
for episode in range(1, num_episodes + 1):
    score = 0
    state, info = env.reset()
    done = False

    while not done:
        action = env.action_space.sample()
        state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        score += reward
    scores.append(score)
    print(f"Episode {episode} Score: {score}")

average_score = np.mean(scores)
print(f"\nAverage Score over {num_episodes} episodes: {average_score:.2f}")
