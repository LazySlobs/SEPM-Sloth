import time, pytesseract, cv2
import numpy as nm
import tkinter as tk
from PIL import ImageGrab, ImageTk
from core.speak import voice_assistant_speak

# Source code from: https://stackoverflow.com/a/58130065
# and https://www.geeksforgeeks.org/python-using-pil-imagegrab-and-pytesseract/
# Used with modifications.
class ImageToText(tk.Tk):
	def __init__(self):
		super().__init__()
		self.withdraw()	# hide window
		self.attributes('-fullscreen', True) # make window fullscreen
		self.attributes("-topmost", True) # put window above all other windows

		self.canvas = tk.Canvas(self) # create tkinter canvas window
		self.canvas.pack(fill="both",expand=True) # 

		image = ImageGrab.grab() # takes a snapshot of the entire screen
		self.image = ImageTk.PhotoImage(image)
		self.photo = self.canvas.create_image(0,0,image=self.image,anchor="nw")

		self.x, self.y = 0, 0 # init x and y values
		self.rect, self.start_x, self.start_y = None, None, None # init x and y values
		self.deiconify() # display the window

		self.canvas.tag_bind(self.photo,"<ButtonPress-1>", self.on_button_press)
		self.canvas.tag_bind(self.photo,"<B1-Motion>", self.on_move_press)
		self.canvas.tag_bind(self.photo,"<ButtonRelease-1>", self.on_button_release)

		voice_assistant_speak("Please select an area of text on your screen.")

	# get x and y axis of the cursor on mouse press
	def on_button_press(self, event):
		self.start_x = event.x
		self.start_y = event.y
		self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')

	# get and update the 2nd x and y axis of the cursor when mouse1 is held and the mouse is moved
	def on_move_press(self, event):
		curX, curY = (event.x, event.y)
		self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

	# get bbox coordinates and convert the texts in the selected area
	# and read the text
	def on_button_release(self, event):
		bbox = self.canvas.bbox(self.rect)
		self.canvas.destroy()
		self.destroy()
		
		# Path of tesseract executable
		# Download the installers here: https://github.com/UB-Mannheim/tesseract/wiki
		pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
		
		# ImageGrab-To capture the screen image in a loop.
		# Bbox to capture a specific area.
		# In Pillow, bbox is a tuple, it contains four elements: (left, upper, right, lower)
		# which determine a pixel coordinate of region. None = screen size.
		cap = ImageGrab.grab(bbox = bbox)

		# Converted the image to monochrome for it to be easily
		# read by the OCR and obtained the output String.
		tesseract = pytesseract.image_to_string(
				cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
				lang ='eng')
		print(tesseract)
		try:
			voice_assistant_speak(tesseract)
		except:
			voice_assistant_speak("Sorry, I can't quite recognize the text.")
		
		# loop version
		# while(True):
		# 	# ImageGrab-To capture the screen image in a loop.
		# 	# Bbox to capture a specific area.
		# 	# In Pillow, bbox is a tuple, it contains four elements: (left, upper, right, lower)
		# 	# which determine a pixel coordinate of region. None = screen size.
		# 	cap = ImageGrab.grab(bbox = bbox)

		# 	# Converted the image to monochrome for it to be easily
		# 	# read by the OCR and obtained the output String.
		# 	tesstr = pytesseract.image_to_string(
		# 			cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
		# 			lang ='eng')
		# 	print(tesstr)
		# 	voice_assistant_speak(tesstr)
		# 	time.sleep(1)

# root = ImageToText()
# root.mainloop()
