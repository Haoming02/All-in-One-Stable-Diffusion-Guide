<h1 align="center">Installation Guide</h1>
<p align="center"><b>for AUTOMATIC1111 Webui</b></p>
<p align="center"><b>by. Haoming</b><br><i>Last Update: 2023/08/30</i></p>

## Installation
- It's highly recommended to install on **SSD** instead of HDD, so that loading models will only take seconds instead of minutes.
- *For Apple Silicon, refer to [this](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon) instead.*

<details>
<summary>Simplified</summary>

1. Go to this [link](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases/tag/v1.0.0-pre)
2. Click on **`sd.webui.zip`** to download
3. Extract its contents to a folder of choice
4. Run **`update.bat`** first
5. Run **`run.bat`** 
    - When you launch it for the first time, it will download and install all the requirements. This will take a while so be patient. ~~Read the rest of the guide in the meantime~~.
6. You will know it's finished loading when you see **`Running on local URL:  http://127.0.0.1:XXXX`**
</details>

<details>
<summary>Detailed (for Tech-Savvy)</summary>

0. Install `CUDA Toolkit 11.8` *(`12.x` is **not** supported)*
1. Install `Python 3.10.x` *(`3.11.x` is **not** supported)*
    - Remember to enable **`Add python.exe to PATH`**
2. Install `git`
3. `git` `clone` https://github.com/AUTOMATIC1111/stable-diffusion-webui
4. Run **`webui-user.bat`** 
    - When you launch it for the first time, it will download and install all the requirements. This will take a while so be patient. ~~Read the rest of the guide in the meantime~~.
5. You will know it's finished loading when you see **`Running on local URL:  http://127.0.0.1:XXXX`**
</details>

## COMMANDLINE ARGS
Go to the installation folder *(`webui` folder for the Simplified version)*, right click the file `webui-user.bat` and press `Edit`.
Then you can add the following *(optional)* arguments after **`COMMANDLINE_ARGS=`**
- **`--xformers`** to speed up the generation and reduce memory consumption
- **`--medvram`** if you have less than **8GB** VRAM
    - **`--lowvram`** instead if you're still getting **CUDA Out of Memory Error**
    - (v1.6) **`--medvram-sdxl`** to only activate it when using SDXL checkpoints

#### Advanced
- **`--api`** allows other programs to talk to it. See the official [Documentation](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API) for more info.
- **`--port XXXX`** specifies which local port to use.

> See all Commandline Args [Here](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings)
