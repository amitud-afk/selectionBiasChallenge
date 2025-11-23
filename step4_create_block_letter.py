"""
Step 4: Create a block letter "S" matching image dimensions.
Generates a block letter that can be used as a mask for the selection bias meme.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_block_letter_s(
    height: int,
    width: int,
    letter: str = "S",
    font_size_ratio: float = 0.9
) -> np.ndarray:
    """
    Create a block letter (default "S") matching the specified image dimensions.
    The letter is rendered as black (0.0) on a white background (1.0).
    
    Parameters
    ----------
    height : int
        Height of the output image in pixels
    width : int
        Width of the output image in pixels
    letter : str
        Letter to render. Default "S".
    font_size_ratio : float
        Ratio of font size to image height. Default 0.9 (letter will be 90% of image height).
    
    Returns
    -------
    block_letter : np.ndarray
        2D array (height, width) with values in [0, 1]
        Letter is black (0.0), background is white (1.0)
    """
    # Create a white image (background) using PIL.Image
    img = Image.new('L', (width, height), color=255)
    
    # Create ImageDraw object to draw on the image
    draw = ImageDraw.Draw(img)
    
    # Calculate font size based on image height
    font_size = int(height * font_size_ratio)
    
    # Try to load a bold font, fallback to default if not available
    try:
        # Try common system font paths for bold fonts
        font_paths = [
            '/System/Library/Fonts/Supplemental/Arial Bold.ttf',  # macOS
            '/System/Library/Fonts/Helvetica.ttc',  # macOS (may need to specify face)
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',  # Linux
            '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',  # Linux
            'C:/Windows/Fonts/arialbd.ttf',  # Windows
        ]
        font = None
        for font_path in font_paths:
            try:
                font = ImageFont.truetype(font_path, font_size)
                break
            except (OSError, IOError):
                continue
        
        # If no system font found, try to use default font with size
        if font is None:
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except (OSError, IOError):
                # Fallback to default font
                font = ImageFont.load_default()
    except Exception:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Get text bounding box to center the letter using PIL.ImageDraw
    bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate position to center the letter
    x = (width - text_width) // 2 - bbox[0]
    y = (height - text_height) // 2 - bbox[1]
    
    # Draw the letter "S" in black (0) using PIL.ImageDraw.text()
    draw.text((x, y), letter, fill=0, font=font)
    
    # Convert PIL image to numpy array and normalize to [0, 1]
    block_letter = np.array(img, dtype=np.float32) / 255.0
    
    # Invert so letter is black (0.0) and background is white (1.0)
    # Since we drew with fill=0 (black) on white background (255),
    # after normalization: letter pixels are 0.0, background is 1.0
    # This is already correct, but let's ensure it
    # Actually, we want letter to be 0.0 (black) and background 1.0 (white)
    # After normalization: 0/255 = 0.0 (black), 255/255 = 1.0 (white) ✓
    
    print(f"Created block letter '{letter}' with dimensions: {block_letter.shape}")
    print(f"Letter pixels (black): {np.sum(block_letter == 0.0)}")
    print(f"Background pixels (white): {np.sum(block_letter == 1.0)}")
    
    return block_letter

