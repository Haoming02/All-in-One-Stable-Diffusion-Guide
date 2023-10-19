# TensorRT
***by. Haoming***

## Prerequisite
- **Nvidia** RTX GPU

## Getting Started
1. Install the latest [driver](https://www.nvidia.com/download/index.aspx) *(`v545`+)*
2. Activate the Python virtual environment
    1. Go to your webui installation folder *(you should see a `venv` folder there)*
    2. Type `cmd` in the address bar to open the console in the current folder
    3. Type `venv\scripts\activate`
    4. You should see the console now starts with `(venv)`
3. Enter the following one by one:
    ```py
    python -m pip install --upgrade pip
    python -m pip install nvidia-cudnn-cu11==8.9.4.25 --no-cache-dir
    python -m pip install --pre --extra-index-url https://pypi.nvidia.com/ tensorrt==9.0.1.post11.dev4 --no-cache-dir
    python -m pip uninstall -y nvidia-cudnn-cu11
    ```
4. Launch the webui
5. Install the following Extension:
    - `Stable-Diffusion-WebUI-TensorRT` *([GitHub](https://github.com/NVIDIA/Stable-Diffusion-WebUI-TensorRT))*
    > Learn how to install [Extensions](../README.md#extensions)
6. After restarting the webui, you should now see a **TensorRT** tab
7. You can then press the *big orange button* to generate an optimized engine
8. The conversion took ~3min on RTX 3060
9. After the conversion is finished, go to **Settings** -> **User Interface**, and add `sd_unet` to `Quick Settings`, then restart the webui
10. Now you can choose the **[TRT]** Unet to enjoy the speed!
    - It went from `~7 it/s` to `~15 it/s` on RTX 3060

## Note
- The optimized engine only works on the specified resolution
- You can select between presets from the dropdown, or manually enter the resolution and batch size to optimize
- If you want to use `Hires. fix`, you need to set the resolution to dynamic between the original and the upscaled resolution
- LoRA has to be baked in separately
- `--medvram` apparently causes problems
