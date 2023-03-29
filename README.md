# Stable Diffusion All-in-One Guides
***by. Haoming 2023/03/29***

## What is Stable Diffusion?
`Stable Diffusion` is an AI artwork generator like `NovelAI` and `Midjourney`, but __**open source**__ and **free** to use. 
User can input prompts (keywords), and the AI will generate artworks based on those prompts. 
Additionally, there are *a lot of* models and extensions available online for Stable Diffusion, 
that can achieve different styles, concepts or functions.

## Where do I start?
The easiest, best, and most straightforward way to use Stable Diffusion is through a client called [webui by Automatic1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui). 
It is also available for macOS w/ [Apple Silicon](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon) too apparently.
You will need to download **[Python3.10](https://www.python.org/downloads/)** as well as **[git](https://git-scm.com/downloads)** first. 
Then clone (download) the repository to a folder of choice. You will also need a decent graphic card (GPU) with high amount of VRAM. 
Alternatively, there are also GoogleColab versions of the client that you can run online. 
But those come with other problems, and will not be covered in this guide as I’ve never used any of them.

>Add `--xformers` after `COMMANDLINE_ARGS=` in `webui-user.bat` to speed up the generation

>Add `--medvram` after `COMMANDLINE_ARGS=` in `webui-user.bat` if you have less than **8GB** VRAM

## How do I start?
When you follow the steps and install the client, if you didn’t download any model yourself beforehand, 
then the script would download a model automatically for you. The model is `Stable-Diffusion-v1-5`, an official model made by **StabilityAI**. 
And it is for general purposes, as in you can generate both realistic arts and anime arts. Though, if you mainly want to generate anime arts, 
I suggest you to download more dedicated models, such as [`anything-v3.0`](https://huggingface.co/Linaqruf/anything-v3.0/tree/main), or ~~shameless self promotion~~ [`UHD-23`](https://civitai.com/models/22371/uhd-23).
After downloading the model (`.ckpt` or `.safetensors`), put them in the folder: `~\stable-diffusion-webui\models\Stable-diffusion`.
Then, you can select the model on the webui.

>`.safetensors` does not contain malicious codes, so always choose it if available

## Where can I find more Models?
Nowadays, the most popular model hosting site is called [CivitAI](https://civitai.com/). 
It hosts a lot of checkpoints, as well as `Embedding` and `LoRA` (will be explained below). 
Each model also has user comments, user ratings, and example generations. So, you can check the samples first before downloading the model.

## What is Embedding & LoRA
`Embedding` (`Textual Inversion`) and `LoRA` are essentially ways to constrain certain aspects (*Characters* or *Style*, etc.) of the generated images. 
Here’s a really detailed [explanation](https://youtu.be/dVjMiJsuR5o) on how they work if you’re interested in technical stuffs. 
Since LoRA takes significantly less time to train *(~4 times faster than Textual Inversion)*, most people nowadays just train LoRA instead. 
To install them:

> Put **Embedding** in `~\stable-diffusion-webui\embeddings`

> Put **LoRA** in `~\stable-diffusion-webui\models\Lora`

To activate them, click the red button (`Show extra networks`) under **Generate**, then press **Refresh**. 
Now you should be able to see the downloaded files in their respective tabs. Simply clicking the icon will add them into the prompt field.
Additionally, most LoRA also requires you to add a certain **trigger words** for it to function, 
check the page where you downloaded it to see more info. You can also adjust the strength of a LoRA by editing the number. 

**Note:** Don’t use too many LoRA at once, it will start distorting the image. `CFG` also somewhat affects it, so play around with the numbers.

## Tab Explanations:
- **`txt2img`:** Generate image based on input prompts
- **`img2img`:** Generate image based on an image along with prompts
- **`Extras`:** Upscale image
  - Use `R-ESRGAN 4x+ Anime6B` for anime generations
  - Use `R-ESRGAN_4x+` for realistic generations
  - Alternatively, download [`4x-UltraSharp`](https://upscale.wiki/wiki/Model_Database) and put it into `~\stable-diffusion-webui\models\ESRGAN`
  - Use `LDSR` for the best result. But it takes *extremely* long to process
  - You can upscale the image using both upscalers, then blend them together with `Upscaler 2 visibility`
- **`PNG Info`:** You can upload an image to see what prompts were used to generate it *(provided that the metadata was not removed)*
- **`Checkpoint Merger`:** ~~The easiest way to *create* something to upload to CivitAI~~
- **`Train`:** Preprocess Images & Train Embeddings
- **`Settings`:** Settings `:skull:`
- **`Extensions`:** Install & manage Extensions

## Term Explanations:
- **`Prompt`:** The tags for stuffs you want in the output.
- **`Negative Prompt`:** The tags for stuffs you don’t want in the output.
- **`Sampling Method`:** The wizardry behind the scene. `Euler a` is fine. `DPM++ 2M Karras` is
popular too. `DPM++ SDE Karras` is supposedly better, but also slower. 
Basically, this slightly affects how the output look.
- **`Sampling Steps`:** How many iterations it does its wizardry. Low value causes the output to be blurry. High value suffers from diminishing return and takes longer. `20 - 50` is mostly fine.
- **`Restore Faces`:** Mainly used with realistic models to fix the faces.
- **`Tiling`:** Makes the output able to seamlessly tile. Useful for generating textures.
- **`Hires. Fix`:** The key that makes output significantly better.
- **`Width/Height`:** The resolution of the generated image. Keep it at `512x512` for `v1.5` models, `768x768` for `v2.0` models. 
- **`Batch Count`:** How many batches to generate (in sequence).
- **`Batch Size`:** How many images per batch (in parallel). Will need high VRAM.
- **`CFG Scale`:** How strong the prompts should influence the output. Low value generates random images; High value generates really distorted images. `7 – 14` is fine.
- **`Seed`:** The random seed that affects how images are generated. If you use the same
seed, you should be able to get the same output when using the same prompts and settings.

## Prompts Tips & Setting Guides
1. If you’re using anime models (eg. `anything-v3.0`), go to `Settings` -> `Stable Diffusion`, set **`Clip Skip`** to **`2`**.
2. In positive prompt, start with `best quality, masterpiece,` for the best results.
3. Download and install this embedding, [EasyNegative.safetensors](https://huggingface.co/datasets/gsdf/EasyNegative/tree/main)
4. Add it to the negative prompt. *(You can experiment the results with and without this)*
5. Optionally, you can then save the default prompts from step 2 and step 4 by clicking the save icon under **Generate** and give it a name. 
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

## Advanced Functions

### XYZ Plots
*Coming Soon^TM^*

### Control Net
*Coming Soon^TM^*

### Extensions
*Coming Soon^TM^*

## Training

### Embedding Training
~~Use LoRA instead~~

### LoRA Training
*Coming Soon^TM^*

### LyCORIS
*Coming Soon^TM^*

## Resources
- Reddit [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/)
- YouTube [Aitrepreneur](https://www.youtube.com/@Aitrepreneur)
- Youtube [OlivioSarikas](https://www.youtube.com/@OlivioSarikas)