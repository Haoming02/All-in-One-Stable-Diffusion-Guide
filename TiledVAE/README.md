<h1 align="center">MultiDiffusion & TiledVAE</h1>
<p align="center"><b>by. Haoming</b></p>

## Introduction
When you use `Hires. fix` or `img2img` to upscale an image, you may encounter **CUDA Out of Memory Error** if the resolution exceeds what your VRAM can handle. This can be solved via this Extension by only processing a small tile of the image at a time then merging them at the end.

> [!TIP]
> This Extension works well with the **Tile Resample** module from [ControlNet](../ControlNet/README.md)

## Requirements

> [!NOTE]
> For **Forge** Webui, the Extension is already built-in

- For **Automatic1111** Webui, install the following Extension:
    - [multidiffusion-upscaler-for-automatic1111](https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111)

> [!TIP]
> Learn how to install [Extensions](../README.md#extensions)
