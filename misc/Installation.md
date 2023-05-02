<h1 align="center">Installation Guide</h1>
<p align="center"><b>for AUTOMATIC1111 Webui</b></p>
<p align="center"><i>by. Haoming 2023/05/02</i></p>

> [Official Guide](https://github.com/AUTOMATIC1111/stable-diffusion-webui#installation-and-running)

## Requirements
- [Python **3.10**](https://www.python.org/downloads/) *(Remember to enable `Add to PATH` during the installation)*
- [git](https://git-scm.com/downloads)
- **(Optional)** [GitHub Desktop](https://desktop.github.com/)

## Step by Step
0. **CUDA Toolkit:** If you have an Nvidia GPU, be sure to install [`CUDA Toolkit`](https://developer.nvidia.com/cuda-toolkit-archive) version **11.x.x** first. Otherwise, `PyTorch` will be running on CPU only and is incredibly slow!
1. **Download the Project:** There are a few ways to do this:
    1. Type `cmd` in the address bar of the desired folder to open the **Command Prompt**. Then paste in `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git` to clone the project.
    2. Open **GitHub Desktop**, go to `File` -> `Clone Repository` -> `URL` and paste in `https://github.com/AUTOMATIC1111/stable-diffusion-webui` to clone the project.
    3. *(Not Recommanded)* Go to the [GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui) page, and press `Code` -> `Download ZIP`, extract to desired folder.
2. **Update the Project:** In the future, there may be newer versions of the **webui** available. I highly recommend you to back up the old version *(**eg.** Rename the project folder)* and follow the step above to clone again to avoid complications.
3. **COMMANDLINE ARGS:** Go to the project folder, right click the file `webui-user.bat` and press `Edit`. Then:
    - Add either `--xformers` or `--opt-sdp-attention` after `COMMANDLINE_ARGS=` to speed up the generation and reduce memory consumption
        - Supposedly, the former works for **Torch 1.x** while the latter works for **Torch 2.x**. But apparently they still work for the opposite version too. Experiment with either and see which yields better speed
    - Add `--no-half-vae` after `COMMANDLINE_ARGS=` to stop NaN images from generating
    - Add `--medvram` after `COMMANDLINE_ARGS=` if you have less than **8GB** VRAM
        - Add `--lowvram` instead if you're still getting **CUDA Out of Memory Error** errors
4. **(Optional)** Download a Checkpoint model and put it into `~\stable-diffusion-webui\models\Stable-diffusion` first.
5. **Launch:** Launch the **webui** via `webui-user.bat`. When you launch it for the first time, it will download and install all the requirements. This will take a while so be patient. ~~Read the rest of the guide in the meantime~~. Additionally, it will also download the default `Stable-Diffusion-v1-5` model if you didn't do step 4.
6. **Run:** You will know it's finished loading when you see **`Running on local URL:  http://127.0.0.1:XXXX`**. You can then `Ctrl + Left Click` that link to open it in your browser.

## Additional Info:
- It's highly recommended to install the project on **SSD** instead of HDD, so loading the models only takes seconds instead of minutes.
- You can add `--ckpt <path to model>` and `--vae-path <path to vae>` after `COMMANDLINE_ARGS=` to specify which models to start with. This way, you can for example duplicate and rename the `.bat` to `webui-user-realistic.bat` and `webui-user-anime.bat`, which start with their respective models.
- You can add `--api` after `COMMANDLINE_ARGS=` to allow other programs to talk to it. See the official [Doc](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API) for more info.
- You can add `--port XXXX` after `COMMANDLINE_ARGS=` to specify which local port to use.