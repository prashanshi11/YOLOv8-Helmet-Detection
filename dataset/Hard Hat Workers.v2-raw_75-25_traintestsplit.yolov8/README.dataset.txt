# Hard Hat Workers > raw_75-25_trainTestSplit
https://universe.roboflow.com/joseph-nelson/hard-hat-workers

Provided by [Northeastern University - China](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/7CBGOS)
License: Public Domain

# Overview

The `Hard Hat` dataset is an object detection dataset of workers in workplace settings that require a hard hat. Annotations also include examples of just "person" and "head," for when an individual may be present without a hard hart.

The original dataset has a [75/25 train-test split](https://blog.roboflow.com/train-test-split/).

Example Image:
![Example Image](https://i.imgur.com/7spoIJT.png)

# Use Cases

One could use this dataset to, for example, build a classifier of workers that are abiding safety code within a workplace versus those that may not be. It is also a good general dataset for practice.

# Using this Dataset

Use the `fork` or `Download this Dataset` button to copy this dataset to your own Roboflow account and export it with new preprocessing settings (perhaps resized for your model's desired format or converted to grayscale), or additional augmentations to make your model generalize better. This particular dataset would be very well suited for Roboflow's new advanced [Bounding Box Only Augmentations](https://blog.roboflow.ai/introducing-bounding-box-level-augmentations/).

## Dataset [Versions](https://help.roboflow.com/workspaces-projects-and-versions):
[Image Preprocessing](https://docs.roboflow.com/image-transformations/image-preprocessing) | [Image Augmentation](https://docs.roboflow.com/image-transformations/image-augmentation) | [Modify Classes](https://help.roboflow.com/modifying-classes)
* `v1` (resize-416x416-reflect): generated with the original 75/25 train-test split | No augmentations
* **`v2` (raw_75-25_trainTestSplit)**: generated with the original 75/25 train-test split | **These are the raw, original images**
* `v3` (v3): generated with the original 75/25 train-test split | Modify Classes used to drop `person` class | Preprocessing and Augmentation applied
* `v5` (raw_HeadHelmetClasses): generated with a 70/20/10 train/valid/test split | Modify Classes used to drop `person` class
* `v8` (raw_HelmetClassOnly): generated with a 70/20/10 train/valid/test split | Modify Classes used to drop `head` and `person` classes
* `v9` (raw_PersonClassOnly): generated with a 70/20/10 train/valid/test split | Modify Classes used to drop `head` and `helmet` classes
* **`v10` (raw_AllClasses)**: generated with a 70/20/10 train/valid/test split | **These are the raw, original images**
* **`v11` (augmented3x-AllClasses-FastModel)**: generated with a 70/20/10 train/valid/test split | Preprocessing and Augmentation applied | 3x image generation | *Trained with Roboflow's Fast Model*
* **`v12` (augmented3x-HeadHelmetClasses-FastModel)**: generated with a 70/20/10 train/valid/test split | Preprocessing and Augmentation applied, Modify Classes used to drop `person` class | 3x image generation | *Trained with Roboflow's Fast Model*
* **`v13` (augmented3x-HeadHelmetClasses-AccurateModel)**: generated with a 70/20/10 train/valid/test split | Preprocessing and Augmentation applied, Modify Classes used to drop `person` class | 3x image generation | *Trained with Roboflow's Accurate Model*
* `v14` (raw_HeadClassOnly): generated with a 70/20/10 train/valid/test split | Modify Classes used to drop `person` class, and remap/relabel `helmet` class to `head`

[Choosing Between Computer Vision Model Sizes](https://blog.roboflow.com/computer-vision-model-tradeoff/) | [Roboflow Train](https://docs.roboflow.com/train)

# About Roboflow

[Roboflow](https://roboflow.ai) makes managing, preprocessing, augmenting, and versioning datasets for computer vision seamless.

Developers reduce 50% of their code when using Roboflow's workflow, automate annotation quality assurance, save training time, and increase model reproducibility.

#### [![Roboflow Workmark](https://i.imgur.com/WHFqYSJ.png =350x)](https://roboflow.ai)