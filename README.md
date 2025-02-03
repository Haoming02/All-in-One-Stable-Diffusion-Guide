<p align="center">
<img src="./banner.jpg" alt="Stable Diffusion All-in-One Guide"><br>
<b>by. Haoming</b><br>
<i>2025 Feb.</i>
</p>

<p align="right">
<sub><i>corresponding <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">Webui</a> version: <code>v1.10.1</code></i></sub><br>
<sup><i>corresponding <a href="https://github.com/lllyasviel/stable-diffusion-webui-forge">Forge</a> version: <code>v2.0.1</code></i></sup>
</p>

## Introduction
**Stable Diffusion** is a text-to-image generative AI model, similar to online services like `Midjourney` and `Bing`. Users can input prompts *(text descriptions)*, and the model will generate images based on these prompts. The main advantage of `Stable Diffusion` is that it is **open-source**, completely **free** to use, and can be run **locally** without any **censorship**.

Furthermore, there are many community-developed extensions *(tools)* that can perform a wide range of functions, as well as numerous community-trained models that can achieve various styles and concepts, giving users full creative control over the generations.

<details open>
<summary><h2>Index</h2></summary>

1. [Getting Started](#getting-started)
    - [Hardware Requirement](#hardware-requirement)
    - [Popular UIs](#popular-uis)
2. [Models](#models)
    - [Architecture](#architecture)
    - [Checkpoint](#checkpoint)
    - [UNet](#unet)
    - [Text Encoder](#text-encoder)
    - [VAE](#vae)
    - [Embedding](#embedding)
    - [LoRA](#lora)
    - [How to Use](#how-to-use)
    - [Download](#download)
    - [Diffusers](#diffusers)
3. [Terminologies](#terminologies)
    - [Tabs](#tabs)
    - [Parameters](#parameters)
4. [Settings](#settings)
    - [Saving images/grids](#saving-imagesgrids)
    - [Optimizations](#optimizations)
    - [Stable Diffusion](#stable-diffusion)
    - [Live Previews](#live-previews)
    - [System](#system)
5. [Tips & Tricks](Tips/README.md)
    - [X/Y/Z Plot](Tips/XYZ.md)
6. [Extensions](#extensions)
    - [Installation](#how-to-install)
    - [Update](#how-to-update)
    - [Recommendations](#recommendations)
    - [ControlNet](ControlNet/README.md)
7. [LoRA Training](./LoRATraining.md)
8. [Learning Resources](#resources)

</details>

## Getting Started
> This section will cover some basic information on how to start generating images locally

### Hardware Requirement
To run AI models locally, a Graphics Card (**GPU**) from **Nvidia** is required

> [!NOTE]
> While it is possible to run `Stable Diffusion` on **AMD**, **Apple**, or even **Intel** GPUs, the setup can be more complicated and the processing speed is usually slower

When choosing a GPU, **VRAM** is the most important spec. Sufficient VRAM is essential to fit the entire model into memory; processing speed is only relevant once the model can be fully loaded. If your GPU does not have enough VRAM, the model will be partially loaded into system swap memory instead, significantly reducing the processing speed by up to ten times. Additionally, aim for the RTX 30 series or later, as older GPUs have limited support for half precision.

These are the reasons why, RTX 3060 *(`12 GB` VRAM)* is generally recommended over RTX 3070 *(`8 GB` VRAM)* and RTX 2080 *(`11 GB` VRAM)*.

#### List of Recommendation
- **Budget:** RTX 3060 *(`12 GB` VRAM)*
- **Entry Level:** RTX 4060 Ti *(`16 GB` VRAM)*
- **Enthusiast:** Second-Hand RTX 3090 *(`24 GB` VRAM)*
- **Professional:** RTX 4090 *(`24 GB` VRAM)*
- **Baller:** RTX 5090 *(`32 GB` VRAM)*

> **What I am using:** RTX 4070 Ti Super *(`16 GB` VRAM)*

> [!TIP]
> If you do not have a capable system, there are also (paid) [online services](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Online-Services) for Stable Diffusion

### Popular UIs
Listed below are some popular **U**ser **I**nterfaces to run Stable Diffusion:

- [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui): The classic frontend that helped popularizing Stable Diffusion in the early days, with a large community and extension supports; though development seems to be halted as of now

- [Forge Webui](https://github.com/lllyasviel/stable-diffusion-webui-forge): A frontend based on **Automatic1111**, with a more optimized memory management that allows even low-end devices to run Stable Diffusion; though some may find Gradio 4 unresponsive; and development seems to be halted as of now

> [!TIP]
> [Installation Guide](./Installation.md) for **Automatic1111** / **Forge**

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI): An advanced node-based frontend, providing the maximum flexibility for users to build custom complex workflows; though the learning curve is steeper as a result

- [Fooocus](https://github.com/lllyasviel/Fooocus): A rather simple frontend, suitable for those who simply want beautiful artworks by just writing a prompt

- [SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI), [InvokeAI](https://github.com/invoke-ai/InvokeAI), [SD.Next](https://github.com/vladmandic/automatic): Other notable frontend; though personally I've never tried them

- [Stability Matrix](https://github.com/LykosAI/StabilityMatrix): A platform that simplifies the frontend installation and model management

> **What I am using:** [Forge Classic](https://github.com/Haoming02/sd-webui-forge-classic), based on the "previous" (Gradio 3) version of **Forge**, with a few minor updates and optimization added

<br>

## Models
> This section will cover various things the word "model" can refer to in the context of Stable Diffusion

### Architecture
There has been numerous architectures released over the years. Listed below are the most widely adopted versions as of now:

- **`Stable Diffusion 1.5`:** The good ol' version that basically brought local image generation into the mainstream. As the smallest model with a base resolution of only `512x512` and an inability to generate hands reliably, its quality is less comparable nowadays. But it remains quite popular thanks to its lower system requirements.
    - *(hereinafter referred to as **SD1** below)*
- **`Stable Diffusion XL`:** The newer and bigger version with a base resolution of `1024x1024`. It now understands prompts better and has a lower chance of generating *eldritch abominations*. But it also has considerably higher system requirements.
    - *(hereinafter referred to as **SDXL** below)*
- **`Pony Diffusion V6 XL`**: A specialized version of `SDXL` that underwent extensive training, causing many features to be incompatible between the two, resulting in a distinct category of its own. This model was specially fine-tuned on "Booru tags" to generate anime/cartoon images, with good prompt comprehension and the ability to generate correct hands/feet.
    - *(hereinafter referred to as **Pony** below)*
- **`Illustrious`**: Another specialized version of `SDXL` that was fine-tuned on "Booru tags" to generate anime images. It has even better prompt comprehension without a broken Text Encoder. Additionally, since the training dataset was not obfuscated, many popular characters can be directly prompted.
    - **TL;DR:** `Illustrious` series is significantly better than `Pony` series nowadays

> [!TIP]
> **Booru Tags** refers to the comma-separated tags used by anime image boards; see this post of [Hatsune Miku](https://safebooru.donmai.us/posts/135361) for example

- **`Flux`**: One of the latest architectures, capable of generating legible text and next-gen quality, with next-gen hardware requirements...
    - *(Don't even bother if you have less than 12 GB VRAM)*
    - There are 3 variants:
        - **`pro`:** Only available through **paid** online services
        - **`dev`:** Distilled from `pro`, uses standard number of steps **(non-commercial)**
        - **`schnell`:** Further distilled from `dev`, requires fewer number of steps
    - ~~Technically, this is not Stable Diffusion~~

- **`Stable Diffusion 3.5`**: Another one of the latest architectures
    - There are 2 variants:
        - **`large`:** Quality is comparable to `Flux`; can also generate texts
        - **`medium`:** Slightly worse quality; but is also lighter to run
    - *(Though, seems that there is no wide adoption yet)*
    - *(hereinafter referred to as **SD3** below)*

> [!IMPORTANT]
> Models of different architectures are **not** compatible with each other *(**eg.** a LoRA trained for `SD1` will **not** work with `SDXL`, etc.)*

> **What I am using:** [Hassaku XL (Illustrious)](https://civitai.com/models/140272?modelVersionId=1200105) - A model further trained on Illustrious

### Checkpoint
**Checkpoint** is what "model" usually refers to. It is the whole package that contains the **UNet**, **Text Encoder**, and **VAE** mentioned below.
- For `SD1` and `SDXL`, models are usually distributed in a single checkpoint
- For `Flux` and `SD3`, the components are usually distributed separately due to the large size

> [!NOTE]
> Put **Checkpoint** in `~webui\models\Stable-diffusion`

### UNet
**U-Net** is the core component that processes the latent noises to generate the image.

> [!NOTE]
> Put **UNet** in `~webui\models\Stable-diffusion`

> [!NOTE]
> For `Flux` and `SD3`, the "core component" is **DiT** instead of **U-Net**, but people generally still call them `UNet` on the internet

### Text Encoder
**Text Encoder** is the component that converts the human-readable prompts into vectors that the model understands.
- `SD1`, `SDXL`, `SD3`, and `Flux` all use the small **Clip** text encoder(s) *(`~300 MB`)*
- `SD3` and `Flux` additionally use the big **T5** text encoder *(`~10 GB` at `fp16` precision)*

> [!NOTE]
> Put **Text Encoder** in `~webui\models\text_encoder`

### VAE
**VAE** is the component that converts RGB images to / from latent space

> [!NOTE]
> Put **VAE** in `~webui\models\VAE`

### Embedding
**Embedding** *(or **Textual Inversion**)* is a technique used to train the `Text Encoder` to learn specific concepts *(**eg.** Characters, Style, etc.)*

> [!NOTE]
> Put **Embedding** in `~webui\embeddings`

### LoRA
**LoRA** *(and **LyCORIS**)* is a technique used to train the `UNet` *(and optionally `Text Encoder`)* to learn specific concepts *(**eg.** Characters, Style, etc.)*

> [!IMPORTANT]
> Most `LoRA` requires **trigger words** to function correctly, make sure to read the description

> [!NOTE]
> Put **LoRA** in `~webui\models\Lora`

### How to Use
- To change **Checkpoint**, select from the `Stable Diffusion checkpoint` dropdown at the top of the UI
    - To use the separated components in Forge, refer to this [Announcement](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1050)
- To use **Embedding**, click on the model card to add the filename to the prompt field
- To use **LoRA**, click on the model card to add the syntax to the prompt field
- To manually set a **VAE**, select from the `SD VAE` dropdown in the `VAE` section of the `Settings` tab

> [!TIP]
> - If you don't see your newly added models, remember to click the **Refresh** button first
> - By default, the Webui should detect the [architecture](#architecture) of LoRAs and hide incompatible ones automatically; if you encounter a situation where known-compatible LoRAs are not showing up, you can enable the `Always show all networks on the Lora page` toggle in the `Extra Networks` section of the `Settings` tab

### Download
**[CivitAI](https://civitai.green/models)** is a site that hosts all sorts of models and user-generated resources like guides. When browsing, you can click the `Filters` to look for a specific model type or architecture. Every page contains user comments, ratings, and samples. Remember to check the `Base Model` in the `Details` before downloading.

> [!NOTE]
> `.safetensors` is a format to store the weights safely; always choose `.safetensors` if available

### Diffusers
On [HuggingFace](https://huggingface.co/), you may come across repositories where each component is separated into sub-folders, such as [epiCRealism](https://huggingface.co/emilianJR/epiCRealism/tree/main). This format is used by the [Diffusers](https://huggingface.co/docs/diffusers/en/index) library. However, the Webui does not support this format. Usually you can find a link to the checkpoint format used by the Webui instead in the `Model card`.

<br>

## Terminologies
> This section will cover some `noun.` used within the Webui

### Tabs
- **`txt2img`:** Generate an image based on prompts
- **`img2img`:** Generate an image based on another image and prompts
- **`Extras`:** Postprocess images *(**incl.** Upscale, Caption, Crop, etc.)*
  - You can download upscaler models from [OpenModelDB](https://openmodeldb.info/)

> [!NOTE]
> Put **upscaler** in `~webui\models\ESRGAN`

> **What I am using:** [2x-NomosUni-esrgan-multijpg](https://openmodeldb.info/models/2x-NomosUni-esrgan-multijpg)

- **`PNG Info`:** You can upload a generated image to see the infotext *(**ie.** the prompts and parameters used)*, provided that the metadata was not removed from the image
- **`Checkpoint Merger`:** ~~The easiest way to spam more junks onto CivitAI~~
- **`Train`:** Broken; use **[Kohya_SS](https://github.com/bmaltais/kohya_ss)** instead
- **`Settings`:** Settings 💀
- **`Extensions`:** Install & Manage [Extensions](#extensions)

### Parameters
- **`Prompt`:** The text for what you want in the output
- **`Negative Prompt`:** The text for what you don’t want in the output
- **`Sampling Method`:** Read this [article](https://stable-diffusion-art.com/samplers/) for explanations and examples
    - **TL;DR:** `Euler a` tends to generate smoother images, suitable for anime models; `DPM++ 2M Karras` tends to generate detailed images, suitable for realistic models

> [!NOTE]
> Since Webui `v1.9.0`, the **Sampler** and **Scheduler** are now two separated dropdowns

- **`Sampling Steps`:** The number of denoising iterations
  - `20` ~ `32` is generally enough
  - Low value causes the output to be noisy; High value takes longer with no benefit
  - **[LCM](https://huggingface.co/latent-consistency/lcm-lora-sdxl)** and **[Lightning](https://huggingface.co/ByteDance/SDXL-Lightning)** models can generate decent images with as few as 4 steps
  - **[Turbo](https://huggingface.co/stabilityai/sdxl-turbo)** models can even generate images with just 1 step
- **`Hires. Fix`:** Upscale then run through the pipeline a second time to improve output
- **`Refiner`:** Obsolete; just ignore it...
- **`Width/Height`:** The resolution of the generated image

> [!IMPORTANT]
> Keep it at `512x512` for **SD1** models; around `1024x1024` for **SDXL**, **SD3**, **Flux** models; and keep both `width` and `height` at multiples of `64` *(**eg.** `1152x896`)*

- **`Batch Count`:** How many batches to generate *(in series)*
- **`Batch Size`:** How many images per batch *(in parallel)*
- **`CFG Scale`:** How strong the prompts influence the output
  - `4` ~ `8` is generally fine
  - Low value generates blurry images; High value generates "burnt" *(really high-contrast and distorted)* images
  - Generally, the lower the steps, the lower the CFG
    - **eg.** for **LCM**, **Lightning**, **Turbo**, set it to **`1`** instead
  - For `Flux` models, CFG should be set to **`1`** as well
- **`Seed`:** The random seed that affects the latent noise generation
  - You *should* get the same output if you use the same parameters and seed

> [!TIP]
> Go to the `Stable Diffusion` section of the `Settings` tab, and change **`Random number generator source`** to **`CPU`** for the maximum repeatability across different systems

<br>

## Settings
> This section will cover some settings recommended to change or frequently asked about

#### Saving images/grids
> These settings modify the saving behavior

- **File format for images:**
    - `png` is lossless with the largest filesize
    - `jpg` is lossy with the smallest filesize
    - `webp` is in-between, but takes slightly longer to save
- **Save copy of large images as JPG:**
    - If `enabled`, when you generate a high-resolution image, it would additionally save a `.jpg` once the filesize threshold is reached

#### Optimizations
> These settings can improve the generation speed

- **Cross attention optimization:**
    - `xformers` if enabled; `sdp - scaled dot product` otherwise
    - `Automatic` for Forge
- **Pad prompt/negative prompt** - `Enable`
- **Persistent cond cache** - `Enable`
- **Batch cond/uncond** - `Enable`

#### Stable Diffusion
> These settings affect the generation details

- **Enable quantization in K samplers:**
    - I myself did `enable` this, though the effect seem minimal
    - Seems to be always enabled for Forge
- **Emphasis mode:**
    - Setting it to `No norm` prevents a problem where certain `SDXL` models tend to generate pure noises
- **Clip skip:**
    - ~~Long story short,~~ some models work better with `2`; but setting it to `2` does not worsen the results for other models anyway. So just set it to `2`...

#### Live previews
> These settings affect the preview during generation

- **Live preview method:**
    - `TAESD`, significantly faster
- **Return image with chosen live preview method on interrupt:**
    - `Enable`, makes interrupts faster

#### System
> These settings modify the behavior of the Webui

- **Automatically open webui in browser on startup:**
    - Change this if you don't want the browser to start automatically
- **Show gradio deprecation warnings in console:**
    - `Disable`, like why...

<br>

## Tips & Tricks
- [General Knowledge and Webui Features](Tips/README.md)
- [Tutorial for X/Y/Z Plot](Tips/XYZ.md)

<br>

## Extensions
> Extensions are basically 3rd-party add-ons that provide additional features not native to the Webui

### How to Install
1. Go to the **Extensions** tab
2. Switch to the **Install from URL** sub-tab
3. In the `URL for extension's git repository` field, paste in the link to the Extension's GitHub page
    - **eg.** https://github.com/Haoming02/sd-webui-tabs-extension
4. **(Optional)** In certain use cases, you may need to fill out the `Specific branch name` field, usually for development or compatibility reasons
5. **(Optional)** You can fill out `Local directory name` to set a custom folder name *(The practical use of this is to sort Extensions)*
6. Click the **Install** button
7. Some Extensions may install additional dependencies; this can take some time
8. Once the installation is finished, an `Installed into ...` line will appear under the **Install** button
9. Switch to the **Installed** sub-tab
10. Click the **Apply and restart UI** button

### How to Update
1. Go to the **Extensions** tab
2. Click the **Check for updates** button
3. Once finished, some Extensions may show the `behind HEAD` label in the `Update` column
4. Click the **Apply and restart UI** button
5. Some Extensions may install additional dependencies; this can take some time

> [!TIP]
> Sometimes, after clicking the `Apply and restart UI` button, the browser will refresh first before the Webui is actually ready, and you may see a bunch of disconnected errors or broken UI texts. When this happens, do not use the Webui yet. Wait for the console to show the `Running on local URL: ...` line, then manually refresh (`F5`) the browser again. After which, the Webui will be good to go again.

### Recommendations
> Some essential Extensions that basically everyone should have

- <ins><b>ControlNet</b></ins>
    - [Tutorial for ControlNet - The biggest strength Stable Diffusion has over proprietary services](ControlNet/README.md)
- <ins><b>RegionalPrompter / ForgeCouple</b></ins>
    - [How to Generate Multiple Characters within the same Image](MultiChara/README.md)
- <ins><b>MultiDiffusion & TiledVAE</b></ins>
    - [How to Generate Extremely High Resolution Image without OOM](TiledVAE/README.md)

### Shameless Self Promotions
> Some Extensions written by yours truly

- <ins><b>Prompt Format</b></ins>
    - [Format your prompts by removing extra spaces and commas](https://github.com/Haoming02/sd-webui-prompt-format)
- <ins><b>Tabs Extension</b></ins>
    - [Convert Extensions into tabs for better organization](https://github.com/Haoming02/sd-webui-tabs-extension)
- <ins><b>Easy Tag Insert</b></ins>
    - [Trivialize inserting prompts by making shortcut buttons](https://github.com/Haoming02/sd-webui-easy-tag-insert)
- <ins><b>Image Comparison</b></ins>
    - [Easily compare images within the Webui](https://github.com/Haoming02/sd-webui-image-comparison)
- <ins><b>IC Light</b></ins>
    - [Manipulate the illumination of images](https://github.com/Haoming02/sd-forge-ic-light)
- <ins><b>Yapping</b></ins>
    - [Save parameters as preset buttons](https://github.com/Haoming02/sd-webui-yapping)
- <ins><b>Boomer</b></ins>
    - [Revert some UI changes for improved usability](https://github.com/Haoming02/sd-webui-boomer)

<br>

## LoRA Training
- [How to Train LoRA](./LoRATraining.md)

<br>

## Resources
> Some more places to learn about Stable Diffusion

- Reddit [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/)
- Webui [Features](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features)
- Youtube [Sebastian Kamph](https://www.youtube.com/@sebastiankamph/)
- Youtube [OlivioSarikas](https://www.youtube.com/@OlivioSarikas)
- Forge [Troubleshoot](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1474)
  - **eg.** `Press anykey to continue...`

<br>

## Support Me
- If you appreciate my works and wish to support me, you can buy me a [coffee](https://ko-fi.com/haoming)~

<hr>

<p align="center">
<a href="http://creativecommons.org/licenses/by-sa/4.0/"><img src="https://licensebuttons.net/l/by-sa/4.0/88x31.png"></a>
</p>
