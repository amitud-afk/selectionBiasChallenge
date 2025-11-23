"""
Step 5: Apply block letter mask to stippled image.
Creates a masked version where stipples are removed in the mask area,
demonstrating selection bias by systematically removing data points.
"""

import numpy as np


def create_masked_stipple(
    stipple_img: np.ndarray,
    mask_img: np.ndarray,
    threshold: float = 0.5
) -> np.ndarray:
    """
    Apply a block letter mask to a stippled image.
    Where the mask is dark (below threshold), stipples are removed (set to white).
    Where the mask is light (above threshold), stipples are kept as they are.
    This creates the "biased estimate" by systematically removing data points.
    
    Parameters
    ----------
    stipple_img : np.ndarray
        Stippled image as 2D array (height, width) with values in [0, 1]
        where 0.0 = black stipple dots, 1.0 = white background
    mask_img : np.ndarray
        Mask image as 2D array (height, width) with values in [0, 1]
        where 0.0 = black (mask area), 1.0 = white (keep area)
    threshold : float
        Threshold value to determine what counts as "part of the mask".
        Pixels below this threshold are considered part of the mask and will
        have stipples removed. Default 0.5.
    
    Returns
    -------
    masked_stipple : np.ndarray
        2D array (height, width) with values in [0, 1]
        Same shape as input images. Stipples are removed in mask areas.
    """
    # Ensure both images have the same shape
    if stipple_img.shape != mask_img.shape:
        raise ValueError(
            f"Image shapes must match: stipple_img {stipple_img.shape} != "
            f"mask_img {mask_img.shape}"
        )
    
    # Create masked stipple: where mask is dark (below threshold), remove stipples
    # Where mask is light (above threshold), keep stipples as they are
    masked_stipple = np.where(mask_img < threshold, 1.0, stipple_img)
    
    # Count statistics
    mask_area = np.sum(mask_img < threshold)
    removed_stipples = np.sum((mask_img < threshold) & (stipple_img == 0.0))
    remaining_stipples = np.sum((mask_img >= threshold) & (stipple_img == 0.0))
    
    print(f"Applied mask to stippled image")
    print(f"Mask area (pixels below threshold {threshold}): {mask_area}")
    print(f"Stipples removed in mask area: {removed_stipples}")
    print(f"Stipples remaining in non-mask area: {remaining_stipples}")
    print(f"Total stipples in original: {np.sum(stipple_img == 0.0)}")
    print(f"Total stipples in masked: {np.sum(masked_stipple == 0.0)}")
    
    return masked_stipple

