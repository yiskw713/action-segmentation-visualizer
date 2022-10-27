# Action Segmentation Visualizer

Visualizing action segmentation results using PascalVOC color palette.

## Install

Please run the below command.

```sh
pip install git+https://github.com/yiskw713/action-segmentation-visualizer.git
```

## Usage

```python
from vis_action_seg import visualize


# `action_list` contains action class ids for each frame.
action_list = [0, 0, 0, 0, 1, 1, 1, 1, 1]

visualize(
    action_list,
    save_path="./sample.png",  # if `save_path` is given, the image will be saved there.
    image_height=100,  # the height of output image.
)
```

You can also use the custom color palette.
For more details, please see `vis_action_seg/core.py`.

## Visualization sample

![](tests/samples/vis.png)
