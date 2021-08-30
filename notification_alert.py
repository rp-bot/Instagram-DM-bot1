import pyperclip
import time
import re
import pyautogui as pt
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as keyboard_con
import datetime
import logging
logfile_users = 'logs/userlog.txt'
logfile_chatnum = 'logs/chatlog.txt'


def user_logger(name, log_file, level=logging.INFO):
    global userlist, userindex
    logger = logging.getLogger(name)
    # if not getattr():
    # logger.propagate = False
    logger.handlers = []
    # if not logger.hasHandlers():
    formatter = logging.Formatter(
        "%(asctime)s -- %(message)s",
        datefmt='%H:%M:%S')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def chat_logger(name, log_file, level=logging.INFO):
    global userlist, userindex
    logger = logging.getLogger(name)
    # if not getattr():
    # logger.propagate = False
    logger.handlers = []
    # if not logger.hasHandlers():
    formatter = logging.Formatter(
        "%(asctime)s -- %(message)s",
        datefmt='%H:%M:%S')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def copy():
    keyboard = keyboard_con()
    keyboard.press(Key.ctrl)
    time.sleep(1)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')


def logusernames(numofchats):
    for num in range(numofchats):
        pyperclip.copy('')
        y = 345+(num*70)
        pt.moveTo(265, y, duration=0.5)
        pt.leftClick(duration=.3)
        pt.moveTo(948, 207, duration=0.3)
        pt.leftClick(duration=0.2)
        pt.moveTo(639, 367, duration=.7)
        pt.tripleClick(interval=0.4)
        copy()
        searchusername = re.search(r".*(?= won't)", pyperclip.paste()).group()
        userlogger.info("@" + f"{searchusername}" + " sent a new msg")
        if num == 0:
            chatnumlogger.info(f"({numofchats})" + " new messages")
        elif num > 0:
            pass
        pt.moveTo(824, 158, duration=0.3)
        pt.leftClick(duration=0.2)


def checkstatus():
    pyperclip.copy('')
    howmanychats_loc = (1118, 290)
    mouse = Controller()
    mouse.position = howmanychats_loc
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(0.4)
    mouse.click(Button.left, 1)
    copy()
    time.sleep(1.1)
    mouse.move(1000, 0)
    time.sleep(.5)
    mouse.click(Button.left, 1)


def evaluate_status():
    global chatnum
    while chatnum < 1:
        time.sleep(1)
        checkstatus()
        time.sleep(1)
        status = re.search(r'(?<=\()\w+(?=\))', pyperclip.paste())
        if status:
            chatnum = int(status.group())
            logusernames(chatnum)
            # run a function to add clients to text file
            break
        else:
            continue


if __name__ == '__main__':
    time.sleep(2)
    now = datetime.datetime.today().strftime("%d-%b-%y %H:%M:%S")
    tdy = datetime.datetime.today().strftime("%d-%b-%y %H:%M")
    newlogfile_users = open(logfile_users, "a")
    newlogfile_chatnum = open(logfile_chatnum, 'a')
    firstline_eval_u = open(f"{logfile_users}", 'r').readlines()
    firstline_eval_c = open(f"{logfile_users}", 'r').readlines()

    if len(firstline_eval_u) == 0:
        print('hey from 0lines')
        newlogfile_users.write(f"--/{tdy}")
    else:
        del firstline_eval_u
        newlogfile_users.write(f"\n\n--/{tdy}")

    if len(firstline_eval_c) == 0:
        print('hey from 0lines')
        newlogfile_users.write(f"--/{tdy}")
    else:
        del firstline_eval_u
        newlogfile_users.write(f"\n\n--/{tdy}")

    chatnum = 0

    userlogger = user_logger('user_logger', f'{logfile_users}')
    #
    chatnumlogger = chat_logger('chatnum_logger', f'{logfile_chatnum}')

    evaluate_status()
