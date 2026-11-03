#importing processes 
import subprocess
import os
import winsound
import json
import keyboard

with open("config.json") as f:
    pages = json.load(f)

print(pages)

def press(page, key):
    items = pages[str(page)]["items"]
    action = items.get(str(key))
    if action is None:
        print("nothing on that key")
    elif action.endswith(".wav"):
        winsound.PlaySound(action, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        os.startfile(action)

+222

def change_page(current, step):
    next_page = current+step
    if next_page > len(pages):
        return 1
    elif next_page < 1:
        return len(pages)
    else:
        return next_page


current_page = 1
while True:
    event = keyboard.read_event()
    if event.event_type != "down":
        continue
    turn = event.name
    if turn == "+":
        current_page = change_page(current_page, 1)
        print(pages[str(current_page)]["name"])
    elif turn == "-":
        current_page = change_page(current_page, -1)
        print(pages[str(current_page)]["name"])
    elif turn in ("1", "2", "3"):
        press(current_page, int(turn))

    