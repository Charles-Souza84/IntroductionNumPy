import numpy as np
import matplotlib.pyplot as plt

# rgb_array_npy contém uma imagem em RGB que será utilizada como base abaixo
# Display the documentation for .astype()
# help(np.ndarray.astype)

with open("rgb_array.npy", "rb") as f:
    rgb_array = np.load(f)
"""

# Reduce every value in rgb_array by 50 percent
darker_rgb_array = rgb_array * 0.5

# Convert darker_rgb_array into an array of integers
darker_rgb_int_array = darker_rgb_array.astype(np.int8)
plt.imshow(darker_rgb_int_array)
plt.show()

# Save darker_rgb_int_array to an .npy file called darker_monet.npy
with open("darker_monet.npy", "wb") as f:
    np.save(f, darker_rgb_int_array)

# trabalhando com flipping e transposing
# a parte mais difícil em flipping é encontrar o eixo correto

# Flip rgb_array so that it is the mirror image of the original
mirrored_monet = np.flip(rgb_array, axis=1)
plt.imshow(mirrored_monet)
plt.show()
# Flip rgb_array so that it is upside down
upside_down_monet = np.flip(rgb_array, axis=(0,1))
plt.imshow(upside_down_monet)
plt.show()

# Transpose rgb_array
transposed_rgb = np.transpose(rgb_array, axes = (1,0,2))
plt.imshow(transposed_rgb)
plt.show()

"""
# trabalhando com dimensões de array
# Split rgb_array into red, green, and blue arrays
red_array, green_array, blue_array = np.split(rgb_array, 3, axis=2)

# Create emphasized_blue_array
emphasized_blue_array = np.where(blue_array > blue_array.mean(), 255, blue_array)

# Print the shape of emphasized_blue_array
print(emphasized_blue_array.shape)

# Remove the trailing dimension from emphasized_blue_array
emphasized_blue_array_2D = emphasized_blue_array.reshape((675, 843))

# Print the shapes of blue_array and emphasized_blue_array_2D
print(blue_array.shape, emphasized_blue_array_2D.shape)

# Reshape red_array and green_array
red_array_2D = red_array.reshape((675, 843))
green_array_2D = green_array.reshape((675, 843))

# Stack red_array_2D, green_array_2D, and emphasized_blue_array_2D
emphasized_blue_monet = np.stack([red_array_2D, green_array_2D, emphasized_blue_array_2D], axis=2)
plt.imshow(emphasized_blue_monet)
plt.show()

# com isso a imagem ficou com a cor azul mais acentuada onde já havia uma concentração maior desta cor.