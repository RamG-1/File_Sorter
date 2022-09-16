import os
import shutil

src_dir = "Your Source Path"
doc_dest = "Doc Folder Destination Path"
img_dest = "Img Folder Path"
vid_dest = "Video Folder Path"
aud_dest = "Audio Folder Dest Path"
mix_dest = "Mix Files Folder Dest Path"

#Image_Xtensions
image_extensions = (".jpg", ".jpeg", ".JPG", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico")
# ? supported Video types
video_extensions = (".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", "MOV",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd")
# ? supported Audio types
audio_extensions = (".m4a", ".flac", "mp3", ".wav", ".wma", ".aac")
# ? supported Document types
document_extensions = (".doc", ".docx", ".odt", ".PDF",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx")


res = []
# Iterate directory
for file in os.listdir(src_dir):
    # check if current path is a file
    if os.path.isfile(os.path.join(src_dir, file)):
        res.append(file)

count = 0
#Printing the List Elements
for i in res:
    if i.endswith(image_extensions):
        print('This one is an Image, so')        
        current_file_dest = src_dir+'/'+i
        shutil.move(current_file_dest,img_dest)
        print(i,"Moved to images Folder...")
        count += 1
        print(count)
        print('')

    #For Videos 
    if i.endswith(video_extensions):
        print(' This one is a Video, so')       
        current_file_dest = src_dir+'/'+i
        shutil.move(current_file_dest,vid_dest)
        print(i,"Moved to Videos Folder...")
        count += 1
        print(count)
        print('')

    #For Audios 
    if i.endswith(audio_extensions):
        print('This is an Audio, so')
        current_file_dest = src_dir+'/'+i
        shutil.move(current_file_dest,aud_dest)
        print(i,"Moved to Audios Folder...")
        count += 1
        print(count)
        print('')
    #For Documents
    if i.endswith(document_extensions):
        print('This is a Document, so') 
        current_file_dest = src_dir+'/'+i
        shutil.move(current_file_dest,doc_dest)
        print(i,"Moved to Doc's Folder...")
        count += 1
        print(count)
        print('')
    else: 
        print("This is an Unknown File")
        current_file_dest = src_dir+'/'+i
        try:
            shutil.move(current_file_dest,mix_dest)
            print(i,"Moved to Mix's Folder")
            count += 1 
            print(count)
            print('')
        finally:
            print(i,"\nThis File Is Skipped Because of Confusion")
            print("")
            continue

print("The Number of Files Sorted are: ",count)

    

        




