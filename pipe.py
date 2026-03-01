import pygame as py
from brain import *
import agentController as Agent

class Pipe:
    pipe_list = []
    PIPE_SPEED = 75
    PIPE_WIDTH = 30
    DT = 0
    SCREEN = None
    RIGHTMOST = None
    LEFTMOST = None

    def __init__(self, pos = py.Vector2(0,0)):
        self.pos = pos
        self.size = 80
        self.timer = 0
        self.time_update = 1
        self.top_rect = (self.pos.x - Pipe.PIPE_WIDTH / 2, 0, Pipe.PIPE_WIDTH ,self.pos.y - self.size)
        self.bottom_rect = None

        self.pos.y = Brain.random_range(self.size,Pipe.SCREEN.get_height() - self.size )

        Pipe.pipe_list.append(self)
    
    def update(dt):
        for pipe in Pipe.pipe_list[:]:
            pipe.pos.x -= Pipe.PIPE_SPEED * dt
            if pipe.pos.x < Pipe.SCREEN.get_width() / 2:
                for agente in Agent.Agent.agents:
                    if agente.alive:
                        agente.pipes_passed += 1
                Pipe.pipe_list.remove(pipe)

        if not Pipe.pipe_list:
            return

        Pipe.RIGHTMOST = max(Pipe.pipe_list, key=lambda p: p.pos.x)
        Pipe.LEFTMOST = min(Pipe.pipe_list, key=lambda p: p.pos.x)

        if Pipe.RIGHTMOST.pos.x <= Pipe.SCREEN.get_width() - 150:
            Pipe(py.Vector2(Pipe.SCREEN.get_width() + 80, 0))

    def draw(screen):
        screen_h = screen.get_height()

        for pipe in Pipe.pipe_list:
            pipe.top_rect = py.Rect(
                int(pipe.pos.x - Pipe.PIPE_WIDTH / 2),
                0,
                int(Pipe.PIPE_WIDTH),
                int(pipe.pos.y - pipe.size)
            )

            pipe.bottom_rect = py.Rect(
                int(pipe.pos.x - Pipe.PIPE_WIDTH / 2),
                int(pipe.pos.y + pipe.size),
                int(Pipe.PIPE_WIDTH),
                int(screen_h - (pipe.pos.y + pipe.size))
            )
            py.draw.rect(screen, "red", pipe.top_rect)
            py.draw.rect(screen, "green", pipe.bottom_rect)