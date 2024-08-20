# Python Flow Control Tools & Musical Experimentations 

## Summary

The class will introduce students to Python flow control tools such as *if-else statements*, *match-case statements*, *iterables*, *advanced functions* and more ways to divert the flow of your program.

## Prerequisites

For this class we will need to install some third-party libraries, namely **pydub**, which requires us to use **virtual environments** — picture them as a box in which your programs and libraries that support them reside.

They are completely isolated from other virtual environments and you will have to create them and install required packages for every new project you do. But they make for a good isolated container that only has tools essential for the job.

---

### Windows

#### Install ffmpeg

1. [Download ffmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) and unarchive it

2. Go to the unarchived folder, locate `bin` folder and copy its path

3. Open search (`Win+S`) and search for `Edit the system environmental variables`

4. Navigate to `Environment variables...` -> `System variables` -> `Path` and double-click it

5. Paste the copied path into an empty field and click "ok"

6. Test the installation by typing `ffmpeg` to your terminal

#### Create a virtual environment

1. Create a folder whereever you'd like and open your terminal (or code editor with terminal) there

2. Create a virtual environment in the current directory (`.`):

    `py -m venv .`

3. Activate it:

    `.\Scripts\activate`

    if your next prompt starts with `(python)` or `(<current-directory-name>)` then you have successfully activated your virtual environment and can now work on your code. But first we need to install some packages

4. Install **pydub** and **pyaudio**:

    `pip install pydub pyaudio`
---

### Mac OS

#### Install ffmpeg and PortAudio

1. Install **HomeBrew** — a convinient package manager for Mac OS and Linux:

    `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

2. Add it to your PATH:

    `echo "export PATH=/opt/homebrew/bin:$PATH" >> ~/.bash_profile && source ~/.bash_profile`

3. Install ffmpeg and PortAudio:

    `brew install ffmpeg portaudio`


#### Create a virtual environment

1. Create a folder whereever you'd like and open your terminal (or code editor with terminal) there

2. Create a virtual environment in the current directory (`.`):

    `python3 -m venv .`

3. Activate it:

    `source ./bin/activate`

    if your next prompt starts with `(python)` or `(<current-directory-name>)` then you have successfully activated your virtual environment and can now work on your code. But first we need to install some packages

4. Install **pydub** and **pyaudio**:

    `pip install pydub pyaudio`
---

### Linux

#### Install ffmpeg

1. Use your package manager to install ffmpeg. For example on Ubuntu/Debian/Mint:

    `sudo apt update && sudo apt install ffmpeg`

2. Test the installation by typing `ffmpeg` to your terminal

#### Create a virtual environment

1. Create a folder whereever you'd like and open your terminal (or code editor with terminal) there

2. Create a virtual environment in the current directory (`.`):

    `python -m venv .`

3. Activate it:

    `source ./bin/activate`

    if your next prompt starts with `(python)` or `(<current-directory-name>)` then you have successfully activated your virtual environment and can now work on your code. But first we need to install some packages

4. Install **pydub**:

    `pip install pydub`