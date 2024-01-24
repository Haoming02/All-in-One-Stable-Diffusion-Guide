<h1 align="center">Installation Guide</h1>
<p align="center">for <b>AUTOMATIC1111 Webui</b> (on Windows)</p>
<p align="center"><b>by. Haoming</b><br><i>Last Update: 2024/01/24</i></p>

## Installation
It's highly recommended to install on a **SSD** instead of a HDD
> For **Apple Silicon**, refer to this [Tutorial](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon) page

> For **AMD GPU**, refer to the [DirectML](https://github.com/lshqqytiger/stable-diffusion-webui-directml) page

1. Go to the [Release](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases/tag/v1.0.0-pre) page
2. Click on **`sd.webui.zip`** to download
3. Extract all its contents *(2x folders and 3x `.bat` files)* to a folder of choice
4. Run **`update.bat`**
5. Modify the [commandline args](#commandline-args) as mentioned below
6. Run **`run.bat`** 
    - When you launch it for the first time, it will download and install all the requirements. This will take a while so be patient. ~~Read the rest of the guide in the meantime~~.
7. You will know it's finished loading when you see **`Running on local URL:  http://127.0.0.1:XXXX`**

<details>
<summary>(for the Tech-Savvy)</summary>

If you don't want to use the self-contained release, follow these steps instead:

0. Install `CUDA Toolkit 11.8` *(`12.x` is not officially supported)*
1. Install `Python 3.10.x` *(`3.11.x` or later is **not** supported currently)*
    - Remember to enable **`Add python.exe to PATH`**
2. Install `git`
3. Run
    ```bash
    git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
    ```
4. Modify the [commandline args](#commandline-args) as mentioned below
5. Run **`webui-user.bat`** 
6. You will know it's finished loading when you see **`Running on local URL:  http://127.0.0.1:XXXX`**
</details>

## COMMANDLINE ARGS
Now, go to the `webui` folder, right click the file `webui-user.bat` and press `Edit`.
> Enable **Show > File name extensions** if you can't find this file

Then you can add the following *(optional)* arguments after the **`COMMANDLINE_ARGS=`** line
- **`--xformers`** to speed up the generation and reduce memory consumption
- **`--medvram-sdxl`** if you have less than **12 GB** VRAM, but wish to use **SDXL** checkpoints
- **`--medvram`** if you have less than **8 GB** VRAM
    - **`--lowvram`** instead if you're still getting **CUDA Out of Memory Error**

### Advanced
- **`--api`** allows other programs to interact with the Webui. See the official [Documentation](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API) for more info.
- **`--port XXXX`** specifies which local port to use.

> See all available Commandline Args [Here](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings)
