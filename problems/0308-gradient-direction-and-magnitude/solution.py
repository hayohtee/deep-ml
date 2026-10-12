import numpy as np


def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.

    Args:
            gradient: A list representing the gradient vector

    Returns:
            Dictionary containing:
            - magnitude: The L2 norm of the gradient
            - direction: Unit vector in direction of steepest ascent
            - descent_direction: Unit vector in direction of steepest descent
    """
    magnitude = np.linalg.norm(gradient)
    if magnitude != 0:
        direction = np.array(gradient) / magnitude
        descent_direction = -direction
    else:
        direction = np.zeros(len(gradient))
        descent_direction = np.zeros(len(gradient))

    return {
        "magnitude": magnitude,
        "direction": direction.tolist(),
        "descent_direction": descent_direction.tolist(),
    }