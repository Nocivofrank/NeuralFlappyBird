import pygame as py, os
from agentController import *
from brain import *
import pipe

py.init()

os.system('cls')
print("Version", "1.0")

size = py.Vector2(800, 600)
screen = py.display.set_mode(size)

py.display.set_caption("Sim")

running = True
clock = py.time.Clock()
dt = 0

pipe.Pipe.SCREEN = screen
prev_best_brain = None
prev_best_brain_fitness = 0

for i in range(10):
    Agent(pos=py.Vector2(screen.get_width()/2 , screen.get_height()/2))

best_agent_wait_time = .2
best_timer = 0

pipe.Pipe(py.Vector2(screen.get_width() - screen.get_width() / 10, 0))

while running:
    dt = clock.tick(120) / 1000

    pipe.Pipe.DT = dt
    pipe.Pipe.SCREEN = screen

    screen.fill('black')
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        
        if event.type == py.KEYDOWN:
            print(py.key.name(event.key))

    Agent.Update(dt, screen)
    Agent.Draw(screen)

    if Agent.amount_dead() == 10:
        if best_timer >= best_agent_wait_time:
            best_timer = 0
            best = (max(Agent.agents, key=lambda p: p.time_alive))
            worst = (min(Agent.agents, key=lambda p: p.time_alive))

            diff = best.time_alive - worst.time_alive

            if diff > 1:
                if prev_best_brain_fitness < best.time_alive + (best.pipes_passed * 5):
                    prev_best_brain = best.brain.clone()
                    fitness = best.time_alive + (best.pipes_passed * 5)
                    prev_best_brain_fitness = fitness
                    print(best.time_alive)
                for i, agente in enumerate(Agent.agents):
                    agente.reset(py.Vector2(screen.get_width()/2 , screen.get_height()/2 + i * 5), brain=prev_best_brain.clone(), mutate=False)
            else:
                if prev_best_brain:
                    for i , agente in enumerate(Agent.agents):
                        if i == 0:
                            agente.reset(py.Vector2(screen.get_width()/2 , screen.get_height()/2 + i * 5), brain=prev_best_brain.clone(), mutate=False)
                        else:
                            agente.reset(py.Vector2(screen.get_width()/2 , screen.get_height()/2 + i * 5), brain=prev_best_brain.clone(), mutate=True)
                else:
                    for agente in Agent.agents:
                        agente.reset(py.Vector2(screen.get_width()/2 , screen.get_height()/2))
        else:
            best_timer += dt

    pipe.Pipe.update(dt)
    pipe.Pipe.draw(screen)

    py.display.flip()

py.quit()