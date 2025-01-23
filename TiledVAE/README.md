<h1 align="center">Tiled VAE</h1>
<p align="center">
<b>by. Haoming</b><br>
<i>2025 Jan.</i>
</p>

## Introduction
When you use `Hires. fix` or `img2img` to upscale an image, you may encounter **CUDA Out of Memory Error** if the memory required by the resolution exceeds what your VRAM can handle. Typically, this happens during the VAE decoding stage *(**ie.** at the end of a generation)*.

This issue can be solved using this Extension by only processing a small tile of the image at a time then merging them together afterwards.

> [!TIP]
> This Extension works well with the **Tile** module of [ControlNet](../ControlNet/README.md)

## Requirements

- For **Automatic1111** Webui, install the following Extension:
    - [multidiffusion-upscaler-for-automatic1111](https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111)

> [!TIP]
> Learn how to install [Extensions](../README.md#extensions)

> [!NOTE]
> For **Forge** Webui, the Extension is already built-in *(called **Never OOM**)*
