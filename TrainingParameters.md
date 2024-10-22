<h1 align="center">Training Parameters</h1>
<p align="center">
<b>by. <a href="https://civitai.com/user/HaomingGaming">Haoming</a></b><br>
<i>Last Update: 2024/10/22</i>
</p>

## Preface
There is no single "best" set of parameters that always works for every training. Keep experimenting to find what works well for your dataset~

<details open>
<summary><h2>Index</h2></summary>

- [Learning Rate](#learning-rate)
- [Scheduler](#scheduler)
- [Warmup](#warmup)
- [Optimizer](#optimizer)
- [Wiki](#official-wiki-document)

</details>

## Learning Rate
> The learning rate controls how much the model weights update each step during training

When training a LoRA, a value around the order of `0.0005` is usually fine. Usually, it is better to set `Text Encoder`'s learning rate to half of `Unet`'s learning rate.

> [!IMPORTANT]
> If you're using an adaptive Optimizer *(**eg.** `Adafactor` or `Prodigy`)*, set both learning rate to `1.0` instead, as they will be handled by the Optimizer

## Scheduler
> The scheduler controls the learning rate throughout the training

- **Constant:** The LR remains fixed throughout training
- **Linear:** The LR decreases linearly over time
- **Cosine:** The LR decreases over time following a cosine curve

## Warmup
> The warmup makes the learning rate gradually increase at the beginning

> [!IMPORTANT]
> For certain Optimizer, you may need to add additional flags to the `Optimizer extra arguments` *(**eg.** `safeguard_warmup=True` for `Prodigy`)*

## Optimizer
> The optimizer determines how the model weights are updated during training

- **AdamW**: The classic optimizer; can't go wrong with it
- **Lion**: A newer optimizer, which is supposedly an improved version of **AdamW**
- **AdamW8bit** / **Lion8bit**: Reduce memory requirement at the cost of precision
- **Prodigy**: An adaptive optimizer that automatically adjusts the learning rates

<hr>

<details>
<summary>My parameters for training <b>Pony LoRA</b>s on a <b>RTX 4070 Ti Super</b></summary>

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
  "pretrained_model_name_or_path": "...",
  "output_dir": "...",
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
  "lr_warmup": 0,
  "max_resolution": "1024,1024",
  "enable_bucket": true,
  "text_encoder_lr": 1.0,
  "unet_lr": 1.0,
  "network_dim": 16,
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
  "adaptive_noise_scale": 0.002
}
```

</details>

<hr>

#### See Also
- **Official Wiki:** https://github.com/bmaltais/kohya_ss/wiki/LoRA-training-parameters
- **My Blog Post:** https://civitai.com/models/850658/ponyxl-lora-training
