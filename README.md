# Instagram-DM-bot1
A bot that can reply to basic one line texts.

## Features

- customizable list of expected texts and responses
- logs all texts with their respective usernames and at what exact time
- the bot uses mouse to navigate(this will be upgraded in the second version)


### How it works
1. **notification_alert.py** needs the desktop page of your [inbox](https://www.instagram.com/direct/inbox/).
2. it also needs the elements of the page ```ctrl/cmd  + shft  + i```.
3. it needs the ```<title>``` element(found under the ```<head>``` dropdown to check for new notifications.
4. the mouse goes to the specific position of the element and updates every second. 
5. when there is a new message, the same script logs the person/people that sent a new message and goes to 

## Installation
