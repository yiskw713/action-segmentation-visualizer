import os

import pytest
from PIL import Image

from vis_action_seg import visualize

TEST_DIR = os.path.dirname(__file__)


def test_visualize():
    action_list = []
    for i in range(10):
        action_list += [i] * 50

    result = visualize(action_list=action_list)

    expected = Image.open(os.path.join(TEST_DIR, "samples", "vis.png"))
    expected = expected.convert("P")

    assert result == expected
