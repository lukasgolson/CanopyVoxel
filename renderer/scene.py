from .world import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.ChunkMeshBuilder = CubeChunkMeshBuilder(self.world)

    def update(self, app):
        self.world.update()

    def render(self):
        self.world.render()
