"""
Create the final statistics meme by assembling all four panels.
This function creates a professional-looking 1×4 layout showing:
- Reality (original image)
- Your Model (stippled image)
- Selection Bias (block letter)
- Estimate (masked stippled image)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec


def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white"
) -> None:
    """
    Assemble all four panels into a professional-looking statistics meme.
    
    Parameters
    ----------
    original_img : np.ndarray
        Original grayscale image (2D array with values in [0, 1])
    stipple_img : np.ndarray
        Stippled image pattern (2D array with values in [0, 1])
    block_letter_img : np.ndarray
        Block letter "S" image (2D array with values in [0, 1])
    masked_stipple_img : np.ndarray
        Masked stippled image (2D array with values in [0, 1])
    output_path : str
        Path where the final meme PNG will be saved
    dpi : int
        Resolution (dots per inch) for the output image. Default 150.
    background_color : str
        Background color for the figure. Default "white".
        Can be any matplotlib color name or hex code.
    
    Returns
    -------
    None
        Saves the meme to output_path
    """
    # Panel labels
    labels = ["Reality", "Your Model", "Selection Bias", "Estimate"]
    
    # Images to display
    images = [original_img, stipple_img, block_letter_img, masked_stipple_img]
    
    # Determine the size of images (they should all be the same, but handle differences)
    heights = [img.shape[0] for img in images]
    widths = [img.shape[1] for img in images]
    
    # Use the maximum dimensions to ensure all panels fit
    max_height = max(heights)
    max_width = max(widths)
    
    # Create figure with 1 row and 4 columns
    # Use GridSpec for better control over spacing
    fig = plt.figure(figsize=(16, 4), facecolor=background_color)
    gs = gridspec.GridSpec(1, 4, figure=fig, wspace=0.1, hspace=0.1,
                          left=0.05, right=0.95, top=0.9, bottom=0.1)
    
    # Create subplots and display images
    for i, (img, label) in enumerate(zip(images, labels)):
        ax = fig.add_subplot(gs[0, i])
        
        # Display the image
        # Handle different value ranges: if values are in [0, 1], use grayscale colormap
        # If values are binary (0.0 and 1.0), also use grayscale
        ax.imshow(img, cmap='gray', vmin=0, vmax=1, aspect='auto')
        
        # Remove axes for cleaner look
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
        # Add label above the panel
        ax.set_title(label, fontsize=14, fontweight='bold', pad=10)
    
    # Add overall title if desired (optional)
    # fig.suptitle("Selection Bias in Statistics", fontsize=16, fontweight='bold', y=0.98)
    
    # Save the figure
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', 
                facecolor=background_color, edgecolor='none')
    plt.close()
    
    print(f"Statistics meme saved to: {output_path}")
    print(f"Image dimensions: {max_width}×{max_height} pixels per panel")
    print(f"Output DPI: {dpi}")

