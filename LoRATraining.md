<h1 align="center"> LoRA Training Tutorial</h1>

<p align="center">
<b>by. <a href="https://civitai.com/user/HaomingGaming/models">Haoming</a></b><br>
<i>Last Update: 2024/01/25</i>
</p>

<p align="right">
<i>corresponding webui version: <code>v21.8.6</code></i><br>
<sup><i>commit: <code><a href="https://github.com/bmaltais/kohya_ss/commit/3cf80f8d68fbc9b9358e3b391432e5950b00f583">3cf80f8</a></code></i></sup>
</p>

## Index
1. [Getting Started](#kohya-ss)
2. [Dataset](#prepare-dataset)
   1. [Resolution](#resolution)
   2. [Preparing Images](#preparing-images)
   3. [Captioning](#captioning)
   4. [Folder Structures](#folder-structures)
3. [Configs](#configs)
    - [Training Parameters](TrainingParameters.md)

<hr>

## Kohya SS
Just like **Automatic1111**, there is already a popular webui for training available: [**Kohya SS**](https://github.com/bmaltais/kohya_ss). 
Simply go to the repository and follow the installation steps.

> There is also [OneTrainer](https://github.com/Nerogar/OneTrainer), though I have no experience with it.

## Prepare Dataset
Now comes the most important part: preparing the dataset. As the good ol’ saying goes: 

> Garbage in, garbage out. 

If you didn’t prepare the dataset properly, the trained model will not produce good results. 
The dataset refers to 2 things: the **images** and the **captions** for said images. 
The model can produce decent enough outcomes with less than a dozen images, 
but the more images with more variety you have in the dataset, the more flexible the model will become. 

### Resolution
You will need at least `512 x 512` for **SD 1.5** models; and at least `1024 x 1024` for **SDXL** models.
Aspect ratio does not matter too much, and there is no need to crop the images to a perfect square either. 
Simply tick the `Enable buckets` toggle and the tool will handle it for you.

### Preparing Images
As mentioned above, it is significantly better to have more varieties in the images, such as different background, lighting and poses, etc.  
Personally, I recommend using only “official” arts, such as cards, in-game screenshots or promo images. 
Once you finish preparing a dozen or so images with great varieties, proceed to the next step. 

### Captioning
The caption file should be placed within the same folder, next to the corresponding image.

On the **Kohya SS** webui, there is an **Utilities** tab with a **Captioning** section. For realistic images, use `BLIP`; for anime images, use `WD14`.
Enter the folder containing the images. The parameters can be left at default just fine. Then press `Caption images` to generate the `.txt` caption files.

**Note:** For `WD14`, there is a toggle called `Replace underscores in filenames with spaces`. Anime checkpoints were trained on [Booru](https://gelbooru.com/) tags. 
Consult the model page to see if it was trained with underscores or not. 

**You’re not done yet!** 

Now you need to go through every single caption file and manually check the captions. You should **remove** every tag that describes your subject, keeping only the tags that are the “variables.” 

Think of it this way: You want the features of your subject to be associated with the **trigger word**. 

So take training a character as an example: only caption the background, the expression of the subject, and the poses of the subject, etc; but not the hair color, eye color, or other defining features. 

Last but not least, add some **trigger words** at the start of the captions. You can use [Insert.py](Scripts/) to automate this. 
The number of trigger words has to be consistent across your dataset. 

> For example, when I am training a character with multiple outfits, I put the character name first, the outfit name second, then the rest of the tags. Thus I have **2** trigger words for every single caption.

### Folder Structures
Create a folder to store your dataset. Inside it, create folders named in the format of `XXX_YYY`:

- The `XXX` is the number of repeats per image. Generally, it takes few hundreds to a thousand steps to train a concept, depending on complexity. 
Divide that by the number of `epochs` *(explained below)*, then divide again by the number of images, to get `XXX`.
  - **eg.** To train `1000` steps in `10` epochs using `10` images, the `XXX` will be 1000 / 10 / 10 = `10`
- The `YYY` is the "class" of the images
  - Generally, put the most broad "category" of your subject. For example, use `1girl`/`1boy` when training an anime character.

In the end, it will be something like:
```
Project
  |- 15_foo
      |- 01.png
      |- 01.txt
  |- 20_bar
      |- 02.jpg
      |- 02.txt
```

## Configs
> Remember to switch to the **LoRA** tab at the top first.

> Parameters that were not mentioned can just be left at default.

### Source Model
- **Model Quick Pick:** You can select from the official ones, or choose `custom` and select your local checkpoint of choice. 
It’s better to pick a more general checkpoint instead of a more finetuned one, so that it is more likely to work on more checkpoints.
- **Save Model as:** `.safetensors`
- If the source model is **SDXL**, also enable the `SDXL Model` toggle *(Refer to [versions](README.md#sd-versions) if you don't know what this mean.)*
  > ~~If the source model is **SD 2**... why...?~~

### Folders
- **Image folder:** Enter the folder you created in the previous step. Remember to link to the project folder, not the folders inside. 
- **Output folder:** The folder where the trained model should be saved to. You can just link to the `~webui\models\Lora` folder.
- **Model output name**: Model output name 💀

### Parameters
- **LoRA Type:** You can choose between training a normal **LoRA** or a [**LyCORIS**](https://github.com/KohakuBlueleaf/LyCORIS) model
- **Train Batch Size:** How many images does it train at once per step. Requires high VRAM to handle. 
    - Increasing this would "smooth out" the changes between each **Epoch**
    - You need to also increase the **Epoch** count to compensate for it
- **Epoch:** How many times should the training go through the entire dataset
- **Caption Extension:** Set it to the correct extension *(`.txt` if you used the Utilities)*
- **Mixed/Save Precision:** Only RTX 30 and 40 series support **`bf16`**; otherwise choose **`fp16`**
- **Learning Rate / Scheduler / Warmup / Optimizer:**
    > See [Training Parameters](TrainingParameters.md)
- **Network Rank:** How “complex” the concept is. `32 ~ 64` for **SD 1.5** and `16` for **SDXL** is usually enough. 
Increase this value if you need the model to learn more concepts. 
    - This also affects the final model file size
    - **LyCORIS** models need lower value
- **Network Alpha:** Setting it to half of **Network Rank** is usually fine
- **Gradient accumulate steps:** Only increase this if you also want to use high **Train Batch Size**
    - Reduce memory usage but also decrease training speed
- **Max Resolution:** For **SDXL**, set to `1024,1024`; For **SD 1.5**, if your VRAM can handle, set to `768,768`; otherwise `512,512`.
- **Enable Buckets:** Enable
- **Keep n tokens:** Refer to [Captioning](#captioning). Set it to the number of **trigger words** you used.
- **Clip Skip:** `1` for realistic or **SDXL**; `2` for anime.
- **Gradient checkpointing:** Enable this if you're barely Out of Memory
    - Slightly reduce memory usage and slightly decrease training speed
- **Shuffle caption:** Enable
- **Use xformers:** Enable
- **Noise offset:** Basically, this helps adapting to brighter and darker scenes
    - Supposedly, SDXL was trained with `0.0357` offset and `0.00357` scale
    > [Technical Explanations](https://youtu.be/cVxQmbf3q7Q)

## Press the **Start Training** button
~~Pray you didn't waste an hour for nothing~~

After the training is finished, you can use [**`X/Y/Z Plot`**](XYZ/README.md) to evaluate the results.
