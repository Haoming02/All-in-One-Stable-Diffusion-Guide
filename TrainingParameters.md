<h1 align="center">Training Parameters</h1>
<p align="center">
<b>by. <a href="https://civitai.com/user/HaomingGaming">Haoming</a></b><br>
<i>Last Update: <b>T.B.D</b></i>
</p>

## Preface
There is no one "best" parameter that simply works for every training. Experiment to find what works well for your case!

> Options that are not mentioned simply mean I have no experience with using them

#### Index
- [Learning Rate](#learning-rate)
- [Scheduler](#scheduler)
- [Warmup](#warmup)
- [Optimizer](#optimizer)
- [Wiki](#official-wiki-document)

<hr>

## Learning Rate
> The learning rate controls the step size of the updates to the model weights during training <br>
> Value too large may cause the optimization process to overshoot the optimal point <br>
> Value too small may cause the optimization process to converge too slowly or get stuck in local optima

For **Stable Diffusion**, a value around the order of `0.00015` is usually fine.

On **Kohya_SS**, you can set a different learning rate for `Text Encoder` and `Unet`. Generally, just set the `Text Encoder` learning rate to around half of `Unet` learning rate.

> **eg.** `0.000075` for `Text Encoder` ; `0.00015` for `Unet`

**Note:** If you're using an *adaptive* Optimizer *(**eg.** `Adafactor` or `Prodigy`)*, set both learning rate to `1.0` as they will be handled by the Optimizer automatically.

## Scheduler
> The scheduler controls the learning rate during training

- **Constant:** The learning rate remains fixed throughout training
- **Linear:** The learning rate decreases linearly over time
- **Cosine:** The learning rate follows a cosine curve, gradually decreasing over time
- **Cosine with Restarts:** Same as above; but also resets to the initial rate intervally based on `LR number of cycles`

## Warmup
> The warmup gradually increases the learning rate from a small value to its maximum value, so that the model can more easily explore the spaces

## Optimizer
> The optimizer is the algorithm used to update the model weights during training

- **AdamW** and **Lion**: Popular optimizers. Nothing special; No drawbacks.
- **AdamW8bit** and **Lion8bit**: Variants with reduced memory requirement but also lost precision.
  - In my experience, the lower precision actually helps train better models, as it "misses out" the low quality artifacts.
- **Adafactor** and **Prodigy**: Optimizers that automatically determines learning rates. In my experience, they are also slower.

<hr>

<details>
<summary>My parameters for training Pony LoRAs on RTX 4070 Ti Super</summary>

```json
{
  "metadata_description": "Preset by. Haoming02",
  "========== Accelerate ==========": null,
  "mixed_precision": "bf16",
  "num_processes": 1,
  "num_machines": 1,
  "num_cpu_threads_per_process": 2,
  "dynamo_backend": "tensorrt",
  "dynamo_mode": "max-autotune",
  "dynamo_use_dynamic": false,
  "dynamo_use_fullgraph": false,
  "========== Model ==========": null,
  "pretrained_model_name_or_path": "S:/sd-webui-models/Stable-diffusion/ponyDiffusionV6XL_v6StartWithThisOne.safetensors",
  "output_dir": "S:/sd-webui-models/Lora/dev",
  "save_model_as": "safetensors",
  "save_precision": "bf16",
  "sdxl": true,
  "========== Parameters ==========": null,
  "LoRA_type": "Standard",
  "train_batch_size": 1,
  "epoch": 12,
  "max_train_epochs": 0,
  "max_train_steps": 0,
  "save_every_n_epochs": 4,
  "caption_extension": ".txt",
  "seed": 42,
  "cache_latents": true,
  "cache_latents_to_disk": true,
  "lr_scheduler": "polynomial",
  "optimizer": "Prodigy",
  "optimizer_args": "decouple=True weight_decay=0.01 d_coef=1.2 use_bias_correction=True betas=(0.9,0.99)",
  "learning_rate": 1.0,
  "lr_warmup": 5,
  "max_resolution": "1024,1024",
  "enable_bucket": true,
  "text_encoder_lr": 1.0,
  "unet_lr": 1.0,
  "network_dim": 32,
  "network_alpha": 8,
  "scale_weight_norms": 2,
  "========== Advanced ==========": null,
  "gradient_accumulation_steps": 1,
  "keep_tokens": 5,
  "clip_skip": 2,
  "max_token_length": 150,
  "gradient_checkpointing": true,
  "shuffle_caption": true,
  "xformers": "xformers",
  "debiased_estimation_loss": true,
  "noise_offset_type": "Original",
  "noise_offset": 0.02,
  "noise_offset_random_strength": false,
  "adaptive_noise_scale": 0.001
}
```

</details>

<hr>

#### Official Wiki Document
- https://github.com/bmaltais/kohya_ss/wiki/LoRA-training-parameters
