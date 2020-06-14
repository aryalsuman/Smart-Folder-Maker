import os,time
import shutil #For copy ,move,renmae
from colored import fg, bg, attr

all_files=os.listdir()
if '--Audio--'not in  all_files:
            os.makedirs('--Audio--')
if '--Videos--'not in  all_files:
            os.makedirs('--Videos--')
if '--Images--'not in  all_files:
            os.makedirs('--Images--')  
if '--Applications--'not in  all_files:
            os.makedirs('--Applications--')  
if '--Others--'not in  all_files: 
            os.makedirs('--Others--') 
if '--Documents--'not in  all_files: 
             os.makedirs('--Documents--')
if '--Compress Files--'not in  all_files: 
            os.makedirs("--Compress Files--")
print("Connecting")
for files in all_files:
    try:
        print (f'%s Moving  {files} %s' % (fg(11), attr(0)))
        #For videos
        if files.endswith('.py') or '--Audio--'in files or '--Videos--'in files or '--Images--'in files or '--Applications--'in files   or '--Compress Files--'in files or '--Other--'in files or '--Documents--'in files:
            continue      
        elif files.endswith( (".avi", ".flv", ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv")):
            shutil.move(files,'--Videos--')
            
            #For audio
        elif files.endswith(('.mp3','.aac','.wav','.flac')):
            shutil.move(files, '--Audio--')#Move file
            #For images
        elif files.endswith(('.png','.jpeg','.gif','.png','.eps','.jpg')):
            shutil.move(files, '--Images--')#Move file
            #For --Applications--
        elif files.endswith('.exe'):
            shutil.move(files, '--Applications--')#Move file
        elif files.endswith(('.zip','.zipx','.7z','.s7z','.rar')):
            shutil.move(files,'--Compress Files--')
        elif files.endswith(('.doc','.docx','.pdf','.xls','.ppt','.txt','.pptx','.xlsx')):
            shutil.move(files,'--Documents--')
        

        else :
             shutil.move(files, '--Others--')#Move file
        print (f'%s Completed  {files} %s' % (fg(2), attr(0)))
    except:
        print(f" %sCannot Move {files}%s"% (fg(1), attr(0)))
input("%sMoving Completed.\nPress Enter to continue...%s"% (fg(2), attr(0)))
# jkhjkhjkh