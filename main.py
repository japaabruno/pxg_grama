from time import sleep
from turtle import pos
import button
import keyboard
import pyautogui
import json

right = (1019,486,70,70)
left = (835,486,70,70)
top = (926,394,70,70)
bot = (926,579,70,70)

list_positions = [right, left, top, bot]

def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

def get_bush(location):
  if location != None:
    move(location)
    keyboard.press(button.key['F2'], 0.5)
    pyautogui.click()
    sleep(4)

def move_and_click(location):
  move(location)
  pyautogui.click()

# for index in range(7):
#   while True:
#     position_in_map = pyautogui.locateOnScreen('./flags/flag_{}.png'.format(index), confidence=0.80)
#     print("position_in_map", position_in_map)
#     if position_in_map != None:
#       move_and_click(position_in_map)
#       sleep(6.5)
#       check_position = pyautogui.locateOnScreen('./flags/flag_{}.png'.format(index), confidence=0.80)
#       if check_position == None:
#         for position in list_positions:
#           for index in range(3):  
#             print('tentando localizar bush')    
#             bush = pyautogui.locateOnScreen('bushs/bush_{}.PNG'.format(index), confidence=0.85, region=position)
#             print("bush", bush)
#             get_bush(bush)
#         break

with open('infos.json', 'r') as file:
    info = file.read()
load_infos = json.loads(info)

cont = 0
while True:
  for item in load_infos:
    while True:
      position_in_map = pyautogui.locateOnScreen(item['path'], confidence=0.82)
      print(position_in_map, item)
      if cont == 6:
        cont=0
        break
      cont= cont+1 
      if position_in_map != None:
        cont=0
        move_and_click(position_in_map)
        sleep(item["wait"])
        check_position = pyautogui.locateOnScreen(item['path'], confidence=0.80)
        if check_position == None:
          for position in list_positions:
            for item in range(3):
              detected_bush = pyautogui.locateOnScreen('bushs/bush_{0}.PNG'.format(item), confidence=0.85, region=position)
              get_bush(detected_bush)
          break

# while True:
#   for position in list_positions:
#     for item in range(3):
#       detected_bush = pyautogui.locateOnScreen('bushs/bush_{}.PNG'.format(0), confidence=0.85, region=position)
#       print(detected_bush)
#       get_bush(detected_bush)