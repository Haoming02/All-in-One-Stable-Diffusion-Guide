# LoRA Training Tutorial
***by. [Haoming](https://civitai.com/user/HaomingGaming) 2023/04/20***

## Install Kohya SS
Just like `Stable Diffusion`, there is already a popular webui available: [Kohya SS](https://github.com/bmaltais/kohya_ss), 
as well as GoogleColab versions that again I won’t cover. Simply go to the repository and follow the installation steps. 
 *(Slightly outdated [Video Tutorial](https://youtu.be/9MT1n97ITaE))*

**Note:** If you have a RTX 30 or RTX 40 series GPU, choose **`bf16`** during the accelerate config; otherwise choose **`fp16`**. 

## Prepare Dataset
Now comes the most difficult part: preparing the dataset. As the good ol’ saying goes: 
> Garbage in, garbage out. 

If you didn’t prepare the dataset properly, the trained model will not produce good outcomes. For training LoRA, the dataset refers to 2 things: the images as well as the captions for the images. The model can produce decent enough outcomes with as few as 6 images, but of course the more the better. Having more images generally does **not** increase training time due to how the training is setup. Additionally, the more variety you have in the dataset the better. For example, having 5 images of your subject in different environments is significantly better than having 50 images of your subject in the exact same conditions.

### Resolution:
The “standard” is to train on 512x512 images. You can also train on 768x768 images, which is said to yield better results, though it will take longer time as well as more VRAM to train, and the actual improvement is yet to be confirmed. 
If you don’t want to crop all the images to square, you can turn on the **`Enable Buckets`** toggle, which will automatically crop and resize all images to the equivalent resolution. Though the impact on results is yet to be confirmed, either. 

### Preparing Images:
As mentioned above, it is better to have more varieties in the images, such as different background, lighting, clothing, etc. Aspect ratio generally doesn’t matter too much thanks to `Buckets` as mentioned above. It’s recommended to use “official” arts, such as card arts, in-game screenshots or promo images, instead of fanarts. 
Once you finish preparing a dozen or so images with varying environments, proceed to next step. 

**Important:** If you have multiple formats of images, make sure that there are no duplicated filenames.

### Captioning:
The easiest way to mass caption all the images is to again use the **Automatic1111 webui**. In the **Train** tab, you should see a section called **Preprocess Images**. Enter your folder that contains the image and a destination folder. Depending on your image, if it’s anime style, choose **`Deepbooru`**; if it’s realistic, choose **`Blip`**, then press **Run**. 

**Note:** If you didn't want to crop the images to square, just copy the caption text files back to the original folder, and use [TrimDigits.py](Scripts/) to rename them. The captions will work as long as the filenames are the same as the images.
Alternatively, if you want to manually caption the images, use [GenerateTxt.py](Scripts/) instead.

You’re not done yet! Now you need to go through every single `.txt` file and manually check the captions. You need to **remove** every tag that describes your subject, keeping only the tags that should be “variables.” Think of it this way: You want the tag of your subject to be associated with their features. 
So do not caption something like hair color or eyes color, unless you want them to be able to change *(eg. when training a Style)*. Only caption the background, the expression of the subject, what pose the subject is in, for example. Last but not least, add the **trigger tags** in front of the captions. (You can use the [Insert.py](Scripts/) script to automate this.) 
The number of triggers has to be consistent across your dataset. For example, when I am training a character with multiple outfits, I put the character name first, then the outfit name, then the rest of tags. Thus I have 2 trigger words for every single caption.

### Folder Structures
Create a folder named after your project. Inside it create 3 more folders, `img`, `mdl`, `log`. Inside the `img` folder create folders named in the format of `XXX_YYY`.

- The `XXX` is the number of steps per image. Generally, it takes a few hundreds steps to learn a “concept,” such as character likeness or outfit. Then, divide that number by the number of images you have to get `XXX`. *(No need to be exact.)* Most of my characters with 2 outfits were trained in ~1500 steps for reference.
- The `YYY` is the class of the images. It's basically a way to group the images. Currently, I’m still unsure how class affects the results. But if I’m training a game character for example, I separate them into a 2D folder for card arts and a 3D folder for model screenshots.

So in the end, it will be something like:
```
Project
- img
    |- 150_foo
        |- 01.png
        |- 01.txt
    |- 150_bar
        |- 04.png
        |- 04.txt
- mdl
- log
```

***Note:** You don't actually have to follow this structure strictly. For example, you can just set the output model folder directly to the webui LoRA folder.*

## Configs
>Remember to switch to the LoRA tab at the top first.

>Parameters that were not mentioned can just be left on default.

### Source Model
- **Pretrained Model:** It’s better to pick a general model (eg. `anything-v3.0` or `SD v1.5`) instead of a finetuned one, so it is more likely to work on all models.
- **Save Model as:** `.safetensors`
- **Important:** If the pretrained model is for SD 2.0, check `v2`; Then, if it’s for SD 2.1, check `v_parameterization` too. *(Refer to [versions](README.md#sd-versions) if you don't know what they are.)*

### Folders
Enter the folders you created in the steps above. Remember to link to the `img` folder instead of the folders inside. Then, enter a model output name of choice.

### Training Parameters
- **Train Batch Size:** Basically means how many images at once does it train per step. Setting it to 2 cut the training time almost in half. Requires high VRAM to handle. 

    **Note:** It is said that this may worsen the results, and you should increase the **Epoch** count to compensate for it, so that the total steps stay the same.

- **Epoch:** How many times should the training go through all the steps. Normally, 1 epoch is fine. You can do more to finetune. *Beware of overfitting!*
- **Caption Extension:** Set it to the correct extension. (`.txt` if you use the webui tools)
- **Mixed/Save Precision:** Again, choose **`bf16`** if you have RTX 30 or 40; otherwise choose **`fp16`**.
- **Learning Rate / Scheduler / Warmup / Optimizer:**
    - Personally I use `0.00025` / `cosine` / `10%` / `AdamW8bit`
    - Refer to the document below for what these do.
- **Network Rank:** How “complex” the subject is. I use `64` for most of my models. Increase this value if you need the model to learn more concepts. *(Affects the final file size.)*
- **Network Alpha:** I set it to `16`. Refer to the document below for what it does.
- **Max Resolution:** `512,512` or `768,768`, depending on your dataset.
- **Enable Buckets:** Refer to [Resolution](#resolution).
- **Keep n tokens:** Refer to [Captioning](#captioning). If you have 1 trigger word, set it to 1, etc.
- **Clip Skip:** `1` for realistic; `2` for anime.
- **Shuffle caption:** Enable
- **Use xformers:** Enable

If you want technical explanations of what these parameters do, check out this [document](misc/TechnicalTerms.pdf) answered by ChatGPT.

## Press the **Train Model** button
~~And hope nothing explodes~~

After the training is finished, you can use [**`X/Y/Z Plot`**](XYZ/README.md) to evaluate the results.
