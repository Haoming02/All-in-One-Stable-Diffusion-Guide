<p align="center"><img src="misc/Banner.jpg" alt="Stable Diffusion All-in-One Guide"></p>
<p align="center"><b>by. Haoming</b><br><i>Last Update: 2023/05/31</i></p>
<p align="right"><i>corresponding webui version: <code>v1.3.0</code></i></p>

## What is Stable Diffusion?
`Stable Diffusion` is an AI artwork generator like `NovelAI` and `Midjourney`, but **open source** and **free** to use. 
User can input prompts, and the AI will generate artworks based on those prompts. 
Additionally, there are *a lot of* models and extensions available online for Stable Diffusion, that can achieve different styles, concepts or functions.

## Index
1. [Installation](#where-do-i-start)
2. [Embedding & LoRA](#embedding--lora)
3. [Terminologies](#tabs-explanations)
3. [Extensions](#extensions)
4. [Tips & Tricks](#tips--tricks)
5. [Model Training](#training)
6. [Learning Resources](#resources)

<hr>

## Where do I start?
The easiest, best, and most straightforward way to use Stable Diffusion is through a client called [webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) by **Automatic1111**. 
It is also available for [macOS w/ Apple Silicon](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon) too.
You will need to install **[Python 3.10](https://www.python.org/downloads/)** as well as **[git](https://git-scm.com/downloads)** first. 
You will also need a decent graphic card (GPU) with good amount of VRAM. 
There are also other popular user interfaces, such as [ComfyUI](https://github.com/comfyanonymous/ComfyUI) and [InvokeAI](https://github.com/invoke-ai/InvokeAI).
However, those come with their own pros and cons, and will not be covered in this guide as I’ve never used them.

**Note:** GoogleColab now blocks Stable Diffusion from running unless you use a paid subscription!

> Detailed [Installation Guide](misc/Installation.md)

>Add `--xformers` after `COMMANDLINE_ARGS=` in `webui-user.bat` to speed up the generation

>Add `--no-half-vae` after `COMMANDLINE_ARGS=` in `webui-user.bat` to prevent NaN images from generating

>Add `--medvram` after `COMMANDLINE_ARGS=` in `webui-user.bat` if you have less than **8GB** VRAM

## Finish Setting Up
After you follow the steps and install the client, if you didn’t download any model yourself beforehand, it would download a model automatically for you. 
The default model is `Stable-Diffusion-v1-5`, an official model made by **runwayml**, which is for general purposes as in you can generate both realistic images and cartoonish arts. 
However, if you mainly want to generate anime arts, I highly suggest you to download more dedicated models, such as [anything-v3.0](https://huggingface.co/Linaqruf/anything-v3.0/tree/main), or ~~shameless self promotion~~ [UHD-23](https://civitai.com/models/22371/uhd-23).
After downloading a model (mostly `.ckpt` or `.safetensors`), put them in the folder: `~\stable-diffusion-webui\models\Stable-diffusion`.
Optionally, you can then select between the models on the webui if you installed multiple.

>`.safetensors` is a new simple format for storing tensors safely (as opposed to `pickle`) while still being really fast. So always choose `safetensors` if available.

## Where can I find more Models?
Nowadays, the most popular model hosting site is called [CivitAI](https://civitai.com/). 
It hosts a lot of `Checkpoint`, as well as `Embedding` and `LoRA`.
Each model also has user comments, user ratings, and sample generations. 
So, you can check the reviews first before downloading the model.

> **`Checkpoint`** is basically the main "model" you run Stable Diffusion on. It has the biggest impact on the generation results. 

**Note:** Some models and sample images are automatically flagged by the system and thus hidden. So you may need to login to see more models.

## SD Versions
The majority of the Checkpoint models on CivitAI were trained on `Stable Diffusion v1.5`. 
This version of models is also the most widely used.
There had been newer versions of Stable Diffusion, namely `v2.1` and `XL`, released by `Stability AI` since.
Those were trained on a different dataset and techniques. 
Though as a result, they are considered inferior in quality by most of the community.
On top of that, some Extensions only work with one version and not the others. So make sure to look out for them when you're installing one.
All in all, unless you have very specific needs, just stick to `v1.5` models.

## VAE
**`VAE`** *(**V**ariational **A**uto**E**ncoder)* is responsible for converting the image from latent space. Every Checkpoint has a VAE baked in. 
However, you can also use other VAE of choice, such as [sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/tree/main). 
Different VAE may fix faces and hands, or produce more vibrant colors for example. You can force a specific VAE by going to `Settings` -> `Stable Diffusion` -> **`SD VAE`**.

## Embedding & LoRA
**`Embedding`** *(Textual Inversion)* and **`LoRA`** *(**Lo**w-**R**ank **A**daptation)* are essentially ways to constrain certain aspects (*Characters* or *Style*, etc.) of the generated images. 
> Here’s a detailed [technical explanation](https://youtu.be/dVjMiJsuR5o) on how they work if you’re interested. *(Just ignore the outdated conclusion.)*

Since LoRA is easier and takes less time to train, most people nowadays just train LoRA instead. 

#### To install them:

> Put **Embedding** in `~\stable-diffusion-webui\embeddings`

> Put **LoRA** in `~\stable-diffusion-webui\models\Lora`

#### To activate them: 
Click the red button (`Show extra networks`) under **Generate**, then press **Refresh**. 
Now you should be able to see the downloaded files in their respective tabs. Simply clicking the icon will add them into the prompt field.
Additionally, most LoRA also require you to add a certain **trigger words** for it to function, so check the page where you downloaded it to see more info. 
You can also adjust the strength of a LoRA by editing the number. 

- **Note:** Don’t use too many LoRA at once, it will start distorting the image.

- **Tip:** You can group the LoRAs by putting them in different sub-folders. They will then show up as buttons that you can press to filter on the webui.

- **Tip:** You can also add preview images for the models to easily identify them:
  - If a file is called `filename.safetensors`, just add an image named `filename.preview.png` in the same folder. Press **Refresh**. Then it should show up on the UI.

## LyCORIS
**`LyCORIS`** *(**L**ora be**Y**ond **C**onventional methods, **O**ther **R**ank adaptation **I**mplementations for **S**table diffusion)* is a more advanced and more efficient implementation of LoRA. *([Github](https://github.com/KohakuBlueleaf/LyCORIS))*

The main advantage is that, the file size can be really small *(~10MB compared to ~100MB)*, and seems to produce better effects while not impacting the art style too much.

On CivitAI, you can see if a model is LyCORIS or LoRA easily. To use LyCORIS, you need to first install this [extension](https://github.com/KohakuBlueleaf/a1111-sd-webui-lycoris). Then follow the same steps above to use it.

> Learn how to install [Extensions](#extensions)

> Put **LyCORIS** in `~\stable-diffusion-webui\models\LyCORIS`

## Tabs Explanations
- **`txt2img`:** Generate image based on input prompts
- **`img2img`:** Generate image based on an image along with prompts
- **`Extras`:** Upscale image
  - Use `R-ESRGAN 4x+ Anime6B` for anime generations
  - Use `R-ESRGAN_4x+` for realistic generations
  - Alternatively, you can download other models from [here](https://upscale.wiki/wiki/Model_Database) and put it into `~\stable-diffusion-webui\models\ESRGAN`
    - A popular model is `4x-UltraSharp.pth`
  - Use `LDSR` for the best result. But it takes *extremely* long to process
    - ***Note:** You need to manually download the models as instructed [here](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/10666)*
  - You can upscale the image using 2 upscalers, then blend them together with `Upscaler 2 visibility`
- **`PNG Info`:** You can upload an image to see what prompts and settings were used to generate it *(provided that the metadata was not removed)*
- **`Checkpoint Merger`:** ~~The easiest way to spam *something* onto CivitAI~~
- **`Train`:** Preprocess Images & Train Embeddings *(See [#](#embedding-training))*
- **`Settings`:** Settings 💀
- **`Extensions`:** Install & Manage Extensions *(See [#](#extensions))*

## Terms Explanations
- **`Prompt`:** The tags for stuffs you want in the output.
- **`Negative Prompt`:** The tags for stuffs you don’t want in the output.
- **`Sampling Method`:** The wizardry behind the scene. `Euler a` is fine. `DPM++ 2M series` are popular too. Basically, this slightly affects how the output look.
  - **Note:** Methods that that use *`Ancestral` (denote by `a` in the name)* may generate rather different results at different steps.
- **`Sampling Steps`:** How many iterations it does its wizardry. Low value causes the output to be blurry. High value suffers from diminishing return and takes longer.
- **`Restore Faces`:** Mainly used with realistic models to fix the faces.
- **`Tiling`:** Makes the output able to seamlessly tile. Useful for generating textures.
- **`Hires. Fix`:** The key that makes output significantly better.
- **`Width/Height`:** The resolution of the generated image. Keep it at `512x512` for `v1.5` models, `768x768` for `v2.x` models. *(Refer to [versions](#sd-versions) if you don't know what this means.)*
- **`Batch Count`:** How many batches to generate (in sequence).
- **`Batch Size`:** How many images per batch (in parallel). Require high VRAM.
- **`CFG Scale`:** How strong the prompts should influence the output. Low value generates random images; High value generates really distorted images.
- **`Seed`:** The random seed that affects how images are generated. If you use the same
seed, you should be able to get the same output when using the same prompts and settings.

## Before You Start
1. If you’re using anime models (eg. `anything-v3.0`), go to `Settings` -> `Stable Diffusion`, set **`Clip Skip`** to **`2`**.
2. In **positive** prompt, start with `high quality, best quality,` for the best results.
3. Additionally, you can add tags like `4k` and `hdr` to further improve the quality.
4. Download and install this **Embedding**, [EasyNegative.safetensors](https://huggingface.co/datasets/gsdf/EasyNegative/tree/main)
5. Add it along with `(bad quality, worst quality:1.2)` to the **negative** prompt.
6. Optionally, you can then save the default prompts from step 2 ~ 5 by clicking the save icon under **Generate** and give it a name. 
In the future, every time you launch webui you just need to load the Style.

## Recommended Workflow
Use `512x512` / `768x768` for rapid prototyping, until the composition (pose & background, etc.) is acceptable. 
Press the recycle icon to fix the `Seed`, then turn on `Hires. Fix` to upscale to higher resolution. Sometimes the upscaling process may mess up the composition again, 
so play around with the upscaler, steps and strength until the result is desired. Lastly, go to `Extra` tab to upscale the image again. 
Now you get a high resolution and detailed image!

## Brackets
- You can use `( )` to increase the influence of a prompt.
- You can use `[ ]` to decrease the influence of a prompt.
- You can also stack brackets to further influence, **e.g.** `[[foo]]`
  - Alternatively, use `(tag:ratio)`, **e.g.** `(bar:1.5)`
- **Example:**
`(long hair:1.5), [[straight hair]]` will try to always generate long hair, 
but the hair being straight or not is not a priority.

## Prompt Order
The order in which you enter the prompts **does** affect the generation results. For example:

- If you enter `<subject>, <background>` then it will first generate the subject then try to modify the background.
- If you enter `<background>, <subject>` then it will first generate the background, then try to fit in the subject.

<p align="center">
<img src="misc/Order.jpg" width=384>
</p>

# Extensions
Extensions are basically 3rd party tools not native to the webui, that aim to provide additional functions. 
You can go to the **Extensions** tab, click `Available`, then click `Load from`. This will load a list of popular extensions. You can then click **Install** to integrate them.
Alternatively, use `Install from URL` and paste in the link to a GitHub repo to install extensions not on the list.

**Note:** Every time you install new extensions, you need to restart the webui to load them properly. 
I recommend to close the browser and the CLI entirely and start again, as only restarting the UI sometimes may not work properly. 

### Control Net
[<--- link --->](ControlNet/README.md)

### Super Resolution Upscale
[<--- link --->](TiledVAE/README.md)

### Speed Up Generations
[<--- link --->](ToMe/README.md)

### Multiple Characters
[<--- link --->](MultiChara/README.md)

<h2><s> Shameless Self Promotion </s></h2>

### Prompt Format
[<--- link --->](https://github.com/Haoming02/sd-webui-prompt-format)

### Easy Tag Insert
[<--- link --->](https://github.com/Haoming02/sd-webui-easy-tag-insert)

### Dynamic HDR
[<--- link --->](https://github.com/Haoming02/sd-webui-dynamic-hdr)

# Tips & Tricks

### X/Y/Z Plot
[<--- link --->](XYZ/README.md)

### Themes
[<--- link --->](TipsTricks/README.md#themes)

### Default Values
[<--- link --->](TipsTricks/README.md#default-values)

### Noise Offset
[<--- link --->](TipsTricks/README.md#noise-offset)

### Logo Creations
[<--- link --->](TipsTricks/README.md#logo-creations)

### *Overclocking*
[<--- link --->](TipsTricks/Overclock.md)

# Training

### Embedding Training
~~*Train LoRA instead*~~
- [Video by Aitrepreneur](https://youtu.be/2ityl_dNRNw)
- [Video by OlivioSarikas](https://youtu.be/MLz0iM0M7Fk)

### LoRA Training
[<--- link --->](LoRATraining.md)

### LyCORIS Training
Follow the same steps as [LoRA Training](LoRATraining.md) above. Except:
- Choose `LyCORIS/LoHa` for the `LoRA type` parameter
- Use **low** `Dimonsion` and `Alpha`.
- *Play around with the Learning Rate / Scheduler / Warmup / Optimizer*

# Resources
- Reddit [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/)
- Webui [Features](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features)
- Youtube [Sebastian Kamph](https://www.youtube.com/@sebastiankamph/)
- YouTube [Aitrepreneur](https://www.youtube.com/@Aitrepreneur)
- Youtube [OlivioSarikas](https://www.youtube.com/@OlivioSarikas)

# Support Me!
If you like my works and wish to support me, you can buy me a [coffee](https://ko-fi.com/haoming).
Any donations will be greatly appreciated!

[![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)