import numpy as np

import renderer

if __name__ == "__main__":
    print("Load a voxel grid, perform basic operations, and render it.")

    voxel_grid = np.load("data.grid.npy")

    # Calculate grid density
    high_density_count = 0
    total_count = 0

    new_array = np.zeros_like(voxel_grid)

    # Loop through the voxel grid and accumulate the sums based on density values
    for voxel in voxel_grid.reshape(-1, 5):
        red = voxel[0]
        green = voxel[1]
        blue = voxel[2]

        intensity = red + green + blue
        intensity_norm = intensity / (255 * 3)

        if intensity != 0:
            red_norm = red / intensity
            green_norm = green / intensity
            blue_norm = blue / intensity
        else:
            red_norm = 0
            green_norm = 0
            blue_norm = 0

        RGRI = red_norm / (green_norm + 0.0000001)

        density = voxel[4]

        if density > 0:
            total_count += 1
        if density > 0.5:
            high_density_count += 1

    grid_density = (high_density_count / total_count) * 100

    print(f"Grid density: {grid_density:.2f}%")

    xyz_rgba_voxel_grid = voxel_grid[:, :, :, [0, 1, 2, 4]]

    renderer.render_3d_array(xyz_rgba_voxel_grid)
