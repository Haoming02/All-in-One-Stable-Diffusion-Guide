# Multi Diffusion
***by. Haoming 2023/05/11***

When you use `Hires. fix` or `img2img` to upscale an image, you may encounter **CUDA Out of Memory Error** if the resolution is too high.
You can solve this by installing this extension:

## Requirements
> Learn how to install [Extensions](../README.md#extensions)
- `MultiDiffusion with Tiled VAE (multidiffusion-upscaler-for-automatic1111)` *([Github](https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111))*

## How to Use
After you install the above extension, you should see a new sub-section down in the **txt2img** and **img2img** tabs.
Open the **Tiled VAE** section and **Enable** it. Adjust the `Tile Size` if needed.

Then, proceed to upscale as normal. *I was able to upscale a `1024x1024` image to `2048x2048` with only **8GB** of VRAM.*

**Note:** For **img2img**, you need to lower the `CFG` *(~4)* and `Denoising strength` *(~0.4)* 

## Example
[Nagase Mana](https://civitai.com/models/18659/nagase-mana-idoly-pride) generated at `512x512`, **Hires. fix** to `1024x1024`, then **img2img** to `2048x2048`. Maxinum VRAM used: **7GB**.

![Example](Upscale.jpg)

## Additional Info
- Alternatively, there is also [Ultimate SD Upscale](https://github.com/Coyote-A/ultimate-upscale-for-automatic1111). However in my experience, this extension produces more visible seams in the generation.
- Both Extensions work great along with the **Tile Resample** [ControlNet](../ControlNet/README.md) model.