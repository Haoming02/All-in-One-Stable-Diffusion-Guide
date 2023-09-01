<p align="center"><img src="misc/Banner.jpg" alt="Stable Diffusion All-in-One Guide"></p>
<p align="center"><b>by. Haoming</b><br><i>Last Update: 2023/08/31</i></p>
<p align="right"><i>corresponding webui version: <code>v1.6.0</code></i></p>

## What is Stable Diffusion?
`Stable Diffusion` is an AI art generating tool just like `Midjourney` and `NovelAI`, 
but **open source**, runs **locally**, and is **free** to use.
User can input prompts, and the AI will generate artworks based on those prompts. 
Additionally, there are *a lot of* community-made models and extensions that can achieve different styles, concepts or functions, 
giving the user the full custom control of the generation. 

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
One simple and straightforward way to use Stable Diffusion is through a client called [**Automatic1111 Webui**](https://github.com/AUTOMATIC1111/stable-diffusion-webui). 
- [Installation Guide](misc/Installation.md) for **Automatic1111**

> GoogleColab now blocks Stable Diffusion from running unless you use a paid subscription!

There are also other popular user interfaces, such as [ComfyUI](https://github.com/comfyanonymous/ComfyUI) and [Fooocus](https://github.com/lllyasviel/Fooocus).
However, those come with their own pros and cons, and will not be covered in this guide.

> **ComfyUI** is significantly more complicated, but also allows you to delve into more technically settings

## Models
Nowadays, the most widely used model hosting site is called [CivitAI](https://civitai.com/). 
It hosts all sorts of models, as well as user-generated guides and resources.
Furthermore, each model page also contains user comments, ratings, and samples. 

**Note:** Certain models and sample images are flagged by the system and thus hidden. You may need to login to see more models.

>`.safetensors` is a new format for storing tensors safely *(as opposed to `pickle`)* while also being really fast. Always choose `safetensors` if available.

### Checkpoint
**Checkpoint** is basically the main "model" you run Stable Diffusion on.
It is the largest in storage size *(2+ GB)*, and has the greatest impact on the generation results. 

##### To Install
> Put **Checkpoint** in `~webui\models\Stable-diffusion`

#### SD Versions
Most of the Checkpoints on CivitAI were trained on **`Stable Diffusion v1.5`**. 
This version is currently the most widely used, with the best Extension supports.

Last month, `Stability AI` also released **`Stable Diffusion XL`**, 
which is able to achieve better quality, but also has higher resources requirements.
Right now, it's still in its infant stage, and the community is still adapting.

**TL;DR:** `v1.5` is mature; `XL` is the bleeding edge

> *Ignore `Stable Diffusion v2.1`, we don't talk about it*

### VAE
**VAE** *(**V**ariational **A**uto**E**ncoder)* is responsible for converting a RGB image to/from latent space.
Different VAE can produce more vibrant colors for example. Every Checkpoint has a VAE baked-in. But you can also force a specific VAE by going to `Settings` -> `VAE` -> **`SD VAE`**.

##### To Install
> Put **VAE** in `~webui\models\VAE`

### Embedding
**Embedding** *(or **Textual Inversion**)* is a way to train the text encoder to create certain concepts *(**eg.** Characters, Style, etc.)* 

##### To Install
> Put **Embedding** in `~webui\embeddings`

### LoRA
**`LoRA`** *(**Lo**w-**R**ank **A**daptation)* is a way to train the UNET to create certain concepts *(**eg.** Characters, Style, etc.)* 

- **Note:** Most **LoRA**s require **trigger words** to activate. Be sure to check the info on the CivitAI page first.

##### To Install
> Put **LoRA** in `~webui\models\Lora`

#### To Activate: 
- For `webui v1.6`:
You should see the tabs of different models right next to the **Generation** tab. Click on them to add them to the prompt.

- For `webui v1.5` and prior:
Click the red button *(`Show extra networks`)* under **Generate** to open the sub-menu. Click on them to add them to the prompt.

> Here’s a detailed [technical explanation](https://youtu.be/dVjMiJsuR5o) on how the different models work if you’re interested. *(Just ignore the outdated conclusion.)*

## Terminologies

### Tabs
- **`txt2img`:** Generate image based on input prompts
- **`img2img`:** Modify an input image based on input prompts
- **`Extras`:** Upscale image
  - Aside from the default options, you can also download other models from the [database](https://upscale.wiki/wiki/Model_Database) into `~webui\models\ESRGAN` to use them. *(Restart the webui to refresh the list.)* One popular model is **`4x-UltraSharp`**
- **`PNG Info`:** You can upload an image to see what prompts and settings were used to generate it *(provided that the metadata was not removed)*
- **`Checkpoint Merger`:** ~~The easiest way to spam *something* onto CivitAI~~
- **`Train`:** Preprocess Images & Train Embeddings
- **`Settings`:** Settings 💀
- **`Extensions`:** Install & Manage [Extensions](#extensions)

## Fields
- **`Prompt`:** The text for what you want in the output.
- **`Negative Prompt`:** The text for what you don’t want in the output.
- **`Sampling Method`:** Basically, this affects the denoising process and thus how the final output look. You can read this [article](https://stable-diffusion-art.com/samplers/) for explanations.
- **`Sampling Steps`:** The number of denoising iterations. Low value causes the output to be blurry; High value takes longer and suffers from diminishing return.
- **`Hires. Fix`:** Run through the pipeline a second time to upscale and make the output significantly better.
- (v1.6) **`Refiner`:** A new way to improve the output, introduced with **SDXL**.
- **`Width/Height`:** The resolution of the generated image. 
  - **Important:** Keep it at `512x512` for `v1.5` models; around `1024x1024` for `SDXL` models. *(Refer to [versions](#sd-versions) if you don't know what these mean.)*
- **`Batch Count`:** How many batches to generate (in series).
- **`Batch Size`:** How many images per batch (in parallel).
- **`CFG Scale`:** How strong the prompts influence the output. Low value generates random images; High value generates really distorted images.
- **`Seed`:** The random seed that affects how images are generated. If you use the same seed, same prompts, and same settings, you *should* get the same output.

## Tips

### Guide for v1.5 Models
- If you’re using anime models (**eg.** `anything-v3.0`), go to `Settings` -> `Stable Diffusion`, set **`Clip Skip`** to **`2`**.
- In **positive** prompt, start with `high quality, best quality`
- In **negative** prompt, start with `(bad quality, worst quality:1.2)`

### Styles
- You can save the prompts using the Styles function to reuse them in the future.

### Brackets
- You can use `( )` to increase the influence of a prompt.
- You can use `[ ]` to decrease the influence of a prompt.
- You can also stack brackets
  - **e.g.** `[[foo]]`
- Alternatively, use `(tag:ratio)`
  - **e.g.** `(bar:1.5)`

##### Example
`(long hair:1.5), [[black hair]]` will try to generate long hair, but the color of the hair is not a priority.

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
**Extensions** are basically 3rd-party features not native to the webui, which provide additional functions. 

- You can go to the **Extensions** tab, click `Available`, then click `Load from`. This will generate a list of extensions from the official Index. You can then click **Install** to download them.
- Alternatively, use `Install from URL` and paste in the link to a repo to install extensions not in the Index.

**Note:** After you install new extensions, you need to restart the webui to load them properly.

### Control Net
[<--- link --->](ControlNet/README.md)

### Super Resolution Upscale
[<--- link --->](TiledVAE/README.md)

### Speed Up Generations
[<--- link --->](ToMe/README.md)

### Multiple Characters
[<--- link --->](MultiChara/README.md)

### Vectorscope CC
[<--- link --->](https://github.com/Haoming02/sd-webui-vectorscope-cc)

### Prompt Format
[<--- link --->](https://github.com/Haoming02/sd-webui-prompt-format)

### Easy Tag Insert
[<--- link --->](https://github.com/Haoming02/sd-webui-easy-tag-insert)

## Training

### Embedding Training
~~*Train LoRA instead*~~
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
If you like my works and wish to support me, you can buy me a [coffee](https://ko-fi.com/haoming).

[![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)
