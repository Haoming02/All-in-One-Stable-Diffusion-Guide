<h1 align="center">Training Parameters</h1>

<p align="center">
<b>by. Haoming</b><br>
<i>Last Update: 2024/01/25</i>
</p>

<p align="right"><i>
<sub>written based on my own experience and explanation from ChatGPT</sub>
</i></p>

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

On **Kohya_SS**, you can set a different learning rate for `Text Encoder` and `Unet`.
Generally, just set the `Text Encoder` learning rate to around half of `Unet` learning rate.

> **eg.** `0.000075` for `Text Encoder` ; `0.00015` for `Unet`

**Note:** If you're using an *adaptive* Optimizer *(**eg.** `Adafactor` or `Prodigy`)*, 
set both learning rate to `1.0` as they will be handled by the Optimizer automatically.

## Scheduler
> The scheduler controls the learning rate during training

- **Constant:** The learning rate remains fixed throughout training
- **Linear:** The learning rate decreases linearly over time
- **Cosine:** The learning rate follows a cosine curve, gradually decreasing over time
- **Cosine with Restarts:** Same as above; but also resets to the initial rate intervally based on `LR number of cycles` 

## Warmup
> The warmup gradually increases the learning rate from a small value to its maximum value, 
so that the model can more easily explore the spaces

Just leave it at `10` (%)

## Optimizer
> The optimizer is the algorithm used to update the model weights during training

- **AdamW** and **Lion**: Popular optimizers. Nothing special; No drawbacks.
- **AdamW8bit** and **Lion8bit**: Variants with reduced memory requirement but also lost precision.
  - In my experience, the lower precision actually helps train better models, as it "misses out" the low quality artifacts.
  - To use 8bit optimizers on Windows, I had to do the following *(in `venv`)* first:
    ```bash
    pip uninstall bitsandbytes
    pip uninstall bitsandbytes-windows
    pip install https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.41.1-py3-none-win_amd64.whl
    ```
- **Adafactor** and **Prodigy**: Optimizers that automatically determines learning rates. In my experience, they are also slower.

<hr>

<details>
<summary>My parameters for SDXL training on RTX 3060</summary>

```json
{
  "LoRA_type": "Standard",
  "adaptive_noise_scale": 0.00357,
  "additional_parameters": "",
  "block_alphas": "",
  "block_dims": "",
  "block_lr_zero_threshold": "",
  "bucket_no_upscale": true,
  "bucket_reso_steps": 64,
  "cache_latents": true,
  "cache_latents_to_disk": false,
  "caption_dropout_every_n_epochs": 0.0,
  "caption_dropout_rate": 0,
  "caption_extension": ".txt",
  "clip_skip": "1",
  "color_aug": false,
  "conv_alpha": 1,
  "conv_block_alphas": "",
  "conv_block_dims": "",
  "conv_dim": 1,
  "decompose_both": false,
  "dim_from_weights": false,
  "down_lr_weight": "",
  "enable_bucket": true,
  "epoch": 32,
  "factor": -1,
  "flip_aug": false,
  "full_bf16": false,
  "full_fp16": false,
  "gradient_accumulation_steps": 2,
  "gradient_checkpointing": true,
  "keep_tokens": 3,
  "learning_rate": 0.00015,
  "logging_dir": "",
  "lora_network_weights": "",
  "lr_scheduler": "cosine_with_restarts",
  "lr_scheduler_num_cycles": "4",
  "lr_scheduler_power": "",
  "lr_warmup": 10,
  "max_bucket_reso": 2048,
  "max_data_loader_n_workers": "0",
  "max_resolution": "1024,1024",
  "max_timestep": 1000,
  "max_token_length": "75",
  "max_train_epochs": "",
  "mem_eff_attn": false,
  "mid_lr_weight": "",
  "min_bucket_reso": 256,
  "min_snr_gamma": 0,
  "min_timestep": 0,
  "mixed_precision": "bf16",
  "model_list": "custom",
  "module_dropout": 0,
  "multires_noise_discount": 0,
  "multires_noise_iterations": 0,
  "network_alpha": 8,
  "network_dim": 16,
  "network_dropout": 0,
  "no_token_padding": false,
  "noise_offset": 0.0357,
  "noise_offset_type": "Original",
  "num_cpu_threads_per_process": 2,
  "optimizer": "Lion8bit",
  "optimizer_args": "weight_decay=0.01 betas='0.95,0.98'",
  "output_dir": "...",
  "output_name": "",
  "persistent_data_loader_workers": false,
  "pretrained_model_name_or_path": "...",
  "prior_loss_weight": 1.0,
  "random_crop": false,
  "rank_dropout": 0,
  "reg_data_dir": "",
  "resume": "",
  "sample_every_n_epochs": 0,
  "sample_every_n_steps": 0,
  "sample_prompts": "",
  "sample_sampler": "euler_a",
  "save_every_n_epochs": 1,
  "save_every_n_steps": 0,
  "save_last_n_steps": 0,
  "save_last_n_steps_state": 0,
  "save_model_as": "safetensors",
  "save_precision": "bf16",
  "save_state": false,
  "scale_v_pred_loss_like_noise_pred": false,
  "scale_weight_norms": 0,
  "sdxl": true,
  "sdxl_cache_text_encoder_outputs": false,
  "sdxl_no_half_vae": false,
  "seed": "1225",
  "shuffle_caption": true,
  "stop_text_encoder_training": 0,
  "text_encoder_lr": 7.5e-05,
  "train_batch_size": 2,
  "train_data_dir": "",
  "train_on_input": true,
  "training_comment": "",
  "unet_lr": 0.00015,
  "unit": 1,
  "up_lr_weight": "",
  "use_cp": false,
  "use_wandb": false,
  "v2": false,
  "v_parameterization": false,
  "vae_batch_size": 0,
  "wandb_api_key": "",
  "weighted_captions": false,
  "xformers": "xformers"
}
```

</details>

<hr>

#### Official Wiki Document
- https://github.com/bmaltais/kohya_ss/wiki/LoRA-training-parameters
