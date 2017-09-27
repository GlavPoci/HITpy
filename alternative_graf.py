from Tkinter import *
from Modules.Math import *
from PIL import *
from PIL import Image
import ImageTk


#All MOdules that you need for that
#sudo apt-get install python-imaging
#sudo apt-get install python-imaging-tk
#self.pilImage = Image.open("discord.png")
#self.image = ImageTk.PhotoImage(self.pilImage)
#self.Discord = self.MainCanvas.create_image(100, 100, image=self.image)


#self.MainCanvas.tag_bind(self.Discord, '<Button-1>', self.ClearCanvas)


class MainWindow():
  def __init__(self, root):
      self.CanvasWidth, self.CanvasHeight = root.winfo_screenwidth(), root.winfo_screenheight()
      self.MainCanvas = Canvas(root, width=self.CanvasWidth - 295, height=self.CanvasHeight, bg="#484848", highlightthickness=0)
      self.DrawArray()
      self.ExitButton = Button(root, text="Exit from game", width="10", height="5")
      self.OptionsButton = Button(root, text="Options", width="10", height="5")
      self.Block = self.MainCanvas.create_polygon([0, 0, 100, 0, 100, 100, 0, 100],     outline='gray',
            fill='gray', width=2)
      #FOR MainCanvas
      self.MainCanvas.tag_bind(self.Block, '<Button-1>', self.ClearCanvas)

      self.ExitButton.pack(side = RIGHT, padx=10)
      self.MainCanvas.pack(side = LEFT)
      self.OptionsButton.pack(side = RIGHT)

      self.ExitButton.bind('<Button-1>', self.ExitFromGame)


  def ExitFromGame(self, x):
      root.destroy()

  def ClearCanvas(self, x):
      print('Discord')

  def DrawArray(self):
     for x in range(0, self.CanvasWidth, 40):
         self.MainCanvas.create_line(x, 0, x, self.CanvasHeight, fill="#323341")

     for y in range(0, self.CanvasHeight, 40):
         self.MainCanvas.create_line(0, y, self.CanvasWidth, y, fill="#323341")

root = Tk()
MainWindow = MainWindow(root)
root.attributes('-zoomed', True)
#root.attributes('-fullscreen', True)
root.title("HITpy")
#root.resizable(width=False, height=False)
root.mainloop()
