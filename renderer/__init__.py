import numpy as np

from renderer.addons.sphere_demo import Demo
from renderer.voxel_engine import VoxelEngine


def render_demo():
    """
       Render a demo scene using the VoxelEngine.
    """

    demo = Demo(64, 64, 64)

    VE = VoxelEngine(custom_update=demo.update)

    # VE.scene.world.enable_demo(True)
    VE.run()


def render_3d_array(voxel_array: np.ndarray):
    """
      Render a 3D array of voxel data using the VoxelEngine.

      Args:
          voxel_array (numpy.ndarray): A 4D NumPy array, indexed by x,y,z coordinates, representing the voxel data (rgba).
    """
    app = VoxelEngine()

    app.step()

    len_x, len_y, len_z, len_channels = voxel_array.shape

    chunk_size = 32
    world_dims = (int(len_x / chunk_size) + 1, int(len_y / chunk_size) + 1, int(len_z / chunk_size) + 1)

    center_x = len_x / 2
    center_z = len_z / 2

    world_x = (8 * 32) / 2
    world_z = (8 * 32) / 2

    for x in range(len_x):
        for y in range(len_y):
            for z in range(len_z):
                voxel_value = voxel_array[x, y, z]
                red, green, blue, alpha = voxel_value

                color = (red * 255, green * 255, blue * 255)

                alpha = min(alpha * 255, 255)

                # Calculate the offset to center the voxel in the world
                offset_x = x - center_x

                offset_z = z - center_z

                # Calculate the world position for the voxel
                world_pos_x = world_x + offset_x
                world_pos_y = y + 5
                world_pos_z = world_z + offset_z

                world_pos = (world_pos_x, world_pos_y, world_pos_z)

                if alpha <= 25:
                    continue

                else:
                    app.scene.world.voxelManager.add_voxel(world_pos, color)
                # print(f"Placing voxel at {world_pos} with col: {color} and alpha {alpha}")

    app.run()
