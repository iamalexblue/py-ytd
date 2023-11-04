from pytube import YouTube
from pytube.cli import on_progress

# 设置登录信息
username = 'fortminor0308@gmail.com'
password = 'nuzbvdqhgnkbzlie'

# 读取视频链接文件
with open('videos.txt', 'r') as file:
    video_urls = file.read().splitlines()

for video_url in video_urls:
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)

        # 解析视频标题
        video_title = yt.title
        print(f"开始下载视频：{video_title}")

        # 登录账号
        yt.login(username, password)

        # 选择视频质量和格式
        video = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

        # 指定保存路径和文件名
        output_path = 'E:\Resources\Video\yt-dlp-download'
        filename = video.default_filename

        # 下载视频
        video.download(output_path=output_path, filename=filename)

        print(f"已完成下载：{video_title}\n")

    except Exception as e:
        print(f"下载视频时发生错误: {str(e)}")

print("所有视频都已下载完成！")