from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
# pip install requests
# import requests

# url = 'https://www.youtube.com/watch?v=kIEWJ1ljEro'
# apikey = '7f320a4976c8824a8bf05d6642b6f3ee59a06093'
# params = {
#     'url': url,
#     'apikey': apikey,
# 	'autoparse': 'true',
# }
# response = requests.get('https://api.zenrows.com/v1/', params=params)
# print(response.text)

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("video downloaded successfully!")
        
    except Exception as e:
        print(e)
        
url= "https://www.youtube.com/watch?v=kIEWJ1ljEro"

save_path = "E:/5-MyProject/3-Python/Download"

download_video(url, save_path)

#Bị chống cào dữ liệu từ Youtube... Cân nhắc tìm cách sửa sau.