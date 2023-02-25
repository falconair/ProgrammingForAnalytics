# Lecture notes for "Programming for Analytics" and "Python for Analytics" courses
This repository contains lecture notes for classes offered by Shahbaz Chaudhary at the University Of Chicago's Masters in Analytics program.

## Class setup
Please follow the instructions below to get your computer ready for this class.

_Note Mac users: Once software is downloaded, if you double click to launch it, you may get permission errors. Try to right click on the downloaded software, pick "open" and continue. (Apple is trying to protect you from accidentally starting malware/virus)_

#### Install Python (anaconda distribution)
Please install Python from this website: https://www.anaconda.com/distribution/
(modern computers are 64 bit so please pick that option)

Mac users:
Accept all default prompts

Windows users:
Accept all default prompts

Anaconda's distribution of Python is widely used in the industry, particularly among data scientists. This distribution makes it easy to use many libraries and packages for data analysis, building models, visualization, etc.

Once installed, please start jupyter notebook and execute code provided below
1. Start `Anaconda Navigator` and click `Launch` on the panel labeled `Jupyter Notebook`
2. Create new notebook from the web interface
3. Execute this code:
```
%%timeit
sum(range(1_000_000))
```
4. Execute this code:
```
from psutil import virtual_memory, disk_usage, cpu_count, os

bytes_in_gb = 1024**3

print("Memory:\t",round(virtual_memory().total/bytes_in_gb,4), "Gigabytes")
print("Disk:\t",round(disk_usage(os.path.abspath(os.sep)).total/bytes_in_gb,4), "Gigabytes")
print("CPUs:\t", cpu_count())
```

#### Clone this repository
1. Visit this web page: https://github.com/falconair/ProgrammingForAnalytics
2. Click "Clone or download" and pick the "Download ZIP" option (unless you already have a GitHub account)

### The following steps are optional
#### Install Git and Git Bash
Please intall Git, a version control sotware, from this website: https://git-scm.com/downloads (you are ok to use default settings)

Note that this is a command-line tool. Once installed, you may not see a new icon to click. We will install a Desktop client to remedy this.

Although we don't make heavy use of version control, you will be introduced to the concept. Installing Git also installs "Git Bash," and comand line environment which simulates Unix/Linux. We will do several exercises which will require this environment.

###### Additional steps:
1. Install a _Graphical_ interface to Git from this website: https://desktop.github.com/
2. [Windows users only] 
  a. type `cd` (this will take you to your home directory)
  b. type `echo cd >> .profile` (this will make sure your home directory is loaded when you start Git Bash)

#### Install Visual Studio Code
Please install Visual Studio Code from https://code.visualstudio.com/

#### Additional steps:
Install Python extensions from https://marketplace.visualstudio.com/items?itemName=ms-python.python (visit that page and click "Install")

