import numpy as np

import renderer

if __name__ == "__main__":
    print("Load a voxel grid, perform basic operations, and render it.")

    voxel_grid = np.load("data.grid.npy")

    # Calculate grid density
    high_density_count = 0
    total_count = 0

    normalized = np.zeros_like(voxel_grid)

    # Loop through the voxel grid and accumulate the sums based on density values
    for dim_0 in range(voxel_grid.shape[0]):
        for dim_1 in range(voxel_grid.shape[1]):
            for dim_2 in range(voxel_grid.shape[2]):
                voxel = voxel_grid[dim_0, dim_1, dim_2]

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

                # Store the calculated values in the new_array at the same index position as voxel
                normalized[dim_0, dim_1, dim_2] = [red_norm, green_norm, blue_norm, RGRI, intensity]

    grid_density = (high_density_count / total_count) * 100

    print(f"Grid density: {grid_density:.2f}%")

    # Now, filter out voxels with low density (channel 4) by multiplying with a mask
    mask = voxel_grid[:, :, :, 4] > 0.5  # Create a mask for high-density voxels
    xyz_rgba_voxel_grid = normalized[:, :, :, [0, 1, 2]] * 255

    filtered_xyz_rgba_voxel_grid = xyz_rgba_voxel_grid * mask[..., np.newaxis]

    renderer.render_3d_array(filtered_xyz_rgba_voxel_grid)
