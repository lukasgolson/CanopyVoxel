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
    app = VoxelEngine(voxel_array=voxel_array)

    app.run()
