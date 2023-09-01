# Tiled Diffusion & VAE
***by. Haoming***

## Usage
When you use `Hires. fix` or `img2img` to upscale an image, you may encounter **CUDA Out of Memory Error** if the resolution is set too high.
You can solve this by using this extension to a degree.

## Requirements
> Learn how to install [Extensions](../README.md#extensions)

- Install the following Extension:
    - `MultiDiffusion with Tiled VAE (multidiffusion-upscaler-for-automatic1111)` *([Github](https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111))*

## How to Use
After you install the above extension, you should see a new sub-section down in the **txt2img** and **img2img** tabs.
Open the **Tiled VAE** section and **Enable** it. Adjust the `Tile Size` if needed.
Then, proceed to upscale as normal. 

> I was able to upscale a `1024x1024` image to `2048x2048` on a RTX 3070 Ti with only **8GB** of VRAM

This Extension also works with the **Tile Resample** module from [ControlNet](../ControlNet/README.md).
