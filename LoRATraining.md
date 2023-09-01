<h1 align="center"> LoRA Training Tutorial</h1>
<p align="center"><b>by. <a href="https://civitai.com/user/HaomingGaming/models">Haoming</a></b><br><i>Last Update: 2023/09/01</i></p>
<p align="right"><i>corresponding webui version: <code>v21.8.6</code></i></p>

## Index
1. [Installation](#kohya-ss)
2. [Dataset](#prepare-dataset)
   1. [Resolution](#resolution)
   2. [Preparing Images](#preparing-images)
   3. [Captioning](#captioning)
   4. [Folder Structures](#folder-structures)
3. [Configs](#configs)

> Slightly Outdated [Video Tutorial](https://youtu.be/9MT1n97ITaE)

<hr>

## Kohya SS
Just like **Automatic1111**, there is already a popular webui for training available: [Kohya SS](https://github.com/bmaltais/kohya_ss). 
Simply go to the repository and follow the installation steps.  

## Prepare Dataset
Now comes the most difficult part: preparing the dataset. As the good ol’ saying goes: 

> Garbage in, garbage out. 

If you didn’t prepare the dataset properly, the trained model will not produce good results. 
The dataset refers to 2 things: the **images** and the **captions** for said images. 
The model can produce decent enough outcomes with less than a dozen images, but the more images and the more variety you have in the dataset, the more flexible the model will become. 

### Resolution
You will need at least `512 x 512` for `v1.5` models; and `1024 x 1024` for `XL` models.
Aspect ratio does not matter too much, and there is no need to crop the images to a perfect square either. 
Simply tick the `Enable buckets` toggle and the tool will handle it for you.

### Preparing Images
As mentioned above, it is significantly better to have more varieties in the images, such as different background, lighting and poses, etc. 
Aspect ratio generally doesn’t matter too much thanks to `Buckets` as mentioned above. 
Personally, I recommend using only “official” arts, such as cards, in-game screenshots or promo images. 
Once you finish preparing a dozen or so images with great varieties, proceed to the next step. 

### Captioning
The caption file should be placed within the same folder, next to the corresponding image.

On the **Kohya SS** webui, there is an **Utilities** tab with a **Captioning** section. For realistic images, use `BLIP`; for anime images, use `WD14`.
Enter the folder containing the images. The parameters can be left at default just fine. Then press `Caption images` to generate the `.txt` caption files.

**Note:** For `WD14`, there is a toggle called `Replace underscores in filenames with spaces`. Most anime checkpoints were trained on images from [Gelbooru](https://gelbooru.com/), which uses tags with underscores. 
So unless you know the checkpoint you're using was not trained with underscores, untick this toggle. 

##### Manual Caption
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
  > Currently, I’m unsure if `class` even affects the results.

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

>Parameters that were not mentioned can just be left at default.

### Source Model
- **Model Quick Pick:** You can select from the official ones, or choose `custom` and select other checkpoint of choice. It’s better to pick a general checkpoint (**eg.** `anything-v3.0`) instead of a more finetuned one, so that it is more likely to work on more checkpoints.
- **Save Model as:** `.safetensors`
- If the pretrained model is based on `SD 2.0`, check **v2**; for `SD 2.1`, check both **v2** and **v_parameterization**; for `SDXL`, check `SDXL Model` instead. *(Refer to [versions](README.md#sd-versions) if you don't know what these mean.)*

### Folders
- **Image folder:** Enter the folder you created in the last step. Remember to link to the project folder, not the folders inside. 
- **Output folder:** The folder where the trained model should be saved to. You can just link to the `~webui\models\Lora` folder.
- **Model output name**: Output model name 💀

### Training Parameters
- **LoRA Type:** You can choose between training a normal **LoRA** or a [**LyCORIS**](https://github.com/KohakuBlueleaf/LyCORIS) model
- **Train Batch Size:** Basically means how many images does it train at once per step. Requires high VRAM to handle. *You also need to increase the **Epoch** count to compensate for it.*
- **Epoch:** How many times should the training go through the entire dataset.
- **Caption Extension:** Set it to the correct extension. *(`.txt` if you used the webui utilities)*
- **Mixed/Save Precision:** Only RTX 30 and 40 series support **`bf16`**; otherwise choose **`fp16`**.
- **Learning Rate / Scheduler / Warmup / Optimizer:**
    - Play around with the values, there is no "universal" answer.
    - If you use **`Adafactor`** or **`Prodigy`** Optimizer, set the learning rate to 1, as it will be automatically adjusted during training. 
- **Network Rank:** How “complex” the concept is. `32 ~ 64` is normally enough for one character. Increase this value if you need the model to learn more concepts. *(Also affects the model file size.)*
    - Use lower value for **LyCORIS** models
- **Network Alpha:** Refer to the document below for what it does.

> Technical explanations of what those parameters do: [Document feat. ChatGPT](misc/TechnicalTerms.pdf)

- **Max Resolution:** For `SDXL`, set to `1024,1024`; For `v1.5`, if your VRAM can handle, set `768,768`; otherwise `512,512`.
- **Enable Buckets:** Enable
- **Keep n tokens:** Refer to [Captioning](#captioning). Set it to the amount of **trigger words** you have.
- **Clip Skip:** `1` for realistic or `SDXL`; `2` for anime.
- **Shuffle caption:** Enable
- **Use xformers:** Enable
- **Noise offset:** Basically, this can help to generate brighter and darker scenes.
  > [Technical Explanations](https://youtu.be/cVxQmbf3q7Q)

## Press the **Start Training** button
- ~~*Pray you don't waste an hour for nothing*~~
- After the training is finished, you can use [**`X/Y/Z Plot`**](XYZ/README.md) to evaluate the results.
