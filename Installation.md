<h1 align="center">Installation Guide</h1>
<p align="center"><b>by. Haoming</b></p>

<p align="right"><i>
for <b>Automatic1111</b> / <b>Forge</b> Webui<br>
<sup>(on Windows)</sup>
</i></p>

> [!IMPORTANT]
> For **Apple Silicon**, refer to this [Tutorial](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon) page instead <br>
> For **AMD GPU**, refer to the repo for [AMD GPU](https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu)  instead

> [!TIP]
> - Install the UI and put the models on an **SSD** to improve load time
> - Enable `View/Show/File name extensions` for the `File Explorer` to locate the files
> - Open `Nvidia Control Panel`, go to `Manage 3D settings`, and set `System Fallback Policy` to **Prefer No System Fallback**

## Download
- for **Forge**
    1. Go to the [Release](https://github.com/lllyasviel/stable-diffusion-webui-forge/releases/tag/latest) page
    2. Click on `webui_forge_cu124_torch24.7z` to download
- for **Automatic1111**
    1. Go to the [Release](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases/tag/v1.0.0-pre) page
    2. Click on `sd.webui.zip` to download

## Installation
1. Extract all contents to a folder of choice
    - Do **not** put them under `OneDrive` or other cloud drives
2. Run `update.bat` first
3. Modify the commandline args as mentioned below
4. Download a **checkpoint** of choice first
    - Otherwise, the Webui will automatically download a ~2 GB checkpoint
    > Refer to [Checkpoint](./README.md#checkpoint) if you don't know what this means
5. Run `run.bat`
    - On the first launch, the Webui will download and install all the required packages; this can take some time so be patient; ~~read the rest of the Guide in the meantime~~
6. When the installation is finished, it will automatically open a browser window showing the UI

#### Commandline Args
In the `webui` folder, right-click the `webui-user.bat` file and select `Edit`. Then, add the following flags as needed to the `COMMANDLINE_ARGS=` line:

- **`--xformers`:** speed up the generation and reduce memory consumption
- **`--listen`:** allow you to access the Webui from local network
- **`--port`:** specify which port to use
- **`--api`:** allow interaction with the Webui using Restful APIs
    - See the [Wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API) for more info

> [!NOTE]
> The following memory-related flags are only needed when using **Automatic1111**

- **`--medvram-sdxl`:** if you have less than 12 GB VRAM but wish to use **SDXL** checkpoints
- **`--medvram`:** if you have less than 8 GB VRAM
- **`--lowvram`:** if you're still getting **CUDA Out of Memory Error**

<hr>

- [List of All Commandline Args](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings)
