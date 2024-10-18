<h1 align="center">Tips & Tricks</h1>
<p align="center"><b>by. Haoming</b></p>

## General Knowledge
> This section will cover some basics on how Stable Diffusion works

### Quality Prompts
Due to how the training datasets were captioned, adding some "quality prompts" can usually improve the results drastically. Be sure to read the description of the Checkpoint page, as some of them require specific keywords in order to generate anything remotely good.

- <ins><b>Example</b></ins>
  - for **SD1** & **SDXL**:
    - add `(high quality, best quality)` to **positive** prompt
    - add `(bad quality, worst quality)` to **negative** prompt
  - for **Pony**:
    - add `score_9, score_8_up, score_7_up` to **positive** prompt
    - add `score_4, score_5, score_6` to **negative** prompt
  - for **Flux**:
    - *not really needed*

> [!TIP]
> See [Architecture](../README.md#architecture) if you don't know what the **versions** mean

### Prompt Order
The order of the prompts has an effect on the generation results. Preceding prompts have more influence than subsequent prompts; but subsequent prompts can sometimes override preceding prompts. *(Kinda like natural language, "a dog in a park" and "a park with a dog" have a different focus)*

~~Experiment more to get the nuance~~...

<br>

## Webui Features
> This section will cover some lesser-known features of the Webui

### Styles
You can save custom prompts using the **Styles** feature, and reuse them again in the future, such as the quality prompts mentioned above.
  - Click the `🖌️` button to open the `Style Dialogue`
  - Manually type the prompts; or click the `📝` button to pull the current prompts in the UI
  - You can use the `{prompt}` keyword to represent the prompts currently in the UI, in order to write a style that surrounds the subjects
  - Enter a name for the style in the dropdown
  - Click the **Save** button to save; **Delete** to delete

When the style name is ticked in the dropdown, the style is applied to the generation automatically; you can also click the `📋` button to load the prompts to the UI.

> [!TIP]
> Styles are saved in the `styles.csv` file in the installation folder. You can share this file, or add curated styles found online.

### Brackets
- Surround a prompt in `( )` / `[ ]` to increase / decrease the weight of the prompt respectively
- You can stack multiple brackets to influence the weight more
  - Brackets stack multiplicatively
- Alternatively, You can also specify the weight by `(tag:ratio)`
- <ins><b>Example</b></ins>
  - `((foo))` is the same as `(foo:1.21)`
  - `[[bar]]` is the same as `(bar:0.81)`

> [!NOTE]
> If you have a mismatching number of opening and closing brackets, the token counter will turn red

> [!TIP]
> You can use `Ctrl + Up Arrow` or `Ctrl + Down Arrow` to quickly increase or decrease the weight of the currently selected words

### Prompt Editing

- **Syntax:** `[a:b:r]`
  - `a` is a string
  - `b` is a string
  - `r` is a `float` ranging from `0.0` to `1.0`; or an `int` above `1`

The prompt will switch from `a` to `b` based on `r`. When `r` is a `float`, it is the ratio of the total steps; when `r` is an `int`, it is the step at which point the prompt switches *(**eg.** When generating for `20` steps, setting `r` to `0.5` is the same as setting `r` to `10`)*. ~~Actual use case depends on your creativity~~.

- <ins><b>Example</b></ins>
  - You can do something like `[arms up:heart hands:0.25]` to "combine poses," generating previously unknown concepts. The result would be different from `arms up, heart hands`, though which one looks better is up to experimentation.

### Alternating Words

- **Syntax:** `[x|y]`
  - `x` and `y` are strings

The prompt will keep alternating between `x` and `y` every step. You can also chain more than two prompts for alternation. ~~Actual use case depends on your creativity~~.

- <ins><b>Example</b></ins>
  - You can do something like `[white t-shirt|black bikini]` for some sort of see-through effect

### BREAK Keyword

- **Syntax:** `BREAK`
  - *(all caps)*

For **SD1** and **SDXL**, if your prompt is too long, it will be split into 75-token chunks, as shown in the token counter. It’s usually better to group the chunks logically. You can write some quality prompts and background, `BREAK`, then the main prompts about your subject, in order to avoid unwanted mixing behavior.

> [!TIP]
> See [Architecture](../README.md#architecture) if you don't know what the **versions** mean

> [!NOTE]
> Token count is not the same as word count

### Themes
In the `User interface` section of the **Settings** tab, you can select a different theme from the `Gradio theme` dropdown to change how the Webui looks. You can also find ~~better~~ themes available online, such as the pastel [Catppuccin Theme](https://github.com/Haoming02/catppuccin-theme) or the modern [Lobe Theme](https://github.com/lobehub/sd-webui-lobe-theme).

> [!TIP]
> You install these themes like [Extensions](../README.md#extensions)

### Default Values
After you changed the value of some parameters, such as the `Sampling method`, you can then go to the `Defaults` section of the **Settings** tab, click **View changes** to see the list of modified parameters, then click **Apply** to save them as the new default values. Next time you launch the Webui, those values would be set automatically.

> [!TIP]
> Defaults are saved in the `ui-config.json` file in the installation folder. You can even disable certain parameters by setting their `visible` to `false`.

### X/Y/Z Plot
- [Tutorial for X/Y/Z Plot](./XYZ.md)

### Restart
There are technically 4 "levels" of restarting the Webui:

- `"Softest"` - **Refresh (`F5`) the Browser**: This basically just resets the changed parameters
- `"Soft"` - **Reload UI** *(at the bottom of the page)*: This additionally refreshes the `.js` and `.css` files if you modified them
- `"Hard"` - **Apply and restart UI** *(in **Extensions** tab)*: This additionally reloads the `.py` files if you modified them
- `"Full"` - **Close and launch the Webui again:** The cleanest restart, should fix all runtime problems if you encountered any
