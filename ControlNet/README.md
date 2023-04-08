# Control Net
***by. Haoming 2023/04/06***

## What is It
This is a suite of models that transfer features from one picture to another,
allowing you to have a specific pose, fix the hands, or create insanely creative results.

## Requirements
> Learn how to install [Extensions](../README.md#extensions)

1. Install the following Extension first and restart the webui:
    - `sd-webui-controlnet` *([GitHub](https://github.com/Mikubill/sd-webui-controlnet))*
2. Download the models of choice from *this link*:
    - [Hugging Face](https://huggingface.co/webui/ControlNet-modules-safetensors/tree/main)
    - **Note:** Most tutorials download the original models that are around 5 GB each; the link above hosts the pruned models that are around 700 MB each instead. *There is no visual difference between the two*.
    - See what each model does in the first video tutorial below.

## Video Tutorials
- [ControlNet Overview](https://youtu.be/ci7NfTsifd0) by. **Olivio Sarikas**
    - How to install *(Download the models from the link above instead)*
    - How to use
    - Brief explanation for each model 
- [Multi-ControlNet](https://youtu.be/MDHC7E6G1RA) by. **Aitrepreneur**
    - Using multiple models at the same time
    - Multiple technique showcases
- [Hands Depth Maps Library](https://youtu.be/EwWkLMhR23I) by. **Aitrepreneur**
    - Extension that provides OpenPose Editor inside webui
    - Extension that provides multiple depth maps for hands
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
3. Pick a model depending on your usecase
4. Modify the values
5. ...
6. Profit