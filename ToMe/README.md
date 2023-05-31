# Speed Up Generations
***by. Haoming***

> [GitHub & Paper](https://github.com/dbolya/tomesd)

## How it Works
It basically merges certain tokens together, thus reducing the memory requirement and increasing the generation speed. The higher the `Ratio`, the more the impact.
However, the process is **lossy**, so you will see **visual degradation** when you set the `Ratio` too high. 

# Note
- Since webui version `v1.3`, this function has been implemented natively. Just go to **Settings** -> `Optimizations`
  - Bump `Negative Guidance minimum sigma` to `1 ~ 2` too while you're there for even more speed increase

## Examples
> Tested on **RTX 3070 Ti** w/ `--xformers`
 
> Generating at 512x512; 32 Steps; Euler a

> Hires. Fix to 1024x1024; 16 Steps; Latent (nearest)

> Same Prompt; Same Seed

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
            <td>13.65 it/s</td>
            <td>13.26 it/s</td>
            <td>13.51 it/s</td>
            <td>14.75 it/s</td>
        </tr>
        <tr align="center">
            <td><b>Hires. Fix</b></td>
            <td>2.96 it/s</td>
            <td>3.45 it/s</td>
            <td>3.90 it/s</td>
            <td>4.30 it/s</td>
        </tr>
        <tr align="center">
            <td><b>Total</b></td>
            <td>9s</td>
            <td>8s</td>
            <td>8s</td>
            <td>7s</td>
        </tr>
        <tr align="center">
            <td><b>Result</b></td>
            <td><img src="Off.jpg" width=100></td>
            <td><img src="0.3.jpg" width=100></td>
            <td><img src="0.5.jpg" width=100></td>
            <td><img src="0.7.jpg" width=100></td>
        </tr>
    </tbody>
</table>