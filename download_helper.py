import os
import pytube
from pytube.cli import on_progress
import time

def download_videos(url_list, download_path, format_option='mp4', resolution_option=720):
    success_count = 0
    failure_count = 0

    total_start = time.time() # 记录总耗时的起始时间

    for idx, url in enumerate(url_list, start=1):
        try:
            print(f'🎬 正在解析视频链接: {url}...')
            youtube = pytube.YouTube(url)
            video_title = youtube.title

            print(f'📺 正在下载视频: {idx}. {video_title}...')

            video = youtube.streams.filter(file_extension=format_option, res=resolution_option).first()

            start = time.time() # 记录下载的起始时间
            video.download(download_path)
            end = time.time() # 记录下载的结束时间

            print(f'✅ 成功下载视频: {idx}. {video_title}! 🥳')
            success_count += 1

            # 计算下载耗时
            duration = round(end - start, 2)
            print(f'⌛️ 下载耗时: {duration}秒')

        except Exception as e:
            print(f'❌ 下载视频发生错误: {e}')
            failure_count += 1
    
    total_end = time.time() # 记录总耗时的结束时间
    total_duration = round(total_end - total_start, 2) # 计算总耗时

    total_count = success_count + failure_count
    print(f'\n🎉 恭喜您！下载已完成！此次下载共 {total_count} 个任务，成功 {success_count} 个，失败 {failure_count} 个')
    print(f'⌛️ 总耗时: {total_duration}秒')

def download_youtube_videos_from_file(file_path, download_path, format_option='mp4', resolution_option=720):
    with open(file_path, 'r') as file:
        url_list = file.readlines()
        url_list = [url.strip() for url in url_list if url.strip()]
    
    print('🚀 正在启动下载脚本...')
    print('📝 正在导入视频列表...\n')
    
    download_videos(url_list, download_path, format_option, resolution_option)

def is_video_age_restricted(url):
    video = pytube.YouTube(url)
    return video.age_restricted

# 使用示例
file_path = 'videos.txt'
download_path = 'E:/Resources/Video/yt-dl-download'
format_option = 'mp4'
resolution_option = 1080

print('💪 脚本开始工作...')
print('😎 正在解析视频...')

download_youtube_videos_from_file(file_path, download_path, format_option, resolution_option)