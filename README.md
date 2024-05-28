<p align="center"><img src="misc/Banner.jpg" alt="Stable Diffusion All-in-One Guide"></p>
<p align="center"><b>by. Haoming</b><br><i>Last Update: 2024/05/28</i></p>
<p align="right"><i>corresponding <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">webui</a> version: <code>v1.9.3</code></i></p>

## What is Stable Diffusion?
`Stable Diffusion` is a text-to-image generative AI model, similar to `DALL·E`, `Midjourney` and `NovelAI`. User can input text prompts, and the AI will then generate images based on those prompts. The main difference is that, `Stable Diffusion` is **open source**, runs **locally**, while being completely **free** to use.

Additionally, there are many community-developed tools and extensions that can perform new functions; as well as many community-finetuned models that can achieve different styles and concepts, giving the user the full control of the generation.

## Index
1. [Getting Started](#getting-started)
2. [Models](#models)
   1. [Checkpoint](#checkpoint)
      - [Versions](#sd-versions)
   2. [VAE](#vae)
   3. [Embedding](#embedding)
   4. [LoRA](#lora)
3. [Terminologies](#terminologies)
4. [Settings](#settings)
5. [Tips](#tips--tricks)
6. [Extensions](#extensions)
6. [Training](#lora-training)
7. [Learning Resources](#resources)

<hr>

## Getting Started
Listed below are some of the most popular user interfaces, each with their own pros and cons:

- **[Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui):** The frontend that is ~~arguably~~ the most widely used, with a large community and extension supports

- **[Fooocus](https://github.com/lllyasviel/Fooocus):** A rather simple frontend similar to other online services, suitable for those who simply want beautiful artworks just by writing a prompt

- **[ComfyUI](https://github.com/comfyanonymous/ComfyUI):** A significantly more complicated frontend with a steep learning curve, but gives the maximum flexibility to the user for building complex custom workflow

- **[Forge Webui](https://github.com/lllyasviel/stable-diffusion-webui-forge):** A frontend based on **Automatic1111**, but with a more optimized memory management, allowing even low-end devices to run Stable Diffusion

- **[Stability Matrix](https://github.com/LykosAI/StabilityMatrix):** A software that streamlines the process of installing above frontends and managing models

> The UI-related information in this Guide will focus on the **Automatic1111 Webui**, but the general knowledge about Stable Diffusion is the same for all of them!

> **[Installation Guide](misc/Installation.md)** for Automatic1111 / Forge

> **GoogleColab** now blocks Stable Diffusion from running unless you use a paid subscription

## Models
In terms of Stable Diffusion, "model" can refer to various things as mentioned below.

One of the most widely used hosting sites is called **[CivitAI](https://civitai.com/)**. It hosts all types of models, as well as user-generated guides and resources. Furthermore, each page also contains user comments, ratings, and samples.

>`.safetensors` is a new format for storing weights safely *(as opposed to `pickle`)*. Always choose `.safetensors` if available.

#### Checkpoint
**Checkpoint** is the main "model" Stable Diffusion runs on. It takes the most storage size, but also has the greatest impact on the generation results.

**To Install:**
> Put **Checkpoint** in `~webui\models\Stable-diffusion`

##### SD Versions
There has been several generations of models released by **Stability AI**:
- **`Stable Diffusion 1.5`**: The version that was released earlier. Due to its lower system requirements, it is currently more widely used.
- **`Stable Diffusion XL`**: The newer version. Understands prompts significantly better, but also has higher system requirements.
- **`Stable Diffusion 3`**: T.B.D *(as of 05/27)*

Models of different generations are **not** compatible with each other. *(**incl.** Checkpoints, LoRAs, Extension supports, etc.)*

> *Ignore `Stable Diffusion v2.1`, we don't talk about it...*

#### VAE
**VAE** *(**V**ariational **A**uto**E**ncoder)* is responsible for converting RGB images to/from latent space. Different VAE can produce different colors for example. Every Checkpoint has a VAE baked-in. But you can also force a specific VAE by going to `Settings` -> `VAE` -> **`SD VAE`**.

**To Install:**
> Put **VAE** in `~webui\models\VAE`

#### Embedding
**Embedding** *(or **Textual Inversion**)* is a way to train the Text Encoder to create certain concepts *(**eg.** Characters, Style, etc.)*

**To Install:**
> Put **Embedding** in `~webui\embeddings`

#### LoRA
**`LoRA`** *(**Lo**w-**R**ank **A**daptation)* is a way to train the UNET to create certain concepts *(**eg.** Characters, Style, etc.)*

> **Note:** Most **LoRA**s require **trigger words** to activate. Be sure to check the description/info first

**To Install:**
> Put **LoRA** in `~webui\models\Lora`

### To Use:
Next to the **Generation** tab, there are tabs for all model types. Clicking on them will show all models currently installed. Simply click on the individual model card to insert them into the prompt.

> If you don't see your models, remember to click the **Refresh** button first

> By default, models of different generations are hidden. *(**eg.** When using a SDXL checkpoint, LoRAs for SD 1.5 will not be shown.)*

## Terminologies

### Tabs
- **`txt2img`:** Generate image based on input prompts
- **`img2img`:** Generate image based on an input image and prompts
- **`Extras`:** Process images *(**incl.** Upscale, Caption, Crop, etc)*
  - You can download other upscale models from the [database](https://openmodeldb.info/), and put them into `~webui\models\ESRGAN` to use them
    - Personal Recommendation: **[4x-Nomos8kDAT](https://openmodeldb.info/models/4x-Nomos8kDAT)**
- **`PNG Info`:** You can upload an image to see what prompts and settings were used to generate it *(provided that the metadata was not removed)*
- **`Checkpoint Merger`:** ~~The easiest way to spam *something* onto CivitAI~~
- **`Train`:**  Train Embeddings *(not recommended; use `Kohya_SS` instead)*
- **`Settings`:** Settings 💀
- **`Extensions`:** Install & Manage [Extensions](#extensions)

### Fields
- **`Prompt`:** The text for what you want in the output
- **`Negative Prompt`:** The text for what you don’t want in the output
- **`Sampling Method`:** Read this [article](https://stable-diffusion-art.com/samplers/) for explanations and examples
  - **Note:** Since Webui `v1.9.0`, the Sampler and Scheduler are now two separated dropdowns
- **`Sampling Steps`:** The number of denoising iterations
  - `20` ~ `32` is generally enough
  - Low value causes the output to be blurry; High value takes longer
  - **[`LCM`](https://huggingface.co/latent-consistency/lcm-lora-sdxl)** and **[`Lightning`](https://huggingface.co/ByteDance/SDXL-Lightning)** models can generate decent images with as few as 4 steps
  - **[`SDXL Turbo`](https://huggingface.co/stabilityai/sdxl-turbo)** models can even generate decent images with just 1 step
- **`Hires. Fix`:** Run through the pipeline a second time to upscale and make the output significantly better
  - Only recommended using with `SD 1.5` models *(Refer to [versions](#sd-versions) if you don't know what these mean.)*
- **`Refiner`:** *You can simply ignore this tbh...*
- **`Width/Height`:** The resolution of the generated image
  - **Important:** Keep it at `512x512` for `SD 1.5` models; around `1024x1024` for `SDXL` models. *(Refer to [versions](#sd-versions) if you don't know what these mean.)*
  - Also keep both values at multiples of `64` *(**eg.** `1152x896`)*
- **`Batch Count`:** How many batches to generate (in series)
- **`Batch Size`:** How many images per batch (in parallel)
- **`CFG Scale`:** How strong the prompts influence the output
  - `4` ~ `8` is generally fine
  - Low value generates random images; High value generates really distorted images
  - For **`LCM`**, **`Lightning`**, and **`SDXL Turbo`** models, set it to **`1`** instead
- **`Seed`:** The random seed that affects how images are generated
  - If you use the same seed*, same prompts, and same settings, you *should* get the same output

> **\*:** In `Settings` -> `Stable Diffusion` -> **`Random number generator source`**, you can change how the seed is calculated. Use **`CPU`** for the maximum recreatibility across different systems.

## Settings
Listed below are some settings that are worth checking out:

### Optimizations
- **Cross attention optimization:** `xformers` if you enabled it; `sdp - scaled dot product` otherwise
- **Pad prompt/negative prompt:** `Enable`
- **Persistent cond cache:** `Enable`
- **Batch cond/uncond:** `Enable`

### Stable Diffusion
- **Emphasis mode:** `No norm`
- **Clip skip:** `2`

### Live previews
- **Return image with chosen live preview method on interrupt:** `Enable`

### System
- **Automatically open webui in browser on startup:** Change this if you don't want it to start the browser automatically

## Tips & Tricks

### Starting Prompts
Due to how checkpoints are trained, it's usually better to add some "quality tags" at the beginning of the prompt to enhance the results. Refer to the description of the checkpoint page, as some of them require specific keywords to generate anything remotely good *(**eg.** Pony)*.

- **Example for SD 1.5:**
  - In **positive** prompt, start with `(high quality, best quality)`
  - In **negative** prompt, start with `(bad quality, worst quality:1.2)`

### Styles
- You can save the current prompts using the **Styles** feature, and reuse them in the future
  - Click the `🖌️` button to open the `Style Dialogue`, and edit/save the prompts
  - Useful for saving the starting prompts mentioned above

### Brackets
- You can use `( )` to increase the influence of a prompt.
- You can use `[ ]` to decrease the influence of a prompt.
- You can also specify the weight by `(tag:ratio)`
  - **e.g.** `(foo:0.5)`, `(bar:1.5)`

### Prompt Order
The order of the prompts **does** have an effect on the generation results. Specifically, earlier *(left)* prompts have more influence than later *(right)* prompts.

### X/Y/Z Plot
[< - Link - >](XYZ/README.md)

### Themes
[< - Link - >](TipsTricks/README.md#themes)

### Default Values
[< - Link - >](TipsTricks/README.md#default-values)

## Extensions
**Extensions** are basically 3rd-party addons that provide additional features not native to the webui.

- You can go to the **Extensions** tab, click `Available`, then click `Load from`. This will load a curated list of extensions from the official Index. You can then click **Install** to download them.
- Alternatively, use `Install from URL` and paste in the link to a repo to install extensions not listed in the Index.

**Note:** After you install new extensions, always restart the webui to load them properly.

### Control Net
[<--- link --->](ControlNet/README.md)

### Super Resolution Upscale
[<--- link --->](TiledVAE/README.md)

### Multiple Characters
[<--- link --->](MultiChara/README.md)

### TensorRT
[<--- link --->](TensorRT/README.md)

### Shameless Self Promotions
- [Prompt Format](https://github.com/Haoming02/sd-webui-prompt-format)
- [Tabs Extension](https://github.com/Haoming02/sd-webui-tabs-extension)
- [Boomer](https://github.com/Haoming02/sd-webui-boomer)
- [Easy Tag Insert](https://github.com/Haoming02/sd-webui-easy-tag-insert)
- [Diffusion CG](https://github.com/Haoming02/sd-webui-diffusion-cg)
- [ReSharpen](https://github.com/Haoming02/sd-webui-resharpen)
- [Vectorscope CC](https://github.com/Haoming02/sd-webui-vectorscope-cc)

## LoRA Training
[<--- link --->](LoRATraining.md)

## Resources
- Reddit [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/)
- Webui [Features](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features)
- Youtube [Sebastian Kamph](https://www.youtube.com/@sebastiankamph/)
- Youtube [OlivioSarikas](https://www.youtube.com/@OlivioSarikas)
- YouTube [Aitrepreneur](https://www.youtube.com/@Aitrepreneur)

<hr>

### Support Me!
If you appreciate my works and wish to support me, you can buy me a [coffee](https://ko-fi.com/haoming).

[![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)
