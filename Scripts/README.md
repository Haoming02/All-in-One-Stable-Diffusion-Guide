# Helper Scripts
Some **python** scripts that ease the process of preparing caption dataset

**Important:** Remember to use `" "` if your tags or paths contain spaces

### Insert.py
- Insert tags at the start of the caption for all text files in a folder.
    - Useful for adding **trigger words**
- **Usage:** `>python Insert.py "<folder path>" "<tags>"`

### Append.py
- Append tags at the end of the caption for all text files in a folder.
- **Usage:** `>python Append.py "<folder path>" "<tags>"`

### Remover.py
- Remove specified tags from the caption for all text files in a folder.
- **Usage:** `>python Remover.py "<folder path>" "<tags>"`

### Replacer.py
- Replace a specific tag with another tag in the caption for all text files in a folder.
- **Usage:** `>python Replacer.py "<folder path>" "<old tag>" "<new tag>"`

### CleanTags.py
- Remove some common tags that describe the subjects (eg. `hair`).
- **(Optional)** Remove `color` tags *(Default to `False`)*.
- **Usage:** `>python CleanTags.py "<folder path>" <remove color (optional)>`

### Formatter.py
- Remove extra commas and spaces for all text files in a folder.
    - **Note:** This is automatically triggered when using other scripts above
- **Usage:** `>python Formatter.py "<folder path>"`

### TriggerDebug.py
- Print out the `n-th` tag for all text files in a folder.
    - Useful for checking if the **trigger words** is consistent
- **Usage:** `>python TriggerDebug.py "<folder path>" <index>`

# Misc
Some other **python** scripts not related to captioning

### CopyConfig.py
- Copy the value from the source config to the target config if the key matches
    - Useful for installing multiple instances of SD Webui
- **Usage:** `>python CopyConfig.py "<source config>" "<target config>"`

### CopyMetadata.py
- Copy the metadata from 1 image to another
    - Useful for baking a ComfyUI workflow into a screenshot
- **Usage:** `>python CopyMetadata.py "<source image path>" "<target image path>"`

### OptimizeImage.py
- Optimize images to reduce their sizes
- **Usage:** `>python OptimizeImage.py "<folder path>"`

### PrepJPG.py
- Prepare PNG to JPG in certain fixed sizes as dataset
- **Usage:** `>python PrepJPG.py "<folder path>"`
