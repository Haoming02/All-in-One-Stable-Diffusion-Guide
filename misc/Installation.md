<h1 align="center">Installation Guide</h1>
<p align="center"><b>by. Haoming</b></p>
<p align="right"><i>for <b>Automatic1111</b> / <b>Forge</b> Webui<br>(on Windows)</i></p>

### Preface
It's highly recommended to install on a **SSD** instead of a HDD

> For **Apple Silicon**, refer to this [Tutorial](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon) page

> For **AMD GPU**, refer to the [AMD GPU](https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu) repo

### Download
- for **Automatic1111**
    1. Go to the [Release](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases/tag/v1.0.0-pre) page
    2. Click on **`sd.webui.zip`** to download
- for **Forge**
    1. Go to the [Release](https://github.com/lllyasviel/stable-diffusion-webui-forge/releases/tag/latest) page
    2. Click on **`webui_forge_cu121_torch21.7z`** to download

### Installation
1. Extract all contents *(2x folders and 3x files)* to a folder of choice
    - Do **not** put them in `OneDrive` or other cloud drives...
2. Run **`update.bat`**
3. **(for Automatic1111)** Modify the [commandline args](#commandline-args) as mentioned below
4. Download a **checkpoint** of choice first. Otherwise, it will automatically download the low-quality base checkpoint...
    - Refer to [Checkpoint](../README.md#checkpoint) if you don't know what these mean
5. Run **`run.bat`**
    - When you launch the Webui for the first time, it will download and install all the required packages
    - This will take some time so be patient
    - ~~Read the rest of the guide in the meantime~~
6. You will know the installation is finished when a browser window opens with the UI loaded

#### COMMANDLINE ARGS

> These memory-related args are only needed on Automatic1111; Forge handles them for you

Inside the `webui` folder, right click the file `webui-user.bat` and press `Edit`

> Enable `Show > File name extensions` if you can't find this file

Then you can add the following flags after the **`COMMANDLINE_ARGS=`** line *(each separated by a space)*

- **`--xformers`** to speed up the generation and reduce memory consumption
- **`--medvram-sdxl`** if you have less than **12 GB** VRAM, but wish to use **SDXL** checkpoints
- **`--medvram`** if you have less than **8 GB** VRAM
    - **`--lowvram`** instead if you're still getting **CUDA Out of Memory Error**

#### Advanced Args

- **`--api`** allows other programs to interact with the Webui. See the official [Documentation](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API) for more info.
- **`--port XXXX`** specifies which port to use

<hr>

- See all available Commandline Args [Here](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings)
