# Helper Scripts
Some **python** scripts that ease the process of preparing caption dataset

> **Important:** Remember to use `" "` if your tags or paths contain space

### Insert.py
- Insert tags at the start of the caption for all text files in a folder
    - Useful for adding **trigger words**

### Append.py
- Append tags at the end of the caption for all text files in a folder

### Remover.py
- Remove specified tags from the caption for all text files in a folder

### Replacer.py
- Replace a string with another string in the caption for all text files in a folder

### Formatter.py
- Remove extra commas and spaces for all text files in a folder
    - *Automatically triggered when using other scripts above*

### TriggerDebug.py
- Print out the `n-th` tag for all text files in a folder
    - Useful for checking if the **trigger words** is consistent

### Cleanse.py
- Clear out the contents of all text files in a folder

### EmptyCaption.py
- Generate an empty `.txt` file with the same name for all non-text files in a folder

# misc.
Some other **python** scripts not related to captioning

### CopyConfig.py
- Copy the value from the source config to the target config if the key matches
    - Useful when installing multiple instances of Webui

### CopyMetadata.py
- Copy the metadata from 1 image to another
    - Useful for baking a ComfyUI workflow into a screenshot

### OptimizeImage.py
- Optimize `.png` images to `.jpg` to reduce their storage sizes

### PrepJPG.py
- Bucket images in certain fixed aspect ratios
