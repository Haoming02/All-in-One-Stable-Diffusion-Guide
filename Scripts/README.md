# Helper Scripts
Some `python` scripts that ease the process of preparing dataset.

**Note:** Remember to use `" "` if you have multiple tags

### Insert.py
- Insert tags at the start of the caption for all text files in a folder. Useful for adding **trigger words**. 
- This will also remove the same tags if found in the original file to avoid duplicates.
- **(Optional)** Using `filter` causes the script to only work on files where the name contains said filter.
  - **eg.** Name your 3D images 3D and 2D images 2D, then only add `3d` tag to files named 3D 
- **Usage:** `>python Insert.py "<folder path>" "<tags>" <filter (optional)>`

### Append.py
- Append tags at the end of the caption for all text files in a folder. 
- This will also remove the same tags if found in the original file to avoid duplicates.
- **(Optional)** Using `filter` causes the script to only work on files where the name contains said filter.
- **Usage:** `>python Append.py "<folder path>" "<tags>" <filter (optional)>`

### Remover.py
- Remove specified tags from the caption for all text files in a folder. 
- **Usage:** `>python Remover.py "<folder path>" "<tags>"`

### Replacer.py
- Replace a specific tag with another tag in the caption for all text files in a folder. 
- **Usage:** `>python Replacer.py "<folder path>" "<old tag>" "<new tag>"`

### GenerateTxt.py
- Generate a `.txt` file containing the tags specified, with the same filename for all files in a folder. Useful for **manually captioning**.
- **Usage:** `>python GenerateTxt.py "<folder path>" "<tags>"`

### CleanTags.py
- Remove some common tags that describe the subjects (eg. \*hair). 
- **(Optional)** Remove color\* tags *(Default to `False`)*.
- **Usage:** `>python CleanTags.py "<folder path>" <remove color (optional)>`

### TrimDigits.py
- Remove the 8 leading numbers from the filename for all text files in a folder. 
- **Usage:** `>python TrimDigits.py "<folder path>"`

### Formatter.py
- Remove duplicated tags, commas and extra spaces for all text files in a folder.
- ***Note:** This is automatically triggered when using other scripts above.*
- **Usage:** `>python Formatter.py "<folder path>"`