import pygame as py
from brain import *
import pipe as Pipe

class Agent:
    agents = []
    
    def __init__(self, pos = py.Vector2(0, 0), brain= Brain()):
        self.pos = pos
        self.vel = py.Vector2(0, 0)
        self.direction = py.Vector2(0, 0)
        self.size = 10
        self.speed = 5
        self.color = 'red'
        self.circle_rect = None
        self.alive = True

        self.brain = brain
        self.last_thought = 0
        self.next_thought_delay = 0

        self.time_alive = 0
        self.pipes_passed = 0

        self.display_text_box = True
        self.text_box_color = 'white'
        self.text = "Test"

        self.brain.brainMutate()
        Agent.agents.append(self)

    def reset(self, pos = py.Vector2(0, 0), brain= Brain(), mutate=True):
        self.pos = pos
        self.vel = py.Vector2(0, 0)
        self.direction = py.Vector2(0, 0)
        self.size = 10
        self.speed = 5
        self.color = 'red'
        self.circle_rect = None
        self.alive = True

        self.brain = brain
        self.last_thought = 0
        self.next_thought_delay = 0

        self.time_alive = 0
        self.pipes_passed = 0

        self.display_text_box = True
        self.text_box_color = 'white'
        self.text = "Test"

        if mutate:
            self.brain.brainMutate()
        
    def Update(dt, screen):
        for agent in Agent.agents:
            if agent.alive:
                agent.time_alive += dt
                agent.apply_physics(dt)
                agent.circle_rect = py.Rect(
                    agent.pos.x - agent.size,
                    agent.pos.y - agent.size,
                    agent.size * 2,
                    agent.size * 2
                )
                for pipe in Pipe.Pipe.pipe_list:
                    if pipe is None:
                        print("hmm")
                    else:
                        if pipe.bottom_rect:
                            if agent.circle_rect.colliderect(pipe.top_rect) or agent.circle_rect.colliderect(pipe.bottom_rect):
                                agent.alive = False
                                return

                #circle update
                agent.time_alive += dt
                agent.direction = py.Vector2(0 , 0)
                agent.update_brain_information()

                if agent.last_thought >= agent.next_thought_delay:
                    actions = agent.brain.brainThink()
                    agent.last_thought = 0
                else:
                    agent.last_thought += dt
                    actions = [0,0,0,0,0]

                if actions[0] > actions[1]:
                    agent.direction.y = actions[0]
                else:
                    agent.direction.y = -actions[1]

                if agent.direction.length_squared() > 0:
                    agent.direction = agent.direction.normalize()

                agent.vel *= .98
                agent.vel += agent.direction
                agent.pos += agent.vel * agent.speed * dt

                #edge collider
                if agent.pos.y < 0 + agent.size:
                    agent.pos.y = 0 + agent.size

                if agent.pos.y > screen.get_height() - agent.size:
                    agent.pos.y = screen.get_height() - agent.size
                    agent.vel.y = 0

    def apply_physics(self, dt):
        GRAVITY = 9.81

        # acceleration → velocity
        self.vel.y += GRAVITY * dt

        # velocity → position
        self.pos.y += self.vel.y * dt

    def update_brain_information(self):
        info = self.brain.information

        info[0] = self.pos.x
        info[1] = self.pos.y
        info[2] = self.vel.x
        info[3] = self.vel.y
        if Pipe.Pipe.LEFTMOST:
            info[4] = Pipe.Pipe.LEFTMOST.pos.x
            info[5] = Pipe.Pipe.LEFTMOST.pos.y

        self.brain.information = info

    def Draw(screen):
        for agent in Agent.agents:
            if agent.alive:
                py.draw.circle(screen , agent.color, agent.pos, agent.size)

    def amount_dead():
        count = 0 
        for agent in Agent.agents:
            if not agent.alive:
                count += 1
        return count