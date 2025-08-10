## Assignment

read slides: [file io and exception handling](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/notes/#:~:text=Slides%3A%20File,Slides%3A%20Exception%20Handling)

[file i/o](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/assignments/file-io/)

## What we learned today

open a file and read

```py
# Read file
# This program assumes the text file is in the same directory as the Python program
import os

# find script dir
dir = os.path.dirname(__file__)

# open file
file = open(
    os.path.join(dir, 'Text Files/whitman.txt'), 'r')  # absolute path
# print(file) # print file object
beginning_my_studies = file.read()  # read the contents of the file
file.close()  # close the file object
print(beginning_my_studies)
```

