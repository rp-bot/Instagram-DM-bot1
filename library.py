import re

greetings = ['how are you', 'how r you', 'how r u', 'hru',
             "how's life", "how you doing", 'how r u doing', "how's it going"]
hellos = ['hey', 'hi', 'hii', 'hello']
wishes = ['goodluck', 'all the best', 'best of luck',
          'hope you have a good day', 'hope u have a good day',
          'happy birthday']
basic_answers = ['good', "i'm good", "great", 'not good', 'not so good',
                 'not bad', "i'm fine", "i'm alright"]
dictkeys = ['hellos', 'wishes', 'greet', 'answer']


class PhraseLookup:
    def __init__(self, text):
        self.text = text

    def greetings(self):
        for phrase in greetings:
            search = re.search(phrase, self.text)
            if search:
                return "greet"
            else:
                continue

    def hellos(self):
        for phrase in hellos:
            search = re.search(phrase, self.text)
            if search:
                return "hellos"
            else:
                continue

    def wishes(self):
        for phrase in wishes:
            search = re.search(phrase, self.text)
            if search:
                return "wishes"
            else:
                continue

    def basic_answers(self):
        for phrase in basic_answers:
            search = re.search(phrase, self.text)
            if search:
                return "answer"
            else:
                continue
