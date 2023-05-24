# Control Net
***by. Haoming***

**Note:** ControlNet 1.1 has been released, bringing additional features and models!

## What is It
This is a suite of models that transfer features from one picture to another,
allowing you to have a specific pose, fix the hands, or create insanely creative results.

## Requirements
> Learn how to install [Extensions](../README.md#extensions)

1. Install the following Extension first and restart the webui:
    - `sd-webui-controlnet` *([GitHub](https://github.com/Mikubill/sd-webui-controlnet))*
2. Download the models of choice from this link:
    - [Hugging Face](https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main)
    - **Note:** Many tutorials were made for 1.0 and thus download the old models; refer to the official link above for the latest models.
    - ~~**Note:** You need to download both the `.pth` and the `.yaml` files of a model, and put them into `~\stable-diffusion-webui\extensions\sd-webui-controlnet\models`~~
      - The Extension now comes with the `.yaml` files. So just download the `.pth` files.

- **Important:** This extension requires different configs and models for `v1.5` and `v2.x` versions of Stable Diffusion. Refer to the official GitHub for the differences and settings.
> *(Refer to [versions](../README.md#sd-versions) if you don't know what this means.)*

## Video Tutorials
- [ControlNet 1.1](https://youtu.be/WZg3e6B2yPQ) by. **Sebastian Kamph**
- [ControlNet 1.1](https://youtu.be/zrGLEgGFJY4) by. **Olivio Sarikas**

#### Old Version
- [ControlNet Overview](https://youtu.be/ci7NfTsifd0) by. **Olivio Sarikas**
    - How to install *(Download the models from the link above instead)*
    - How to use
    - Brief explanation for each model 
- [Multi-ControlNet](https://youtu.be/MDHC7E6G1RA) by. **Aitrepreneur**
    - Using multiple models at the same time
    - Multiple technique showcases
- [Hands Depth Maps Library](https://youtu.be/EwWkLMhR23I) by. **Aitrepreneur**
    - Extension that provides OpenPose Editor inside webui
    - Extension that provides multiple DepthMaps for hands
- [Open Pose w/ Blender](https://youtu.be/ptEZQrKgHAg) by. **Aitrepreneur**
    - Generate OpenPose and DepthMap using `Blender`
- [Open Pose w/ Magic Poser](https://youtu.be/5z71oxf8kh4) by. **Aitrepreneur**
    - Yet another online editor for generating OpenPose and DepthMap 
- [Technical Explanations](https://youtu.be/fhIGt7QGg4w) by. **koiboi**
    - Original paper reading

## How to Use
There's simply too much to write in text easily. Just watch the videos above... 💀

Essentially,
1. Open ControlNet
2. Upload an image to extract features from
3. Pick a model depending on your need
4. Modify the values
5. ...
6. ~~Profit~~