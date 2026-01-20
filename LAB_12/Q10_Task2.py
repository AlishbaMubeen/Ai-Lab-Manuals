
import gymnasium as gym
env = gym.make('MountainCar-v0')
state, info = env.reset()
for _ in range(100): # Running for 100 steps
    # state[0] = Position, state[1] = Velocity
    print(f"State Array: {state} | Position: {state[0]:.4f} | Velocity: {state[1]:.4f}")
    action = env.action_space.sample()
    state, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        break
env.close()
