# 使用指南和说明

> 在使用此脚本之前，请确保计算机上已安装 `Python` 环境和 `pip`。

## 如何安装依赖项

- `Python`
  - 前往 [www.Python.org](https://www.Python.org/)，下载对应版本并完成安装。
- `pip`
  - 运行以下命令来安装 pip。
    ```ps
    python get-pip.py
    ```
- `pytube`
  - 运行以下命令来安装 pytube。
    ```ps
    pip install pytube
    ```

# 使用方法

- 下载并解压 [最新版本](https://github.com/iamalexblue/pytube/releases) 脚本。
- 使用 VScode 或记事本打开 download_helper.py 文件。
- 在文件中找到以下行：
    ```ps
    download_path = 'E:/Resources/Video/yt-dl-download'
    ``` 
- 使用你希望保存视频的地址替换引号 `''` 中的代码。
- 打开终端并跳转到你解压的文件夹位置，例如：
    ```ps
    cd E:/Download/V.0.0.1/
    ```
- 打开 `videos.txt`，逐行将 YouTube 视频链接粘贴到其中。
- 在终端中粘贴以下代码以启动下载脚本并开始下载视频。
    ```ps
    py download_helper.py
    ```
