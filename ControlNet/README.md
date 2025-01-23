<h1 align="center">ControlNet</h1>
<p align="center">
<b>by. Haoming</b><br>
<i>2025 Jan.</i>
</p>

## Introduction
**ControlNet** is a technique that transfers feature(s) from source image(s) to the Stable Diffusion pipeline, generating a specific pose, a particular scene, or other creative compositions.

## Requirements

1. For **Automatic1111** Webui, install the following Extension:
    - [sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet)

> [!TIP]
> Learn how to install [Extensions](../README.md#extensions)

> [!NOTE]
> For **Forge** Webui, the Extension is already built-in

2. Download the ControlNet Model(s) of choice:
    - For **SD1**, refer to the official [HuggingFace](https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main) for a list of all models
    - For **SDXL**, check out the [Union ProMax](https://huggingface.co/xinsir/controlnet-union-sdxl-1.0), which can process multiple modules in a single model
    - For **Flux**, check out the [Flux Collections](https://huggingface.co/XLabs-AI/flux-controlnet-collections)
    - A [list](https://github.com/Mikubill/sd-webui-controlnet/wiki/Model-download) of some other sources of models
    - Some models are also hosted on [CivitAI](https://civitai.com/tag/controlnet)

> [!TIP]
> See [Architecture](../README.md#architecture) if you don't know what the **versions** mean

> [!NOTE]
> You only need to download the `.pth` or `.safetensors` files <br>
> Put **ControlNet Models** in `~webui\models\ControlNet`

## How to Use
**ControlNet** contains has two parts: a **Preprocessor** responsible for **extracting** features from the source image; and a **Model** that takes these features then **injects** them into the pipeline.

<details>
<summary>Simple Explanation for various Modules</summary>

- **Canny:** Detect the edges within an image; useful for details; create a black image with white lines
- **Depth:** Detect the shapes within an image; useful for composition; create a greyscale image
- **OpenPose:** Detect the poses within an image; useful for actions; create a black image with colored stick figures
- **[IP-Adapter](https://huggingface.co/h94/IP-Adapter):** Useful for style transfer
- **[FaceID](https://huggingface.co/h94/IP-Adapter-FaceID):** Useful for faceswap
- **t.b.d**...

</details>

To get started, upload a source image, select a compatible pair of `Preprocessor` and `Model`, enable the Extension, then generate as usual.

> [!IMPORTANT]
> If you have an image that is already preprocessed *(**eg.** OpenPose mappings from various pose collections found online)*, you only need to pick the `Model`. Be sure to set the `Preprocessor` to **`None`**.

> [!TIP]
> After you upload a source image and pick a `Preprocessor`, you can click the `💥` button to generate a preview of the extracted features. Play around with the parameters if the desired features are not sufficient / apparent.

## Tutorials
- **[Video](https://youtu.be/WZg3e6B2yPQ)** by. <ins>Sebastian Kamph</ins>
- **[Video](https://youtu.be/zrGLEgGFJY4)** by. <ins>Olivio Sarikas</ins>
