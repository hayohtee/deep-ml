import numpy as np


def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    match norm_type:
        case "l1":
            return np.float32(np.sum(np.abs(arr)))
        case "l2":
            return np.sqrt(np.sum(arr**2))
        case "linf":
            return np.float32(np.max(np.abs(arr)))
        case "frobenius":
            if arr.ndim != 2:
                raise ValueError("Frobenius norm is only defined for 2D arrays.")
            return np.sqrt(np.sum(arr.flatten() ** 2))
        case _:
            raise ValueError(f"Unsupported norm type: {norm_type}. Supported types are 'l1', 'l2', 'linf', and 'frobenius'.")
