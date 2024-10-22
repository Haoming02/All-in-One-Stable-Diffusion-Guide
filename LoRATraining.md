<h1 align="center">LoRA Training Tutorial</h1>
<p align="center">
<b>by. <a href="https://civitai.com/user/HaomingGaming">Haoming</a></b><br>
<i>Last Update: 2024/10/22</i>
</p>

<p align="right">
<sup><i>corresponding <a href="https://github.com/bmaltais/kohya_ss">Webui</a> version: <code>v24.1.7</code></i></sup>
</p>

<details open>
<summary><h2>Index</h2></summary>

1. [Getting Started](#getting-started)
2. [Dataset](#prepare-dataset)
    - [Images](#images)
    - [Captions](#captions)
3. [Folder Structures](#folder-structures)
4. [Configs](#configs)
    - [Parameters](#parameters)

</details>

## Getting Started
Just like with generation, there is also a popular Webui for training: **[Kohya_SS](https://github.com/bmaltais/kohya_ss)**. Simply go to the repository and follow the installation steps.

> (The UI is maintained by <ins>bmaltais</ins>, and internally calls the [sd-scripts](https://github.com/kohya-ss/sd-scripts) written by <ins>kohya-ss</ins>)

> [!TIP]
> There are also other training UIs, such as [OneTrainer](https://github.com/Nerogar/OneTrainer), [AI Toolkit](https://github.com/ostris/ai-toolkit), and [Flux Gym](https://github.com/cocktailpeanut/fluxgym). Though I personally do not have much experience with them.

## Prepare Dataset
Now comes the most important part, preparing the dataset. If you didn’t prepare the dataset properly, the trained model will not produce good results, just as the good ol’ saying goes:

> ***"Garbage in, garbage out."***

The dataset refers to 2 things: the **images** and the **captions** for said images.

### Images
You can train a decent LoRA with just a dozen images. The more important part is the variety of the images, such as different backgrounds, lighting, and poses. **i.e.**, quality over quantity. **Personally**, I recommend using only “official” images, such as card carts, in-game screenshots, or promo posters.

The resolution of the images should be around `512 x 512` for **SD1** models; and at least `1024 x 1024` for **SDXL** and **Flux** models. The aspect ratio of each image does not matter. Simply enable the `Enable buckets` option, and the tool will handle them for you. No longer need to crop the images into perfect squares.

> [!TIP]
> See [Architecture](./README.md#architecture) if you don't know what the **versions** mean

Once you finish preparing the images, proceed to the next step:

### Captions
You can train a decent LoRA without any captions at all; however, having captions can drastically improve the flexibility of the model. You can manually write the descriptions of the images; or use tagging tools to automatically generate captions for an entire folder of images, such as the [WD series](https://huggingface.co/SmilingWolf/wd-swinv2-tagger-v3) for anime checkpoints, or [Florence-2](https://huggingface.co/microsoft/Florence-2-large) for realistic checkpoints. Caption file should be placed next to its corresponding image, with the same filename in `.txt` extension.

**You’re not done yet!**

Next, you need to go through every single caption file and manually prune the captions. You should **remove** every tag that describes your subject, keeping only the tags that are the “variables.” Think of it this way: the LoRA should learn to associate the features of your subject with its "**trigger words**."

**Trigger Words** are keywords that you add into the captions, so that the LoRA will learn to recreate the concept when the keywords are present in the prompt. Usually, the trigger word would be the name of the character or the style.

> [!TIP]
> When training a LoRA for anime checkpoints, due to how **Booru Tags** are formatted, you should put the trigger words at the start of the captions. Additionally, the number of trigger words should be consistent across the entire dataset.

- **TL;DR:**
    - Take training a character LoRA as example: Only caption the background, the expression of the subject, and the poses of the subject; not the hair color, eye color, or other defining features.
    - Personally, when I am training a character with multiple outfits, I put the character name first, the outfit name second, then the rest of the tags. Thus, I have **2** trigger words for every single caption.

## Folder Structures
> This structure is specific to **Kohya_SS**

- Create a <ins>project folder</ins> to store your dataset. Inside it, create folders named in the format of `XXX_YYY`:
    - The `XXX` is the number of repeats per image. Generally, it takes around a thousand steps to train a concept, depending on its complexity. Divide that by the number of `epochs` and the number of images, and then multiply by the `batch size`, to get `XXX`.
        - **eg.** To train `1000` steps in `10` epochs using `10` images at a batch size of `2`, the `XXX` will be `1000 / 10 / 10 * 2` = **`20`**
    - The `YYY` is the "class" of the images, basically the most broad "category" of your subject.
        - **eg.** `man` or `woman`

In the end, it will be something like:
```
Project
  |- 12_foo
      |- 01.png
      |- 01.txt
      |- ...
  |- 16_bar
      |- 02.jpg
      |- 02.txt
      |- ...
```

## Configs

> [!TIP]
> Remember to switch to the **LoRA** tab at the top first

> [!NOTE]
> Parameters that were not mentioned can just be left at default

### Configuration

- You can save the following settings into a `.json` file, and simply load it again in future trainings

### Accelerate Launch

- **Mixed precision:** If you have a RTX 30 series or later GPU, select `bf16`; otherwise select `fp16`

- **Dynamo backend:** Try setting it to `inductor` and see if your GPU supports it; otherwise leave it at `no`

### Model
- **Pretrained model name or path:** Click the `📄` button, and select a checkpoint of choice. Recommended to pick a more general checkpoint instead of a more finetuned one, so that it is flexible to work on more checkpoints.
    - If the model is **SDXL**, also enable the `SDXL` checkbox
- **Image folder:** Enter the path to the <ins>project folder</ins> *(**not** the sub-folders)*
- **Trained Model output name:** The name of the LoRA
- **Save trained model as:** `.safetensors`
- **Save precision:** Same as **Mixed precision** above

### Folders

- **Output directory for trained model:** The folder where the LoRA should be saved to *(You can simply link to the `~webui\models\Lora` folder)*

### Parameters
- **LoRA Type:** You can choose between training a LoRA or a [LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS) model
    - Keep it at `Standard` when you are starting out
- **Train Batch Size:** How many images does it train at once every step
    - Increasing this would "smooth out" the changes between each **Epoch**
    - You may need to increase the **Epoch** count to compensate for it
- **Epoch:** How many times should the training go through the entire dataset
- **Max train steps:** I set this to `0` cause my step count is determined by **Epoch** instead
- **Caption file extension:** `.txt`
- **Learning Rate / Scheduler / Optimizer:**
    - See [Training Parameters](TrainingParameters.md)
- **Max resolution:** For **SDXL**, set to `1024,1024`; For **SD1**, set to `768,768` if VRAM is sufficient; otherwise `512,512`.

> [!TIP]
> See [Architecture](./README.md#architecture) if you don't know what the **version** mean

- **Enable buckets:** `true`
- **Network Rank:** How “complex” the concept is
    - You do **not** need more than `32` for the vast majority of cases. Do not blindly follow random YouTube tutorials where they set it to super high values, generating junks that are hundreds of MBs in size, wasting everyone's time and space...
    - I was able to train LoRA for a single character with multiple outfits at just `4`; a pack LoRA with three characters at just `8`; and a pack LoRA with ten characters at `32`
- **Network Alpha:** Setting it to half of **Network Rank** is usually fine
- **Keep n tokens:** For realistic checkpoints, set it to `0`; for anime checkpoints, set it to the number of **trigger words** you have
    - See [Captions](#captions)
- **Clip Skip:** `1` for realistic checkpoints; `2` for anime checkpoints
- **Gradient checkpointing:** Enable this if you're getting **Out of Memory** errors
- **Shuffle caption:** `true` for anime checkpoints; `false` otherwise
    - This doesn't make sense for natural sentences after all
- **CrossAttention:** `xformers`
- **Debiased Estimation loss:** `true`; helps with color
- **Noise offset:** Basically, this helps adapting to brighter and darker scenes
    - I set it to `0.02`
    - Do **not** set this too high, or you will get extremely contrasty "AI" look...
- **Adaptive noise scale:** Set this to `1 / 10` of **Noise offset**
    - So `0.002` in my case

<h2>Press the <ins>Start training</ins> button</h2>

- ~~Pray that you don't waste an hour for nothing~~
- After the training is finished, you can use [X/Y/Z Plot](Tips/XYZ.md) to evaluate the results

<hr>

#### See Also
- **English:** https://github.com/darkstorm2150/sd-scripts/blob/main/docs/train_README-en.md
- **Japanese:** https://github.com/kohya-ss/sd-scripts/blob/main/docs/train_README-jp.md
- **Chinese:** https://github.com/kohya-ss/sd-scripts/blob/main/docs/train_README-zh.md
