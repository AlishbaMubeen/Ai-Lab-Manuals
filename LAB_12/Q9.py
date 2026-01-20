
!pip install gymnasium

import gymnasium as gym
env = gym.make("MountainCar-v0", render_mode="rgb_array")

num_episodes = 20
scores = []

print("Episode | Score | Remarks")
print("--------------------------")

for episode in range(1, num_episodes + 1):
    state, info = env.reset()
    done = False
    score = 0

    while not done:

        if state[1] > 0:
            action = 1
        else:
            action = 0

        state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        score += reward

    scores.append(score)

    if score > -200:
        remark = "Slight improvement"
    else:
        remark = "Poor (no learning)"

    print(f"{episode:>7} | {score:>5} | {remark}")

print("\nMaximum Score:", max(scores))
print("Average Score:", sum(scores) / len(scores))

env.close()
