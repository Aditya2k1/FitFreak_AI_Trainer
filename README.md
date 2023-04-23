# FitFreak_AI_Trainer
#### This repository contains the source code for the Fit-Freak AI trainer Project for our college project
#### [Click Here](https://github.com/Aditya2k1/FitFreak_AI_Trainer) to go to Our Repository

---
## Prerequisites
#### You should have a GitHub Account
#### If not, create one - [Click Here](https://github.com/)

## Install Git on your Local
* Go to https://git-scm.com/download/win and download the `64-bit git for Windows Setup`
* Or click [this link](https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe) to direct download the file
* Open the installer file and click Accept then Next
* Then in the select components section **tick ALL the boxes** and rest keep as default
* Lastly click `Install`

## Setup Git on Local
* Open Git Bash
* Run command - `git init`
* Now your Origin will be set as `~ master`
* Now you need to setup your **Git Username** and **Useremail**
* Run `git config --global user.name "First_Name Last_Name"` to set username
* Replace **First_Name** with your **First Name** and **Last_Name** with your **Last Name** for the above
* Run `git config --global user.email "my_name@example.com"` to set useremail 
* Replace **my_name@example.com** with the **email id** associated with your GitHub account for the above
* Run `git config --list` you will be able to see your username and useremail is set successfully

## Either Install IntelliJ or PyCharm to run the code
### To Install IntelliJ
* Go to [this link](https://www.jetbrains.com/idea/download/#section=windows) and click on Download button under **Community edition**
* Install the .exe file and keep all the values as default

### To Install PyCharm 
* Go to [this link](https://www.jetbrains.com/pycharm/download/#section=windows) and click on Download button under **Community edition**
* Install the .exe file and keep all the values as default
---
## Clone Git Repository from GitHub
* Create a folder inside any directory in your local
* Open Git Bash
* Now `cd` into that directory from Git Bash (if unsure prefer the example given below)

**Example -** Suppose you created a folder named **Project** in `Local Disk D:`
Then you can **cd** into it using the command `cd D:` and press Enter.
Then again run `cd <folder-name>`, in our case the folder name is **Project**,
so the command will be `cd Project` and press Enter

* Run `git clone https://github.com/Aditya2k1/FitFreak_AI_Trainer.git`
* This will clone the repository inside your Project folder

```
*NOTE: The above steps should be performed inside Git Bash
And this is a one-time process
Once you successfully cloned the repository in your local
No need to clone it again to resuse.
You can just use `git pull` and start making changes
```

---
## Start With The Project

* Now you have successfully cloned the repository
* Let's assume you are already inside the folder / working directory which you created to clone the repository
* If not then, `cd` into the folder (In case you are unsure, refer the 3rd step from the above block)
* Now **cd** into _/FitFreak_AI_Trainer_ using `cd FitFreak_AI_Trainer`
* Select this package / working directory from IntelliJ / PyCharm through **_File > Open > [your-directory] > [your-folder-name] > FitFreak_AI_Trainer_** and click **Ok**
* You are ready to make changes and contribute in this project

---
## To Push Your Successful Changes
* Always run `git pull` before committing / pushing your changes
* Run `git diff` to see the difference / changes you made
* Run `git status` to see the modified files
* Once you successfully made changes `git status` will show to files you modified, at first it will be marked in red colour as your changes are still unsaved / unstaged
* Run `git add <file-name>` to saved or mark the changes staged


_NEVER ADD `.idea/` and any `out/` FOLDER_

**NOTE -** If you made changes inside `src/` or `lib/` package / folder, then do `git add <package-name>/<file-name>`
[Example - I made changes in a file named `hello.py` inside `lib/` folder / package,
then I will run command - `git add lib/hello.py` to add the file successfully]
* Again run `git status` to check if your modified files turned to green
* Run `git commit` to commit your changes 
* One editor will open, press `i` to turn on insert mode and write your description. Make sure to mention in which file you made changes and write the description crisp in commit message
* Once completed writing your commit message press `esc` to come out of insert mode then type `:wq` to save the commit message
* Run `git log` to check if your latest log with committed message is present or not
* Run `git push` to successfully push your changes to the repository

---
## Useful Git Commands
* `git pull` - Pulls / downloads the latest changes in the working directory
* `git diff` - To see the difference you made in the working directory
* `git status` - To see the unstaged / unsaved changes you have in the working directory
* `git log` - To see the commit logs history in the working directory
* `git commit` - To commit changes after you made any edits
* `git push` - To the changes in the repository
* `git commit --amend` - To edit the last commit message
* `git restore <file-name>` - To undo the changes you made for that particular file (<file-name>) in the working directory
* `git reset` - To remove untracked files from the working directory
* `git config --list` - To show Git configuration in your system
* `git init` - To set initialization in the particular working directory
* `git log --summary` - To see detailed log view
* `git rm -r <file-name>` - To remove any file / folder
