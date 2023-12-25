# TensorRT
***by. Haoming***

## Prerequisite
- Nvidia **RTX** GPU

## Getting Started

1. Install the latest [driver](https://www.nvidia.com/download/index.aspx) *(`v545`+)*
2. Activate the Python virtual environment
3. Enter the following one by one:
    ```bash
    python -m pip install nvidia-cudnn-cu11==8.9.4.25 --no-cache-dir
    python -m pip install --pre --extra-index-url https://pypi.nvidia.com/ tensorrt==9.0.1.post11.dev4 --no-cache-dir
    python -m pip uninstall -y nvidia-cudnn-cu11
    ```
4. Launch the Webui

> Learn how to install [Extensions](../README.md#extensions)

5. Install the following Extension:
    - `Stable-Diffusion-WebUI-TensorRT` *([GitHub](https://github.com/NVIDIA/Stable-Diffusion-WebUI-TensorRT))*
6. After restarting the webui, you should now see a **TensorRT** tab
7. **(Optionally)** Select and modify a preset
8. Then, press the **Export Default Engine** button to generate an optimized engine
    - The conversion took ~3min on RTX 3060
9. After the conversion is finished, go to **Settings** -> **User Interface**, and add **`sd_unet`** to the **`Quicksettings list`**, then restart the webui
10. Now you can choose the **[TRT]** Unet to enjoy the speed!
    - It went from `~7 it/s` to `~15 it/s` on RTX 3060

## Note
- The optimized engine only works on the specified resolution, batch size, and token count
- If you want to use `Hires. fix`, you need to export a **dynamic** engine, with the resolution set to cover the original and the upscaled resolution
- LoRA has to be baked in separately *(Not Recommended)*
