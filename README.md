# Instagram-DM-bot1
A bot that can reply to basic one line texts.

## Features

- customizable list of expected texts and responses
- logs all texts with their respective usernames and at what exact time
- the bot uses mouse to navigate(this will be upgraded in the second version)


## How it works
1. **notification_alert.py** needs the desktop page of your [inbox](https://www.instagram.com/direct/inbox/).
2. it also needs the elements of the page ```ctrl/cmd  + shft  + i```.
3. it needs the ```<title>``` element(found under the ```<head>``` dropdown to check for new notifications.
4. the mouse goes to the specific position of the element and updates every second. 
5. when there is a new message, the same script logs the person/people that sent a new message and goes to 

## Installation

Instagram DM Bot1 needs python 3.8 to run and the following modules.

tested in spyder 5.0.5

## Modules
| Plugin | Pypi |
| ------ | ------ |
| pynput | [/project/pynput/](https://pypi.org/project/pynput/) |
| pyAutoGui | [/project/PyAutoGUI/](https://pypi.org/project/PyAutoGUI/) |
| openCV| [/project/opencv-python/](https://pypi.org/project/opencv-python/) |
| pyperclip | [/project/pyperclip3/](https://pypi.org/project/pyperclip3/) |


## License

MIT


