from importlib.resources import path
import json
from pynput.mouse import Listener
import os
import pyautogui
import datetime;

class Photo:
  def __init__(self):
    self.count = 100
    self.coordiantes = []
    self.timestemp = 0
    self.time = 0

  def take_photo(self, mouseX, mouseY):
      format_x = mouseX - 10
      format_y = mouseY - 10
      myScreenshot = pyautogui.screenshot(region=(format_x, format_y, 20, 20))
      # path = os.path.join(os.path.dirname(__file__), "my_flags", "flag_{0}.png".format(self.count))
      path="flags/flag_{}.PNG".format(self.count)
      self.count = self.count + 1
      myScreenshot.save(path)
      now = datetime.datetime.now().timestamp()
      if self.timestemp == 0:
        self.timestemp = now
        infos = {
        "path": path,
        "wait": 3
        }
        self.coordiantes.append(infos)
      else:
        self.time = self.timestemp - now
        infos = {
        "path": path,
        "wait": abs(int(self.time)) + 3
        }
        self.timestemp = now
        self.coordiantes.append(infos)
      return

  def click(self, x, y, button, pressed):
      print(button.name)
      if button.name == 'right':
        with open('infos.json', 'w') as file:
         file.write(json.dumps(self.coordiantes))
        return False
      if pressed:
        self.take_photo(x, y)

photo = Photo()

with Listener(on_click=photo.click) as listener:
    listener.join()