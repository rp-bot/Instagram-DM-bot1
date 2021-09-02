import os
import pyperclip
import time
import re
import random
import pyautogui as pt
from pynput.keyboard import Key, Controller as keyboard_con
import library as lib


def logger(user='', message='', bot=False, newuser=False):
    f = open(f"{lib.logfile_texts}", 'a')
    if newuser is True:
        print('hey')
        firstline_eval = open(f"{lib.logfile_texts}", 'r').readlines()
        if len(firstline_eval) == 0:
            print('hey from 0lines')
            f.write(f"--/{lib.tdy}")
        else:
            f.write(f"\n\n--/{lib.tdy}")
    elif bot is True:
        f.write(f"\n{lib.now} - //@{user} -- {message}")
    elif bot is False and newuser is False:
        f.write(f"\n{lib.now} - @{user} -- {message}")
    f.close()


def userlistgen():
    global userlist
    chatnumlog = open(lib.logfile_chatnum, 'r').readlines()
    chatnumlog = re.search(r'(?<=\()\w+(?=\))', chatnumlog[-1]).group()
    userlist = []
    print(chatnumlog)
    for users in range(int(chatnumlog)):
        user = open(lib.logfile_users, 'r').readlines()
        user = re.search(r"(?<=@).*(?= sent)", user[-(users + 1)]).group()
        userlist.append(user)


def buffer():
    pt.moveRel(20, -10, duration=.2)
    pt.moveRel(-60, 0, duration=.2)
    time.sleep(.2)
    pt.moveRel(0, -150, duration=.2)
    pt.moveRel(0, 0, duration=.2)


def copy(initial):
    dots_im = 'learningimages/3dots.png'
    pt.moveTo(initial, duration=.2)
    try:
        dots_loc = pt.locateOnScreen(dots_im, confidence=0.9)
        pt.moveTo(dots_loc[0:2], duration=.1)
    except TypeError:
        pt.moveRel(0, -60, duration=0.1)
    try:
        dots_loc = pt.locateOnScreen(dots_im, confidence=0.9)
        pt.moveTo(dots_loc[0:2], duration=.1)
    except TypeError:
        pass
    else:
        pt.leftClick(duration=0.1)
        pt.moveRel(120, -29, duration=0.2)
        pt.leftClick(duration=0.1)
        pass
    finally:
        pass


def paste():
    keyboard = keyboard_con()
    keyboard.press(Key.ctrl)
    time.sleep(0.1)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')


def evalndel(textback, clipboard):
    logslist = open(lib.logfile_texts, 'r').readlines()
    prev = ''
    try:
        prev = re.search(r'(?<=-- ).*', logslist[-2]).group()
    except AttributeError:
        pass
    except IndexError:
        pass
    if clipboard == '':
        languagecompute.marker = 1
    elif clipboard == prev:
        os.system("cd logs/ && sed -i '$d' textslog.txt")
        languagecompute.marker = 1


def languagecompute(index):
    global userlist, totaltext, textlogger
    fixedloc = (657, 1329)
    languagecompute.marker = 0
    while languagecompute.marker == 0:
        pyperclip.copy('')
        dynamicloc = (fixedloc[0], fixedloc[1] - (totaltext * 55))
        copy(dynamicloc)
        clipboard = pyperclip.paste().lower()
        totaltext += 1
        textback = lib.PhraseLookup(clipboard)
        textback = textback.eval_result
        evalndel(textback, clipboard)
        if languagecompute.marker == 0 and textback != 'inconclusive':
            logger(userlist[index], clipboard)
            reply(textback)
        elif textback == 'inconclusive' and languagecompute.marker == 0:
            reply(inconclusive=True)
            break
        elif languagecompute.marker == 1:
            logger(userlist[index], '//end conversation')
            break


def reply(text='-', inconclusive=False):
    if inconclusive is False and text != 'answer' and text != 'kill':
        index = random.randint(0, len(lib.replies[text]) - 1)
        pyperclip.copy(lib.replies[text][index])
        logger("bot", pyperclip.paste(), bot=True)
        pt.moveTo(657, 1397, duration=.2)
        pt.leftClick(duration=0.1)
        paste()
        keyboard = keyboard_con()
        time.sleep(.2)
        keyboard.press(Key.enter)
    elif text == 'answer':
        pass
    elif text == 'kill':
        pyperclip.copy("thanks for the convo, this has been a learning curve"
                       ", wait while I notify Prat.\n\n" +
                       "you can clone me from\n\n" + lib.github_link)
        logger("bot", " killed", bot=True)
        pt.moveTo(657, 1397, duration=.2)
        pt.leftClick(duration=0.1)
        paste()
        keyboard = keyboard_con()
        time.sleep(.2)
        keyboard.press(Key.enter)
    elif inconclusive is True:
        pyperclip.copy("at this time, I can only compute one line at a time" +
                       " and can only handle a few basic strings" +
                       "\n\nType [stop] to make me shut up")
        logger("bot", " cover blown", bot=True)
        pt.moveTo(657, 1397, duration=.2)
        pt.leftClick(duration=0.1)
        paste()
        keyboard = keyboard_con()
        time.sleep(.2)
        keyboard.press(Key.enter)
        pyperclip.copy('')
    time.sleep(.5)


def bot_init():
    bot_on = True
    while bot_on:
        global userlist, userindex, totaltext
        userlistgen()
        userlist = userlist[::-1]
        print(userlist)
        for index in range(len(userlist)):
            pyperclip.copy('')
            logger(newuser=True)
            print('hey from for loop')
            y = 345 + (index * 70)
            pt.moveTo(265, y, duration=0.2)
            pt.leftClick(duration=.3)
            totaltext = 0
            languagecompute(index)
            pyperclip.copy('')
            if index == len(userlist) - 1:
                pt.moveTo(824, 158, duration=0.3)
                pt.leftClick(duration=0.2)
        print("breakin loop")
        break
