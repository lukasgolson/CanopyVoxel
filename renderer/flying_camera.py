from .camera import *
from .settings import *

import pygame as pg


class FlyingCamera(Camera):
    def __init__(self, app, position=(0, 150, 0), yaw=-90, pitch=0, speed=0.1, sensitivity=0.002):
        self.app = app
        super().__init__(position, yaw, pitch)

        self.speed = speed
        self.sensitivity = sensitivity

    def update(self, app):
        if self.app.window_has_focus:
            self.keyboard_control()
            self.mouse_control()
        super().update(app)

    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        if mouse_dx:
            self.rotate_yaw(delta_x=mouse_dx * self.sensitivity)
        if mouse_dy:
            self.rotate_pitch(delta_y=mouse_dy * self.sensitivity)

    def keyboard_control(self):
        key_state = pg.key.get_pressed()
        vel = self.speed * self.app.delta_time
        if key_state[pg.K_w]:
            self.move_forward(vel)
        if key_state[pg.K_s]:
            self.move_back(vel)
        if key_state[pg.K_d]:
            self.move_right(vel)
        if key_state[pg.K_a]:
            self.move_left(vel)
        if key_state[pg.K_SPACE]:
            self.move_up(vel)
        if key_state[pg.K_LSHIFT]:
            self.move_down(vel)
