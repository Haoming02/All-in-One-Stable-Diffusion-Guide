<h1 align="center">Tips & Tricks</h1>
<p align="center"><b>by. Haoming</b><br><i>Last Update: 2023/05/31</i></p>

## Themes
You can write **CSS** scripts, or download ones made by others such as [Catppuccin](https://github.com/catppuccin/stable-diffusion-webui), 
and then save as `user.css` in the project directory to change how the webui looks.

<hr>

## Default Values
Inside your webui installation folder, there is a file called `ui-config.json`

You can open it and edit the entries to change the default ui values such as `Sampling method`, disable unused elements, or increase the max resolution limits.
Save you a few clicks everytime you use the webui.

<hr>

## Noise Offset
Some people found out that, the noise functions used during training was flawed, causing Stable Diffusion to always generate image with average brightness of `0.5`.

> **ie.** Even if you prompt for dark/night or bright/snow, the overall image still looks "grey" on average

> [Technical Explanations](https://youtu.be/cVxQmbf3q7Q)

The solution is to use [Noise Offset](https://civitai.com/models/13941/epinoiseoffset), which allows you to generate some truly dark or bright images.

<hr>

## Logo Creations
You can generate stylistic logos *(like those of eSports teams)* by following the steps below. *Original credit: [Reddit](https://www.reddit.com/r/StableDiffusion/comments/11i11nd/to_generate_icons_on_a_neutral_background_put_a/).*
1. Prepare a solid color image using any program
2. Upload it to **img2img** 
3. Set the **denoising strength** to `1.0`
4. Prompt the subject of choice
5. ...
6. ~~Profit~~

<hr>

## *More Coming Soon*