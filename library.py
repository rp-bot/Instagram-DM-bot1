import re
import datetime
now = datetime.datetime.today().strftime("%H:%M:%S")
tdy = datetime.datetime.today().strftime("%d-%b-%y %H:%M")
date = datetime.datetime.today().strftime("%d-%b-%y")

greetings = ['how are you', 'how r you', 'how r u', 'hru',
             r"how\Ws life", "how you doing", 'how r u doing',
             r"how\Ws it going", r"what\Ws up\b"]

hellos = [r'\bhey\b', r'\bhi\b', r'\bhii\b', 'hello']

wishes = ['goodluck', 'all the best', 'best of luck',
          'hope you have a good day', 'hope u have a good day',
          'happy birthday', 'happy bday']

basic_answers = ['good', r"i\Wm good", "great", 'not good',
                 'not so good',
                 'not bad', r"i\Wm fine", r"i\Wm alright"]

kill_text_ = r"\bstop\b"

dictkeys = ['say_hello', 'wish_back', 'greet', 'answer']
replies = {'say_hello': ['hey!!', 'hii!', 'hello', 'sup'],
           'wish_back': ['thank you sm!', 'thanks', 'thank you', 'thank you!'],
           'greet': ["i'm good thanks for asking", "i'm good", 'good,thank u'],
           'answer': ""}


github_link = '<https://github.com/rp-bot/Instagram-DM-bot1>'
logfile_users = f'logs/userlog_{date}.txt'
logfile_chatnum = f'logs/chatlog_{date}.txt'
logfile_texts = f'logs/textslog_{date}.txt'


class PhraseLookup:
    def __init__(self, text):
        self.text = text
        self.greetings_l = greetings
        self.hellos_l = hellos
        self.wishes_l = wishes
        self.basic_answers_l = basic_answers
        self.kill_text_ = kill_text_
        self.eval_result = ''
        self.greetings()
        self.hellos()
        self.wishes()
        self.basic_answers()
        self.kill_text()
        if self.eval_result == '':
            self.eval_result = 'inconclusive'

    def greetings(self):
        for phrase in self.greetings_l:
            search = re.search(phrase, self.text)
            if search:
                self.eval_result = "greet"
                break
            else:
                continue

    def hellos(self):
        for phrase in self.hellos_l:
            search = re.search(phrase, self.text)
            if search:
                self.eval_result = "say_hello"
                break
            else:
                continue

    def wishes(self):
        for phrase in self.wishes_l:
            search = re.search(phrase, self.text)
            if search:
                self.eval_result = "wish_back"
                break
            else:
                continue

    def basic_answers(self):
        for phrase in self.basic_answers_l:
            search = re.search(phrase, self.text)
            if search:
                self.eval_result = "answer"
                break
            else:
                continue

    def kill_text(self):
        search = re.search(self.kill_text_, self.text)
        if search:
            self.eval_result = "kill"

    def __str__(self):
        return self.eval_result
