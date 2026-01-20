
import gymnasium as gym
import pygame

env = gym.make("CartPole-v1", render_mode="human")

font = None

for episode in range(1, 21):
    score = 0
    state, info = env.reset()
    done = False

    while not done:
        action = env.action_space.sample()
        state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        score += reward

        if font is None:
            pygame.font.init()
            font = pygame.font.SysFont("Arial", 24)

        surface = pygame.display.get_surface()
        surface.fill((0, 0, 0), (0, 0, 400, 50))

        text = font.render(
            f"Episode: {episode} | Score: {int(score)}",
            True,
            (0, 255, 0)
        )
        surface.blit(text, (200, 20))
        pygame.display.update()

        pygame.time.delay(20)

    print(f"Episode {episode} Score: {score}")

env.close()
pygame.quit()
