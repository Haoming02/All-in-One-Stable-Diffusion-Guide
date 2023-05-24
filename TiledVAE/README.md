# Tiled Diffusion & VAE
***by. Haoming***

When you use `Hires. fix` or `img2img` to upscale an image, you may encounter **CUDA Out of Memory Error** if the resolution is too high.
You can solve this by using this extension.

## Requirements
> Learn how to install [Extensions](../README.md#extensions)

Install the following Extension first and restart the webui:
- `MultiDiffusion with Tiled VAE (multidiffusion-upscaler-for-automatic1111)` *([Github](https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111))*

## How to Use
After you install the above extension, you should see a new sub-section down in the **txt2img** and **img2img** tabs.
Open the **Tiled VAE** section and **Enable** it. Adjust the `Tile Size` if needed.

Then, proceed to upscale as normal. *I was able to upscale a `1024x1024` image to `2048x2048` with only **8GB** of VRAM.*

**Note:** You may need to lower the `CFG` and `Denoising strength` when upscaling in img2img.

## Example
[Nagase Mana](https://civitai.com/models/18659/nagase-mana-idoly-pride) generated at `512x512`, **Hires. fix** to `1024x1024`, then **img2img** to `2048x2048`. Maxinum VRAM used: `7GB`.

![Example](Upscale.jpg)

## Additional Info
- Alternatively, there is also [Ultimate SD Upscale](https://github.com/Coyote-A/ultimate-upscale-for-automatic1111). However in my experience, the script produces more visible seams in the generation compared to this extension.
- Both methods work with the **Tile Resample** model from [ControlNet](../ControlNet/README.md).