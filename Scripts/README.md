<h1 align="center">Helper Scripts</h1>
<p align="center">Some <b>python</b> scripts that ease the process of preparing caption dataset</p>

> [!TIP]
> Remember to use `" "` if your paths or tags contain spaces

### Append.py
- Append tags at the end of the caption for all text files in a folder

### Cleanse.py
- Clear out the contents for all text files in a folder

### CopyConfig.py
- Copy the values from the source `.json` config to the target `.json` config if the key matches
    - Useful when installing multiple instances of Webui

### CopyMetadata.py
- Copy the metadata from an image to another image
    - Useful for baking a ComfyUI workflow into a screenshot

### EmptyCaption.py
- Generate an empty `.txt` file with the same name for all non-text files in a folder

### Folder2Name.py
- Insert the part after the `_` in the folder name to all text files under that folder

### Formatter.py
- Remove extra commas and spaces for all text files in a folder
    - Automatically triggered when using most other scripts

### Front2Back.py
- Move the first tag to the last for all text files in a folder

### GenMask.py
- Generate a grayscale image for all image files in a folder
    - Useful for masked training

### Insert.py
- Insert tags at the start of the caption for all text files in a folder
    - Useful for adding **trigger words**

### LookForTag.py
- Print out all files that contain a specific tag

### LoRA_Metadata.py
- Given a LoRA file, extract its training metadata

### OptimizeImage.py
- Optimize `.png` images into `.jpg` to reduce storage size

### PrepJPG.py
- Bucket images in certain fixed aspect ratios

### PruneColor.py
- Remove color `hair` and `eyes` tags from caption for all text files in a folder 

### Remover.py
- Remove specified tags from the caption for all text files in a folder
    - Also supports removing by index

### Replacer.py
- Replace a tag with another tag in the caption for all text files in a folder

### ReplacerRaw.py
- Replace a plain string with another plain string in the caption for all text files in a folder

### TargetedDelete.py
- Delete the text and image files if the caption contains specified tag

### TriggerDebug.py
- Print out the `n-th` tag for all text files in a folder
    - Useful for checking if the **trigger words** is consistent
