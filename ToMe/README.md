# Speed Up Generations
***by. Haoming 2023/05/04***

> [GitHub & Paper](https://github.com/dbolya/tomesd)

## How it Works
It basically merges certain tokens together, thus reducing the memory requirement and increasing the generation speed. The higher the `Ratio`, the more the impact.
However, the process is **lossy**, so you will see **visual degradation** when you set the `Ratio` too high. 

> See [Examples](#examples) below

## Requirements
- Install the required Python Package:
  1. Go to the webui install folder
  2. Click the address bar, then enter `cmd` to open the console
  3. Enter `venv\Scripts\activate` to open the virtual environment
  4. Enter `pip install tomesd` to install the package
- Install the following Extension:
  - `sd-webui-tome` ([link](https://git.mmaker.moe/mmaker/sd-webui-tome))
    - Click `Download Repository`, then extract the folder inside to `~\stable-diffusion-webui\extensions`

## How to Use
After you install the above extension, you should see a new section called **`Token Merging`** in the **Settings** tabs.
Toggle `Enable` and play with the `Ratio` and other settings.

**Note:** You need to **Reload UI** when you adjust the `Ratio` to re-apply the patch

## Examples
> Tested on **RTX 3060**;  `--xformers`
 
> Generating at 512x512; Hires. Fix to 1024x1024; Euler a; 32 Steps; Same Prompt & Seed

> Max Downsample: 2; Stride X: 4; Stride Y: 4; All 4 Toggles Enabled

<table>
    <tbody>
        <tr align="center">
            <td><b>Ratio</b></td>
            <td>Off</td>
            <td>0.3</td>
            <td>0.5</td>
            <td>0.7</td>
        </tr>
        <tr align="center">
            <td><b>Base</b></td>
            <td>7.85 it/s</td>
            <td>7.92 it/s</td>
            <td>8.08 it/s</td>
            <td>9.31 it/s</td>
        </tr>
        <tr align="center">
            <td><b>Hires. Fix</b></td>
            <td>1.46 it/s</td>
            <td>1.81 it/s</td>
            <td>2.15 it/s</td>
            <td>2.71 it/s</td>
        </tr>
        <tr align="center">
            <td><b>Total</b></td>
            <td>16s</td>
            <td>14s</td>
            <td>12s</td>
            <td>10s</td>
        </tr>
        <tr align="center">
            <td><b>Result</b></td>
            <td><img src="Off.jpg" width=128></td>
            <td><img src="0.3.jpg" width=128></td>
            <td><img src="0.5.jpg" width=128></td>
            <td><img src="0.7.jpg" width=128></td>
        </tr>
    </tbody>
</table>