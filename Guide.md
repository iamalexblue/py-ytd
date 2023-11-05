# Guide and Instructions

<p align="center">
  <a href="Guide_CN.md">🇨🇳 使用指南</a>
</p>

> Before using this script, make sure you have the `Python` environment and `pip` installed on your computer.

## How to install depedencies

- `Python`
  - Go to [www.Python.org](https://www.Python.org/) , download the corresponding version and complete the installation.
- `pip`
  - run this command to install pip.  
  ```ps
  python get-pip.py
  ```
- `pytube`
  - Run this command to install pytube
  ```ps
  pip install pytube
  ```

### Usage

- Download and unzip [latest release](https://github.com/iamalexblue/pytube/releases).
- Open download_helper.py with VScode or Notepad.exe.
- Look in the file for the line:

  ```ps
  download_path = 'E:/Resources/Video/yt-dl-download'
  ``` 
and replace the code in the `''` with the address you want to save the Video to.

- Open the terminal and jump to the location of the folder you extracted with below code, for example:
  ```ps
  cd E:/Download/V.0.0.1/
  ```
- open `videos.txt` and paste YouTube video links into it, one line at a time.
- Paste the following code at the Terminal to start the download script and start downloading the video.
  ```ps
  py download_helper.py
  ```