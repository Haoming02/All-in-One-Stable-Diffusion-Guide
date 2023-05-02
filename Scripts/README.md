# Helper Scripts
Some `python` scripts that ease the process of preparing dataset.

### Insert.py
- Insert tags at the start of the caption for all text files in a folder. Useful for adding **trigger words**. 
- This will also remove the same tags if found in the original file to avoid duplicates.
- **Usage:** `>python Insert.py "<folder path>" "<tags>"`

### Append.py
- Add tags at the end of the caption for all text files in a folder.
- **Usage:** `>python Append.py "<folder path>" "<tags>"`

### Remover.py
- Remove specified tags from all text files in a folder.
- **Usage:** `>python Remover.py "<folder path>" "<tags>"`

### Replacer.py
- Replace a specific tag with another tag for all text files in a folder.
- **Usage:** `>python Replacer.py "<folder path>" "<old tag>" "<new tag>"`

### GenerateTxt.py
- Generate a `.txt` file containing the tags specified, with the same filename for every file in a folder. Useful for **manually captioning**.
- **Usage:** `>python GenerateTxt.py "<folder path>" "<tags>"`

### CleanTags.py
- Remove some common tags that describe the subjects (eg. \*hair). Can optionally remove color\* tags *(Default to `False`)*.
- **Usage:** `>python CleanTags.py "<folder path>" <delete color tags? (optional)>`

### TrimDigits.py
- Remove the 8 leading numbers from the filename of the caption text files in a folder.
- **Usage:** `>python TrimDigits.py "<folder path>"`