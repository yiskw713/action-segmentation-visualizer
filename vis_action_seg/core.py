from __future__ import annotations

import os
from typing import Optional

import numpy as np
from PIL import Image

from .palette import PALETTE


def visualize(
    action_list: list[int],
    save_path: Optional[str] = None,
    image_height: int = 100,
    palette: list[int] = PALETTE,
) -> Image.Image:
    """Visualize action segmentation result (and save it if necessary).

    Args:
        action_list (list[int]):
            List containing action class id like [1, 1, 1, 0, 0, 2, 2, ....]
        save_path (Optional[str]):
            If `save_path` is given, the visualized image will be save at `save_path`.
        image_height (int, optional):
            The height of visualized image. Defaults to 100.
            Note that the width depends on the length of `action_list`.
        palette (list[int]):
            Color palette. Default to `PALETTE`, which are obtained from PascalVOC.

    Returns:
        Image.Image:
    """
    # convert to 2D array.
    array = np.array(action_list, dtype=np.uint8)
    array = np.tile(array, reps=(image_height, 1))

    # convert to an image using color palette.
    image = Image.fromarray(array)
    image = image.convert("P")
    image.putpalette(palette)

    if save_path is not None:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        image.save(save_path)

    return image
