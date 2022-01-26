# uppercase-indicator-in-a-system-tray-icon
Only works on Windows, I didn't try it on linux.



# How to setup it
1 : 
You need python:
download link : https://www.python.org/downloads/
You have to download it with the pip

2 : 
Open cmd and type:
pip install infi.systray
close the cmd

Now you can use it, but you have to lunch it everytime using the lunch.bat file
With all the next step it will start at the startup of your computer

3 :
tap : windows + r
%appdata%
go to : AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

4 : 
Create a short cut of lunch.bat
put it in the the folder you had open in the step 3

5 : 
When you start your computer,  now it will create a system tray icon, and a cmd windows, you can close the cmd it doesn't matter
You can now use it !



I used this lib : https://github.com/Infinidat/infi.systray to make the system tray icon
