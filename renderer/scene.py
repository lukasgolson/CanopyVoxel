from .world import *


class Scene:
    def __init__(self, app, world_size, chunk_size):
        self.app = app
        self.world = World(self.app, world_size, chunk_size)
        self.ChunkMeshBuilder = CubeChunkMeshBuilder(self.world)

    def update(self, app):
        self.world.update()

    def render(self):
        self.world.render()
