<h1 align="center">ControlNet</h1>
<p align="center"><b>by. Haoming</b></p>

## Introduction
**ControlNet** is a technique that allows you to transfer features from source image(s) to the Stable Diffusion pipeline, generating a specific pose, a particular scene, or other creative compositions.

## Requirements

> [!NOTE]
> For **Forge** Webui, the Extension is already built-in

1. For **Automatic1111** Webui, install the following Extension:
    - [sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet)

> [!TIP]
> Learn how to install [Extensions](../README.md#extensions)

2. Download the model(s) of choice:
    - For **SD1**, refer to the official [HuggingFace](https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main) for a list of all models
    - For **SDXL**, check out the [Union ProMax](https://huggingface.co/xinsir/controlnet-union-sdxl-1.0), which can process multiple modules in a single model
    - For **Flux**, check out the [Flux Collections](https://huggingface.co/XLabs-AI/flux-controlnet-collections)
    - A [list](https://github.com/Mikubill/sd-webui-controlnet/wiki/Model-download) of some other sources of models

> [!TIP]
> See [Architecture](../README.md#architecture) if you don't know what the **versions** mean

> [!NOTE]
> You only need to download the `.pth` or `.safetensors` files <br>
> Put **ControlNet Models** in `~webui\models\ControlNet`

## How to Use
The **ControlNet** Extension basically has two parts: the **Preprocessor** and the **Model**. The Preprocessor is responsible for extracting features from your source image. For example, an `OpenPose` module will create colorful stick figures, while a `Depth` module will produce a greyscale depth map. The Model then takes these features and injects them into the pipeline. To get started, simply upload a source image, select a compatible pair of Preprocessor and Model, enable the Extension, then generate as normal.

> [!TIP]
> After you upload a source image and pick a Preprocessor, you can click the `💥` button to generate a preview of the extracted features. Play around with the parameters if the features are not sufficient.

> [!IMPORTANT]
> If you have an image that is already preprocessed *(**eg.** an image with white outlines and black background)*, you only need to pick the Model *(`Canny` in this example)*. Be sure to set the Preprocessor to **`None`**.

## Tutorials
- **[Video](https://youtu.be/WZg3e6B2yPQ)** by. <ins>Sebastian Kamph</ins>
- **[Video](https://youtu.be/zrGLEgGFJY4)** by. <ins>Olivio Sarikas</ins>
