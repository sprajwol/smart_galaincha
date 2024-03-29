import numpy as np
import matplotlib.pyplot as plt
from .convolution import convolution


def sobel_edge_detection(image, filter, convert_to_degree=False):
    new_image_x = convolution(image, filter)

    new_image_y = convolution(image, np.flip(filter.T, axis=0))

    gradient_magnitude = np.sqrt(
        np.square(new_image_x) + np.square(new_image_y))

    gradient_magnitude *= 255.0 / gradient_magnitude.max()

    gradient_direction = np.arctan2(new_image_y, new_image_x)

    if convert_to_degree:
        gradient_direction = np.rad2deg(gradient_direction)
        gradient_direction += 180

    return gradient_magnitude, gradient_direction
