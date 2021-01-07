from os import listdir
import os
from PIL import Image, ImageFile
   
for file_name in listdir('./'):
  if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png') or file_name.endswith('.svg') or file_name.endswith('.gif') or file_name.endswith('.ico'):	
    try:
      deleted = open("deleted_files.txt", "a+", encoding='utf-8')
      photo = Image.open('./'+file_name)
      photo.verify()
    except (IOError, SyntaxError) as e:
      deleted.write(file_name + "\n")
      photo.close()
      os.remove(file_name)
      print("Deleted file: " + file_name)
      