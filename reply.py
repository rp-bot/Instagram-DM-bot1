import os
import pyperclip
import time
import re
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
            del firstline_eval
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
        user = re.search(r"(?<=@).*(?= sent)", user[-(users+1)]).group()
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
    time.sleep(1)
    try:
        dots_loc = pt.locateOnScreen(dots_im, confidence=0.9)
        pt.moveTo(dots_loc[0:2], duration=.2)
    except TypeError:
        pt.moveRel(0, -60, duration=0.2)
    try:
        dots_loc = pt.locateOnScreen(dots_im, confidence=0.9)
        pt.moveTo(dots_loc[0:2], duration=.2)
    except TypeError:
        pass
    else:
        pt.leftClick(duration=0.1)
        pt.moveRel(120, -29, duration=0.2)
        pt.leftClick(duration=0.1)
        buffer()
    finally:
        pass


def paste():
    keyboard = keyboard_con()
    keyboard.press(Key.ctrl)
    time.sleep(0.2)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')


def evalndel(numberoftexts):
    global totaltext
    logslist = open(lib.logfile_texts, 'r').readlines()
    latest = ''
    prev = ''
    prev_user = ''
    if numberoftexts > 0:
        latest = re.search(r'(?<=-- ).*', logslist[-1]).group()
        if numberoftexts > 1:
            prev = re.search(r'(?<=-- ).*', logslist[-2]).group()
        if len(logslist) > 3:
            try:
                prev_user = re.search(r'(?<=-- ).*', logslist[-4]).group()
            except AttributeError:
                try:
                    prev_user = re.search(r'(?<=-- ).*', logslist[-5]).group()
                except IndexError:
                    pass
                except AttributeError:
                    pass
                pass
        if numberoftexts == 1 and latest == prev_user:
            os.system('''cd logs/ && sed -i '$d' textslog.txt &&
            sed -i '$d' textslog.txt''')
            totaltext -= 1
            languagecompute.marker = 1
        if latest == prev:
            print(totaltext)
            print('totaltext soon -1')
            os.system("cd logs/ && sed -i '$d' textslog.txt")
            totaltext -= 1
            languagecompute.marker = 1
    else:
        pass


def languagecompute(index):
    global userlist, totaltext, textlogger
    fixedloc = (657, 1329)
    languagecompute.marker = 0
    while languagecompute.marker == 0:
        dynamicloc = (fixedloc[0], fixedloc[1]-(totaltext*55))
        copy(dynamicloc)
        clipboard = pyperclip.paste().lower()
        totaltext += 1
        # PhraseLookup(clipboard)
        result = re.search("happy birthday|happy bday", clipboard)
        logger(userlist[index], clipboard)
        print(userlist[index])
        evalndel(totaltext)
        if result:
            reply()  # future add parameter for what the match was
            break
        else:
            continue


def reply():
    pyperclip.copy("Thank you sm!")
    logger("bot", pyperclip.paste(), bot=True)
    pt.moveTo(657, 1397, duration=.2)
    pt.leftClick(duration=0.1)
    paste()
    # time.sleep(1)
    keyboard = keyboard_con()
    keyboard.press(Key.enter)
    time.sleep(.2)
    pt.leftClick(duration=0.1)


def bot_init():
    bot_on = True
    while bot_on:
        global userlist, userindex, totaltext
        userlistgen()
        userlist = userlist[::-1]
        print(userlist)
        for index in range(len(userlist)):
            logger(newuser=True)
            y = 345+(index*70)
            pt.moveTo(265, y, duration=0.2)
            pt.leftClick(duration=.3)
            totaltext = 0
            languagecompute(index)
            if index == len(userlist)-1:
                pt.moveTo(824, 158, duration=0.3)
                pt.leftClick(duration=0.2)
        print("breakin loop")  # contin
        break


if __name__ == '__main__':
    time.sleep(2)
