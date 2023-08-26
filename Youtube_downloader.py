import pytube

url=input("İndirmek istediğiniz videonun linkini girin: ")

path="C:\\Users\\abuka\\Downloads"

pytube.YouTube(url).streams.get_highest_resolution().download(path)


