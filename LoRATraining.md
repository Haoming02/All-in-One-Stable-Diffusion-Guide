<h1 align="center"> LoRA Training Tutorial</h1>
<p align="center"><b>by. <a href="https://civitai.com/user/HaomingGaming/models">Haoming</a></b><br><i>Last Update: 2023/06/02</i></p>
<p align="right"><i>corresponding webui version: <code>v21.5.11</code></i></p>

## Index
1. [Installation](#install-kohya-ss)
2. [Prepare Dataset](#prepare-dataset)
   1. [Resolution](#resolution)
   2. [Preparing Images](#preparing-images)
   3. [Captioning](#captioning)
3. [Configs](#configs)

<hr>

## Install Kohya SS
Just like `Stable Diffusion`, there is already a popular webui available: [Kohya SS](https://github.com/bmaltais/kohya_ss). 
Simply go to the repository and follow the installation steps. 
 
> Slightly Outdated [Video Tutorial](https://youtu.be/9MT1n97ITaE)

## Prepare Dataset
Now comes the most difficult part: preparing the dataset. As the good ol’ saying goes: 

> Garbage in, garbage out. 

If you didn’t prepare the dataset properly, the trained model will not produce good results. 
For training LoRA, the dataset refers to 2 things: the **images** and the **captions** for the images. 
The model can produce decent enough outcomes with less than a dozen images, though having more images does not increase the total training time by much, due to how the training is setup.
Furthermore, the more images and the more variety you have in the dataset, the more flexible the trained model will become. 

For example, having 10 images of your subject in different environments is significantly better than having 100 images of your subject in the exact same background and poses.

### Resolution:
Nowadays, the resolution of the images generally does not matter too much. 
You do not need to crop the images to a perfect square either. 
Simply tick the `Enable buckets` toggle and you're set.
A parameter below will dive more into this.

### Preparing Images:
As mentioned above, it is significantly better to have more varieties in the images, such as different background, lighting and poses, etc. Aspect ratio generally doesn’t matter too much thanks to `Buckets` as mentioned above. 
Personally, I recommend using only “official” arts, such as cards, in-game screenshots or promo images. Though many ~~lazy~~ people just scrape the internet for hundreds of fanarts instead... 
Once you finish preparing a dozen or so images with great varieties, proceed to the next step. 

### Captioning:
The caption file should be placed next to the corresponding image, and will work as long as the filenames match exactly.

> *`Kohya SS` used to not have anime-style captioning tool so I used `Automatic1111` instead, hence the old and new ways.*

#### New Way
On the **Kohya SS** webui, there is a **Utilities** tab with a **Captioning** section. For realistic images, use `BLIP`; for anime images, use `WD14`.
Enter the folder containing the images. The parameters can be left at default just fine. Then press `Caption images` to generate the `.txt` caption files.

**Note:** For `WD14`, there is a toggle called `Replace underscores in filenames with spaces`. Most anime checkpoints were trained on images from [Gelbooru](https://gelbooru.com/), which uses tags with underscores. 
So unless you know the checkpoint you're using was not trained with underscores, untick this toggle. 

> This tool does not modify the images or filenames

#### Old Way
*Another* way to mass caption all the images is to use the **Automatic1111** webui. In the **Train** tab, there is a section called **Preprocess Images**. 
Simply enter your folder that contains the image and a destination folder. 
And depending on your image, choose **`Deepbooru`** for anime; choose **`Blip`** for Realistic, then press **Preprocess**. 

> By default, this tool crops all images into squares. You can play around with the toggles to change this.

#### Manual Caption
Alternatively, if you want to manually caption the images, you can use [GenerateTxt.py](Scripts/) instead. 

**You’re not done yet!** 
Now you need to go through every single caption file and manually check the captions. You should **remove** every tag that describes your subject, keeping only the tags that are the “variables.” 
Think of it this way: You want the features of your subject to be associated with the model. 
Thus, when training a character for example, only caption the background, the expression of the subject, and the poses of the subject, etc. 
Last but not least, add some **trigger words** at the start of the captions. You can use [Insert.py](Scripts/) to automate this. 
The number of trigger words has to be consistent across your dataset. 

> For example, when I am training a character with multiple outfits, I put the character name first, the outfit name second, then the rest of the tags. Thus I have **2** trigger words for every single caption.

### Folder Structures
Create a folder to store your dataset. Inside it, create folders named in the format of `XXX_YYY`:

- The `XXX` is the number of steps per image. Generally, it takes few thousand steps to train a concept, depending on complexity. Divide that by the number of `epochs` *(explained below)*, then divide again by the number of images, to get `XXX`.
  - **eg.** To train `1500` steps in `10` epochs using `10` images, the `XXX` will be 1500 / 10 / 10 = `15`
- The `YYY` is the class of the images. It's basically a way to organize the images. 
  > Currently, I’m still unsure if `class` even affects the results.

So in the end, it will be something like:
```
Project
  |- 15_foo
      |- 01.png
      |- 01.txt
  |- 15_bar
      |- 02.png
      |- 02.txt
```

## Configs
>Remember to switch to the **LoRA** tab at the top first.

>Parameters that were not mentioned can just be left on default.

>Some authors on [CivitAI](https://civitai.com/) include their training parameters in the description, or even provide their datasets. 

### Source Model
- **Pretrained Model:** It’s better to pick a general checkpoint (**eg.** `anything-v3.0` or `SD v1.5`) instead of a finetuned one, so it is more likely to work on more checkpoints.
- **Save Model as:** `.safetensors`
- If the pretrained model is based on `SD 2.0`, check **v2**; for `SD 2.1`, check both **v2** and **v_parameterization**. *(Refer to [versions](README.md#sd-versions) if you don't know what this means.)*

### Folders
- **Image folder:** Enter the folder you created in the last step. Remember to link to the project folder, not the folders inside. 
- **Output folder:** The folder where the trained model should be saved to. You can just link to the `~\stable-diffusion-webui\models\Lora` folder.
- **Model output name**: Output model name 💀

### Training Parameters
- **Train Batch Size:** Basically means how many images does it train at once per step. Requires high VRAM to handle. However, you need to increase the **Epoch** count to compensate for it.
- **Epoch:** How many times should the training go through the entire dataset.
- **Caption Extension:** Set it to the correct extension. *(`.txt` if you used the webui tools)*
- **Mixed/Save Precision:** Only RTX 30 and 40 series support **`bf16`**; otherwise choose **`fp16`**.
  > Effect Unsure
- **Learning Rate / Scheduler / Warmup / Optimizer:**
    - Play around with the values, there is no "universal" answer. 
    - I used `0.00025` / `cosine` / `10%` / `AdamW8bit` for LoRA
    - Refer to the document below for what these do.
- **Network Rank:** How “complex” the concept is. `32 ~ 64` is normally enough for one character. Increase this value if you need the model to learn more concepts. *(Also affects the model file size.)*
- **Network Alpha:** Refer to the document below for what it does.

> Technical explanations of what the above parameters do: [Document feat. ChatGPT](misc/TechnicalTerms.pdf)

- **Max Resolution:** If your VRAM can handle, set `768,768`; otherwise `512,512`.
- **Enable Buckets:** Enable
- **Keep n tokens:** Refer to [Captioning](#captioning). Set it to the amount of **trigger words** you have.
- **Clip Skip:** `1` for realistic; `2` for anime.
- **Max Token Length:** 150
  > Effect Unsure
- **Shuffle caption:** Enable
- **Use xformers:** Enable
- **Noise offset:** Basically, this can help to generate brighter and darker scenes.
  > [Technical Explanations](https://youtu.be/cVxQmbf3q7Q)

## Press the **Train Model** button
- ~~*Pray you didn't waste an hour for nothing*~~
- After the training is finished, you can use [**`X/Y/Z Plot`**](XYZ/README.md) to evaluate the results.
