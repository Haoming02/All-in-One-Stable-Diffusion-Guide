# X/Y/Z Plot
***by. Haoming***

## What is It
This tool is extremely useful for doing **comparisons** and **evaluations** for models, prompts, or settings, etc. 
You can use it to create a large grid of images generated from different configurations, and then quickly decide which one is better at a glance.

## Where is It
In the **txt2img** and **img2img** tabs of the webui, you should see a **Script** section when you scroll down. Click it then select `X/Y/Z plot` to open the sub-section.

## How to Use
There are 3 different axes: X axis will generate variations horizontally; Y axis will generate variations vertically; Z axis will generate another XY Grid separately.
For each axis, you can choose a type as the variable in the left field, then enter the values to cycle through in the right field, separated by comma.
Some of the types (eg. `Checkpoint name`) show a yellow button that when clicked will populate the field with all values available, so you don't have to type them manually.
Among the types, the most useful one for evaluations is `Prompt S/R`.

**Note:** This does not require higher VRAM than normal, as it generates each image individually then combine them afterwards.

## Prompt S/R
#### How it Works
It searches through the prompts to look for the first value in the field. Then in each cycle, it replaces the value with other values in the field.
The value can be either numbers or strings.

#### Training Evaluation
If you train a LoRA for multiple epochs, they will come in the format of `name-000001`. And you can add them to the prompt like `<lora:name-000001:0.5>`.
Then, you can use `S/R` in both X and Y axis, with X field using `01, 02, 03` and Y field using `0.5, 0.75, 1.0`. The tool will then generate a 3x3 grid with LoRA from different epochs at different strength.
Afterwards, you can quickly check what strength can produce the best results, and if the training caused overfittings.

## Example:
- **Prompt:** ` 1girl, solo, smile, blush, rooftop, sunset`
- **X axis:** `Checkpoint name` ; **Y axis:** `Steps` 

<p align="center"><img src="01.jpg"></p>
