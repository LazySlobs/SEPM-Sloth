import time, pytesseract, cv2
import numpy as nm
import tkinter as tk
from PIL import ImageGrab, ImageTk

# Source code from: https://stackoverflow.com/a/58130065
# used with modifications
class ImageToText(tk.Tk):
	def __init__(self):
		super().__init__()
		self.withdraw()
		self.attributes('-fullscreen', True)

		self.canvas = tk.Canvas(self)
		self.canvas.pack(fill="both",expand=True)

		image = ImageGrab.grab()
		self.image = ImageTk.PhotoImage(image)
		self.photo = self.canvas.create_image(0,0,image=self.image,anchor="nw")

		self.x, self.y = 0, 0
		self.rect, self.start_x, self.start_y = None, None, None
		self.deiconify()

		self.canvas.tag_bind(self.photo,"<ButtonPress-1>", self.on_button_press)
		self.canvas.tag_bind(self.photo,"<B1-Motion>", self.on_move_press)
		self.canvas.tag_bind(self.photo,"<ButtonRelease-1>", self.on_button_release)

	def on_button_press(self, event):
		self.start_x = event.x
		self.start_y = event.y
		self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')

	def on_move_press(self, event):
		curX, curY = (event.x, event.y)
		self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

	def on_button_release(self, event):
		bbox = self.canvas.bbox(self.rect)
		self.canvas.destroy()
		self.destroy()
		
		# Path of tesseract executable
		# Download the installers here: https://github.com/UB-Mannheim/tesseract/wiki
		pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
		
		while(True):
			# ImageGrab-To capture the screen image in a loop.
			# Bbox to capture a specific area.
			# In Pillow, bbox is a tuple, it contains four elements: (left, upper, right, lower)
			# which determine a pixel coordinate of region. None = screen size.
			cap = ImageGrab.grab(bbox = bbox)

			# Converted the image to monochrome for it to be easily
			# read by the OCR and obtained the output String.
			tesstr = pytesseract.image_to_string(
					cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
					lang ='eng')
			print(tesstr)
			time.sleep(1)

root = ImageToText()
root.mainloop()
