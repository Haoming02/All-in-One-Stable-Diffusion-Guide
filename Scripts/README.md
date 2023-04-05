# Helper Scripts
Some `python` scripts that ease the process of preparing dataset.

### Insert.py
- Insert tags at the start of the caption for all text files in a folder. Useful for adding **trigger words**.
- **Usage:** `>pyton Insert.py "<folder path>" "<tags>"`

### Append.py
- Add tags at the end of the caption for all text files in a folder.
- **Usage:** `>pyton Append.py "<folder path>" "<tags>"`

### Replacer.py
- Replace a specific tag with another tag for all text files in a folder.
- **Usage:** `>pyton Replacer.py "<folder path>" "<old tag>" "<new tag>"`

### GenerateTxt.py
- Generate a `.txt` file containing the tags specified, with the same filename for every file in a folder. Useful for manual captions.
- **Usage:** `>pyton GenerateTxt.py "<folder path>" "<tags>"`

### CleanTags.py
- Remove some common tags that describe the subjects (eg. \*hair and \*eye). Can optionally remove color\* tags *(Default to `False`)*.
- **Usage:** `>pyton CleanTags.py "<folder path>" <delete color tags? (optional)>`

### TrimDigits.py
- Remove the leading numbers from the filename of the caption text files in a folder.
- **Usage:** `>pyton TrimDigits.py "<folder path>"`