import tagui as t
import time
import os

t.init()

# Open File Explorer using Win + E
t.keyboard('[win] + e')
time.sleep(2)

# Navigate to Desktop using address bar shortcut (Ctrl + L)
t.keyboard('[ctrl] + l')
t.keyboard(os.path.join(os.environ['USERPROFILE'], 'Desktop') + '[enter]')
time.sleep(2)

# Right click on a general area in the window
# You may need to adjust the coordinates (300,300) based on your resolution
t.mouse(300, 300, 'right')
time.sleep(1)

# Press W (for "New") and F (for "Folder")
t.keyboard('w')
t.keyboard('f')
time.sleep(1)

# Type the folder name and press Enter
folder_name = "MyTestFolder"
t.keyboard(folder_name + '[enter]')

time.sleep(1)
t.close()
