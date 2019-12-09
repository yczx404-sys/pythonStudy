from datetime import date
import sys
print(sys.path)
# ['F:\\pythonCode\\pythonStudy\\pythonBasic\\dateTime', 
#'c:\\Users\\liuchao\\AppData\\Local\\Programs\\Python\\Python38',
#'c:\\Users\\liuchao\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 
#'c:\\Users\\liuchao\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 
#'c:\\Users\\liuchao\\AppData\\Local\\Programs\\Python\\Python38\\lib',
#'c:\\Users\\liuchao\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']

# 日期类
print(date.max)
print(date.min)
print(date.resolution)
d = date.today()
print(d.day)
print(d.timetuple())
