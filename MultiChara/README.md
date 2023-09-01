# Latent Couple
***by. Haoming***

> [Video Tutorial](https://youtu.be/uR89wZMXiJ8) by **Aitrepreneur**

## Requirements
> Learn how to install [Extensions](../README.md#extensions)

- Install the following Extension:
  - `two-shot (Latent Couple)` *([GitHub](https://github.com/ashen-sensored/stable-diffusion-webui-two-shot))*
  - `composable-lora` *([GitHub](https://github.com/a2569875/stable-diffusion-webui-composable-lora))*

## How to Use
After you install the above extensions, you should see the 2 new sub-sections down in the **txt2img** and **img2img** tabs.

### Composable Lora
You only need to enable `Composable Lora` if you are going to use different LoRAs or LyCORIS *(**eg.** generating different characters)* in each region. 

### Latent Couple
- When opened, you can see 2 tabs, **Mask** and **Rectangular**.
  - **Mask:** You can upload an image with separated regions marked with distinct colors. Then click `I've finished my sketch` and finetune the populated regions.
  - **Rectangular:** Manually enter fields to divide up the regions.
- It's rather easier and straightforward to use the **Rectangular** mode.
- Fields Explanations:
  - **Divisions:** `Height`:`Width` of the regions.
  - **Positions:** `X` and `Y` coordinates of the regions.
  - **Weights:** Weights of the regions.
  - **end at this step:** Just set it the same as the `Sampling steps` above.
- Alternatively, use the [Latent Couple Helper](https://github.com/Zuntan03/LatentCoupleHelper). Check the [video tutorial](#multiple-characters) above for how it works.
- You can then click **Visualize** see how the specified regions look.

### Prompts
- You write prompt as usual. The only difference is that, you separate each regions with the keyword **`AND`**. The prompts will correspond to the regions in order.
- By default, if you didn't modify the values, the **Rectangular** tab has 3 regions: 1 covering the entire image and 2 on each half of the image.
- Use the first region that covers the whole image for the starting tags (`best quality`, etc.) and the background, as well as the number of subjects. (eg. `2girls`)
- Then use the rest of the regions to describe each subjects.
- You can also create a region that covers the whole image again at the end to do some "post-processing."

## Example Generation
```
high quality, best quality, masterpiece, absurdres, 2girls, beach
AND 2girls, blond_hair, short_hair, standing, smile, blush, barefoot
AND 2girls, pink_hair, long_hair, sitting, angry, stare, barefoot, beach_chair
AND 2girls, beach, sunny, water, day, blue_sky, clouds
```

<p align="center"><img src="Sample01.jpg"></p>
