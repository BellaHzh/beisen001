# **0918**
- intro to Python
- Hello.py
  - ```python
    name = input('Enter your name: ')
    # f for format, use {} to indicate it is a variable
    print(f'hello, {name}')
    ```
- **Terminal commands (Important)**
    - `pwd` print working directory, shows where you are
    - `cd` change directory
    - `ls` lists all items in current working directory
      - `ls -a` to show hidden files
    - `mkdir` make directory (folder)
    - `touch` to create new file
      - e.g. `touch hello.py` to create a new file called `hello.py` in current working directory
    - `open` to open a file
      - e.g. `open hello.py` to open the file called `hello.py` using the default app (can be modified in MacOS by right click on the file --> get info)

- ### Git and Github
  - Git is a distributed version control system that tracks changes in any set of computer files, usually used for coordinating work among programmers who are collaboratively developing source code during software development.
  - basic commands in git: check out [this pdf](https://education.github.com/git-cheat-sheet-education.pdf) for basic commands in git (the ones needed for this class are everything on the pdf except for the Branch and Merge part, all assignments are to be submitted on github)
  - A cheat to github: if you want the easy ways, [download VSCode](https://code.visualstudio.com/) and Familiarize with the User Interface. VSCode allows you to commit and sync in one button click.
- Staging and commiting in git
  - `git add . ` stages all unstaged changed files 
  - Once staged, use `git commit -m 'your message'` to make a commit. the `-m` command lets you write a message for the commit, and it's necessary.
  - To sync your commits to github, use `git push -u origin main`. Recount that `origin` is the url we set when initializing and `main` is the branch that we are pushing to the remote
  - To pull from github, simply use `git pull`
- [Homework 1](https://emilydidthis.github.io/CSCI-UA.002-Fall23/assignments/01.html) (due 9/22)