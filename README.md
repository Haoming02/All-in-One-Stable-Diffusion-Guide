<p align="center"><img src="misc/Banner.jpg" alt="Stable Diffusion All-in-One Guide"></p>
<p align="center"><i>by. Haoming 2023/04/20</i></p>

## What is Stable Diffusion?
`Stable Diffusion` is an AI artwork generator like `NovelAI` and `Midjourney`, but **open source** and **free** to use. 
User can input prompts (keywords), and the AI will generate artworks based on those prompts. 
Additionally, there are *a lot of* models and extensions available online for Stable Diffusion, 
that can achieve different styles, concepts or functions.

## Where do I start?
The easiest, best, and most straightforward way to use Stable Diffusion is through a client called [webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) by **Automatic1111**. 
It is also available for [macOS w/ Apple Silicon](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon) too apparently.
You will need to download **[Python3.10](https://www.python.org/downloads/)** as well as **[git](https://git-scm.com/downloads)** first. 
Then clone *(download)* the repository to a folder of choice. You will need a decent graphic card (GPU) with high amount of VRAM. 
There are also other popular webui, such as [ComfyUI](https://github.com/comfyanonymous/ComfyUI) or [InvokeAI](https://github.com/invoke-ai/InvokeAI).
Alternatively, there is a GoogleColab version of the client that you can run online without the need of high-end graphic card.
However, the above have their own pros and cons, and will not be covered in this guide as I’ve never used any of them.

>Add `--xformers` after `COMMANDLINE_ARGS=` in `webui-user.bat` to speed up the generation

>Add `--medvram` after `COMMANDLINE_ARGS=` in `webui-user.bat` if you have less than **8GB** VRAM

## How do I start?
When you follow the steps and install the client, if you didn’t download any model yourself beforehand, 
then the script would download a model automatically for you. The model is `Stable-Diffusion-v1-5`, an official model made by **runwayml**. 
And it is for general purposes, as in you can generate both realistic arts and anime arts. Though, if you mainly want to generate anime arts, 
I suggest you to download more dedicated models, such as [anything-v3.0](https://huggingface.co/Linaqruf/anything-v3.0/tree/main), or ~~shameless self promotion~~ [UHD-23](https://civitai.com/models/22371/uhd-23).
After downloading the model (`.ckpt` or `.safetensors`), put them in the folder: `~\stable-diffusion-webui\models\Stable-diffusion`.
Then, you can select the model on the webui.

>`.safetensors` is a new simple format for storing tensors safely (as opposed to `pickle`) while still being really fast. So always choose `safetensors` if available.

## Where can I find more Models?
Nowadays, the most popular model hosting site is called [CivitAI](https://civitai.com/). 
It hosts a lot of `Checkpoints`, as well as `Embedding` and `LoRA`.
Each model also has user comments, user ratings, and example generations. So, you can check the samples first before downloading the model.

**Note:** Many models and sample images are automatically-flagged by the system and thus hidden. So you may need to login to see more models.

## SD Versions
The majority of the Checkpoint models on CivitAI were trained on `Stable Diffusion v1.5`. 
This version of models is also the most widely used.
There had been newer versions of Stable Diffusion, namely `v2.1` and `XL`, released by `Stability AI` since.
Those were trained on a different dataset and techniques. 
Though as a result, they are considered inferior in quality by most of the community.
On top of that, some Extensions only work with one version. So make sure to look out for them when you're installing one.
All in all, unless you have specific needs, just stick to `v1.5` models.

## Embedding & LoRA
`Embedding` (`Textual Inversion`) and `LoRA` are essentially ways to constrain certain aspects (*Characters* or *Style*, etc.) of the generated images. 
Here’s a really detailed [explanation](https://youtu.be/dVjMiJsuR5o) on how they work if you’re interested in technical stuffs *(Just ignore the outdated conclusion.)*
Since LoRA takes significantly less time to train *(~4 times faster than Textual Inversion)*, most people nowadays just train LoRA instead. 
To install them:

> Put **Embedding** in `~\stable-diffusion-webui\embeddings`

> Put **LoRA** in `~\stable-diffusion-webui\models\Lora`

To activate them, click the red button (`Show extra networks`) under **Generate**, then press **Refresh**. 
Now you should be able to see the downloaded files in their respective tabs. Simply clicking the icon will add them into the prompt field.
Additionally, most LoRA also requires you to add a certain **trigger words** for it to function, 
check the page where you downloaded it to see more info. You can also adjust the strength of a LoRA by editing the number. 

**Note:** Don’t use too many LoRA at once, it will start distorting the image.

**Tip:** You can group the LoRAs by putting them in different sub-folders. They will then show up as tabs on the webui.

## Tab Explanations:
- **`txt2img`:** Generate image based on input prompts
- **`img2img`:** Generate image based on an image along with prompts
- **`Extras`:** Upscale image
  - Use `R-ESRGAN 4x+ Anime6B` for anime generations
  - Use `R-ESRGAN_4x+` for realistic generations
  - Alternatively, you can download other models from [here](https://upscale.wiki/wiki/Model_Database) and put it into `~\stable-diffusion-webui\models\ESRGAN`
    - A popular model is `4x-UltraSharp.pth`
  - Use `LDSR` for the best result. But it takes *extremely* long to process
  - You can upscale the image using 2 upscalers, then blend them together with `Upscaler 2 visibility`
- **`PNG Info`:** You can upload an image to see what prompts were used to generate it *(provided that the metadata was not removed)*
- **`Checkpoint Merger`:** ~~The easiest way to *create* something for uploading to CivitAI~~
- **`Train`:** Preprocess Images & Train Embeddings
- **`Settings`:** Settings 💀
- **`Extensions`:** Install & Manage Extensions

## Term Explanations:
- **`Prompt`:** The tags for stuffs you want in the output.
- **`Negative Prompt`:** The tags for stuffs you don’t want in the output.
- **`Sampling Method`:** The wizardry behind the scene. `Euler a` is fine. `DPM++ 2M series` are popular too. Basically, this slightly affects how the output look.
  - **Note:** Methods that that use `Ancestral` *(denote by `a` in the name)* may generate vastly different results at different steps.
- **`Sampling Steps`:** How many iterations it does its wizardry. Low value causes the output to be blurry. High value suffers from diminishing return and takes longer. `20 - 50` is mostly fine.
- **`Restore Faces`:** Mainly used with realistic models to fix the faces.
- **`Tiling`:** Makes the output able to seamlessly tile. Useful for generating textures.
- **`Hires. Fix`:** The key that makes output significantly better.
- **`Width/Height`:** The resolution of the generated image. Keep it at `512x512` for `v1.5` models, `768x768` for `v2.x` models. *(Refer to [versions](#sd-versions) if you don't know what they are.)*
- **`Batch Count`:** How many batches to generate (in sequence).
- **`Batch Size`:** How many images per batch (in parallel). Will need high VRAM.
- **`CFG Scale`:** How strong the prompts should influence the output. Low value generates random images; High value generates really distorted images. `7 – 14` is fine.
- **`Seed`:** The random seed that affects how images are generated. If you use the same
seed, you should be able to get the same output when using the same prompts and settings.

## Prompts Tips & Setting Guides
1. If you’re using anime models (eg. `anything-v3.0`), go to `Settings` -> `Stable Diffusion`, set **`Clip Skip`** to **`2`**.
2. In positive prompt, start with `best quality, masterpiece,` for the best results.
3. Download and install this embedding, [EasyNegative.safetensors](https://huggingface.co/datasets/gsdf/EasyNegative/tree/main)
4. Add it along with `(bad quality, worst quality:1.2)` to the **negative** prompt.
5. Optionally, you can then save the default prompts from step 2 ~ 4 by clicking the save icon under **Generate** and give it a name. 
In the future, every time you launch Stable Diffusion, you just need to load the Style.

## Brackets
- You can use `( )` to increase the influence of a prompt.
- You can use `[ ]` to decrease the influence of a prompt.
- You can also stack brackets to further influence, **e.g.** `[[foo]]`
- Alternatively, use `tag:ratio`, **e.g.** `(bar:1.5)`
- **Example:**
`(long hair:1.5), [[straight hair]]` will try to always generate long
hair, but the hair being straight or not is not a priority.

## Recommended Workflow
Use `512x512 ~ 768x768` for rapid prototyping, until the composition (pose & background, etc.) is acceptable. 
Press the recycle icon to fix the `Seed`, then turn on `Hires. Fix` to upscale to higher resolution. Sometimes the upscaling process may mess up the composition again, 
so play around with the steps and strength until the result is desired. Lastly, go to `Extra` tab to upscale the image again. 
Now you get a high resolution and detailed image!

# Advanced Topics
There are tens of papers published for Stable Diffusion almost every single week. [Refer](#resources) to YouTube or Reddit for the latest news and technologies.

### Extensions
Extensions are basically 3rd party tools which were not native to the webui, that aim to provide additional functions. 
You can go to the **Extensions** tab, click `Available`, then click `Load from`. This will generate a list of popular extensions. You can then click **Install** to integrate them.
Alternatively, use `Install from URL` and paste in the link to a GitHub repo to install extensions not on the list. Some of the topics below require extensions.

**Note:** Every time you install new extensions, you need to restart the webui to load them properly. 
I recommend to close the browser and the cmd window entirely and start again, since only restarting the UI may not work properly sometimes. 

### X/Y/Z Plot
[<--- link --->](XYZ/README.md)

### Multiple Characters
[<--- link --->](MultiChara/README.md)

### Control Net
[<--- link --->](ControlNet/README.md)

# Tips & Tricks

### Extra Details
[<--- link --->](TipsTricks/ExtraDetail.md)

### Themes
You can write **CSS** scripts, or download ones made by others such as [Catppuccin](https://github.com/catppuccin/stable-diffusion-webui), 
and then save as `user.css` in the same directory to change how the webui looks.

### *More Coming Soon*

# Training

### Embedding Training
~~*Train LoRA instead*~~
- [Video by Aitrepreneur](https://youtu.be/2ityl_dNRNw)
- [Video by OlivioSarikas](https://youtu.be/MLz0iM0M7Fk)

### LoRA Training
[<--- link --->](LoRATraining.md)

### LyCORIS
- [Github](https://github.com/KohakuBlueleaf/LyCORIS)
- *Coming Soon?*

# Resources
- Reddit [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/)
- YouTube [Aitrepreneur](https://www.youtube.com/@Aitrepreneur)
- Youtube [OlivioSarikas](https://www.youtube.com/@OlivioSarikas)
- Youtube [Sebastian Kamph](https://www.youtube.com/@sebastiankamph/)
- Webui [Features](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features)

# Support Me!
If you like my works and wish to support me, you can do so on [ko-fi](https://ko-fi.com/haoming). Any donations will be greatly appreciated.