import numpy as np

from .camera import *
from .chunk import *
from .chunk import Chunk
from .meshes.cube_chunk_mesh_builder import CubeChunkMeshBuilder
from .voxel_manager import *


class World:
    def __init__(self, app, world_dims: tuple[int, int, int] = (8, 8, 8), chunk_size: int = 32):
        self.app = app

        self.chunk_size = chunk_size
        self.half_chunk_size = chunk_size // 2
        self.chunk_area = chunk_size * chunk_size
        self.chunk_volume = self.chunk_area * chunk_size

        self.world_width = world_dims[0]
        self.world_height = world_dims[1]
        self.world_depth = world_dims[2]
        self.world_area = self.world_width * self.world_depth
        self.world_volume = self.world_area * self.world_height

        self.chunks: list[Chunk] = [None for _ in range(self.world_volume)]
        self.voxelManager = VoxelManager(self)

        self.voxels = np.empty(([self.world_volume, self.chunk_volume, 3]), dtype=np.uint8)

        self.build_chunks()
        self.build_chunk_mesh()

    def build_chunks(self):
        for x in range(self.world_width):
            for y in range(self.world_height):
                for z in range(self.world_depth):
                    chunk = Chunk(self, position=(x, y, z))

                    chunk_index = x + self.world_width * z + self.world_area * y
                    self.chunks[chunk_index] = chunk

                    self.voxels[chunk_index] = chunk.build_voxels()

                    chunk.voxels = self.voxels[chunk_index]

    def build_chunk_mesh(self):
        for chunk in self.chunks:
            chunk.build_mesh()

    def update(self):
        pass

    def render(self):
        for chunk in self.chunks:
            chunk.render()
