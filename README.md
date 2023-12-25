<p align="center"><img src="misc/Banner.jpg" alt="Stable Diffusion All-in-One Guide"></p>
<p align="center"><b>by. Haoming</b><br><i>Last Update: 2023/12/25</i></p>
<p align="right"><i>corresponding <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">webui</a> version: <code>v1.7.0</code></i></p>

## What is Stable Diffusion?
`Stable Diffusion` is a model for AI image generation, similar to `DALL·E`, `Midjourney` and `NovelAI`. 
The main advantage is that, `Stable Diffusion` is **open source**, runs **locally**, and is completely **free** to use.
User can input prompts, and the AI will generate artworks based on those prompts. 
Additionally, there are *a lot of* community-made tools and extensions that can achieve different styles, concepts or functions, 
giving the user the full control of the generation and customization. 

## Index
1. [Getting Started](#getting-started)
2. [Models](#models)
   1. [Checkpoint](#checkpoint)
      - [Versions](#sd-versions)
   2. [VAE](#vae)
   3. [Embedding](#checkpoint)
   4. [LoRA](#checkpoint)
3. [Terminologies](#terminologies)
4. [Tips](#tips)
5. [Extensions](#extensions)
6. [Learning Resources](#resources)

<hr>

## Getting Started
One simple and straightforward way to access Stable Diffusion is through a client called [**Automatic1111 Webui**](https://github.com/AUTOMATIC1111/stable-diffusion-webui). 
> [Installation Guide](misc/Installation.md)

There are also other popular user interfaces, such as [**Fooocus**](https://github.com/lllyasviel/Fooocus) and [**ComfyUI**](https://github.com/comfyanonymous/ComfyUI), each with their own pros and cons. 
The UI-related information in this Guide will mainly focus on Automatic1111 Webui, 
but the general knowledge about Stable Diffusion is the same for all of them!

> **Fooocus** is rather simplified, suitable for those who just want to get beautiful artworks by writing a prompt

> **ComfyUI** is significantly more complicated, but also allows you to delve into more technical settings

> **GoogleColab** now blocks Stable Diffusion from running unless you use a paid subscription

## Models
Nowadays, the most widely used model hosting site is called [**CivitAI**](https://civitai.com/). 
It hosts all sorts of models, as well as user-generated guides and resources.
Furthermore, each page also contains user comments, ratings, and samples. 

>`.safetensors` is a new format for storing weights safely *(as opposed to `pickle`)* while also being really fast. Always choose `.safetensors` if available.

### Checkpoint
**Checkpoint** refers to the main "model" Stable Diffusion runs on.
It takes the most storage size, and has the greatest impact on the generation results. 

**To Install:**
> Put **Checkpoint** in `~webui\models\Stable-diffusion`

#### SD Versions
There has been several generations of models released by **Stability AI**:
- **`Stable Diffusion 1.5`**: This version is currently the most widely used, with the best Extension supports.
- **`Stable Diffusion XL`**: Able to achieve better quality *(~~debatable~~)*, but also has higher resources requirements.
- **`SVD`**: Used for video generation. Will not be covered in this Guide.
- **`SDXL Turbo`**: Able to generate a decent image with just **1** step, making realtime render a reality.

Models of different generations are **not** compatible with each other. *(**incl.** Checkpoints, LoRAs, Extension supports, etc.)*

> *Ignore `Stable Diffusion v2.1`, we don't talk about it*

### VAE
**VAE** *(**V**ariational **A**uto**E**ncoder)* is responsible for converting RGB images to/from latent space.
Different VAE can produce different colors for example. Every Checkpoint has a VAE baked-in. 
But you can also force a specific VAE by going to `Settings` -> `VAE` -> **`SD VAE`**.

**To Install:**
> Put **VAE** in `~webui\models\VAE`

### Embedding
**Embedding** *(or **Textual Inversion**)* is a way to train the Text Encoder to create certain concepts *(**eg.** Characters, Style, etc.)* 

**To Install:**
> Put **Embedding** in `~webui\embeddings`

### LoRA
**`LoRA`** *(**Lo**w-**R**ank **A**daptation)* is a way to train the UNET to create certain concepts *(**eg.** Characters, Style, etc.)* 

- **Note:** Most **LoRA**s require **trigger words** to activate. Be sure to check the info on the CivitAI page first.

**To Install:**
> Put **LoRA** in `~webui\models\Lora`

## To Activate: 
Under the prompt fields, there is a row of tabs next to the **Generation** tab. 
Click on them to see the models currently installed. *(If you don't see your models, click on the **Refresh** button.)*
Simply click on the individual model card to add them to the prompt.

## Terminologies

### Tabs
- **`txt2img`:** Generate image based on input prompts
- **`img2img`:** Generate image based on an input image and prompts
- **`Extras`:** Upscale or Preprocess image
  - Aside from the default options, you can also download other upscale models from the [database](https://openmodeldb.info/), and put them into `~webui\models\ESRGAN` to use them.
  - One popular model is **`4x-UltraSharp`**
- **`PNG Info`:** You can upload an image to see what prompts and settings were used to generate it *(provided that the metadata was not removed)*
- **`Checkpoint Merger`:** ~~The easiest way to spam *something* onto CivitAI~~
- **`Train`:**  Train Embeddings
- **`Settings`:** Settings 💀
- **`Extensions`:** Install & Manage [Extensions](#extensions)

### Fields
> Value in `[ ]` are the typical values used

- **`Prompt`:** The text for what you want in the output.
- **`Negative Prompt`:** The text for what you don’t want in the output.
- **`Sampling Method`:** Read this [article](https://stable-diffusion-art.com/samplers/) for explanations and examples.
- **`Sampling Steps`:** The number of denoising iterations. `[16 ~ 32]`
  - Low value causes the output to be blurry; High value takes longer.
  - **`LCM`** models can generate decent images with as few as 4 steps
  - **`SDXL Turbo`** models can generate decent images with just 1 step
- **`Hires. Fix`:** Run through the pipeline a second time to upscale and make the output significantly better.
- **`Refiner`:** *You can simply ignore this tbh*
- **`Width/Height`:** The resolution of the generated image. 
  - **Important:** Keep it at `512x512` for `SD 1.5` models; around `1024x1024` for `SDXL` models. *(Refer to [versions](#sd-versions) if you don't know what these mean.)*
- **`Batch Count`:** How many batches to generate (in series).
- **`Batch Size`:** How many images per batch (in parallel).
- **`CFG Scale`:** How strong the prompts influence the output. `[4 ~ 8]`
  - Low value generates random images; High value generates really distorted images.
  - For **`LCM`** and **`SDXL Turbo`** models, set it to **1** instead.
- **`Seed`:** The random seed that affects how images are generated. If you use the same seed*, same prompts, and same settings, you *should* get the same output.

> **\*:** In `Settings` -> `Stable Diffusion` -> **`Random number generator source`**, you can change how the seed is calculated. Use **CPU** for the maximum recreatibility across different systems.

## Tips

### Guide for SD 1.5 Models
- In **positive** prompt, start with `(high quality, best quality)`
- In **negative** prompt, start with `(bad quality, worst quality:1.2)`
- If you’re using anime models (**eg.** `anything-v3.0`), go to `Settings` -> `Stable Diffusion`, set **`Clip skip`** to **`2`**.

> These are less important for SDXL models

### Styles
- You can save the current prompts using the **Styles** feature, and reuse them in the future.
  - Click the `🖌️` button to open the Style Dialogue, and edit/save the prompts
  - With this, you no longer need to write all the starting prompts every single time

### Brackets
- You can use `( )` to increase the influence of a prompt.
- You can use `[ ]` to decrease the influence of a prompt.
- You can also specify the weight by `(tag:ratio)`
  - **e.g.** `(foo:0.5)`, `(bar:1.5)`

### Prompt Order
The order of the prompts does have effects on the generation results. For example:

- `<subject>, <background>` will first generate the subject then try to fill the background.
- `<background>, <subject>` will first generate the background then try to fit in the subject.

<p align="center"><img src="misc/Order.jpg" width=384></p>

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

**Note:** After you install new extensions, you need to restart the webui to load them properly.

### Control Net
[<--- link --->](ControlNet/README.md)

### Super Resolution Upscale
[<--- link --->](TiledVAE/README.md)

### Multiple Characters
[<--- link --->](MultiChara/README.md)

### Token Merging
[<--- link --->](ToMe/README.md)

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

## Training

### Embedding Training
- [Video by Aitrepreneur](https://youtu.be/2ityl_dNRNw)
- [Video by OlivioSarikas](https://youtu.be/MLz0iM0M7Fk)

### LoRA Training
[<--- link --->](LoRATraining.md)

## Resources
- Reddit [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/)
- Webui [Features](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features)
- Youtube [Sebastian Kamph](https://www.youtube.com/@sebastiankamph/)
- Youtube [OlivioSarikas](https://www.youtube.com/@OlivioSarikas)
- YouTube [Aitrepreneur](https://www.youtube.com/@Aitrepreneur)

# Support Me!
If you appreciate my works and wish to support me, you can buy me a [coffee](https://ko-fi.com/haoming).

[![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)
