import re


#img_path = r'C:\Users\DELL\AppData\Local\Programs\Python\Python37-32\python.exe "C:/Users/DELL/PycharmProjects/second pro/once.py"'
img_path=r'C:/Users/DELL/PycharmProjects/second pro/s1.jpg'
if re.search(r'\.jpg$', img_path)==False:
    print("accepted")
else:
    print("not accepted")

