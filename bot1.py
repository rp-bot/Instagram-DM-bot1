greetings = ['how are you', 'how r you', 'how r u', 'hru',
             "how's life", "how you doing", 'how r u doing', "how's it going"]
hellos = ['hey', 'hi', 'hii', 'hello']
wishes = ['goodluck', 'all the best', 'best of luck',
          'hope you have a good day', 'hope u have a good day',
          'happy birthday']
basic_answers = ['good', "i'm good", "great", 'not good', 'not so good',
                 'not bad', "i'm fine", "i'm alright"]
dictkeys = ['hellos', 'wishes', 'greet', 'answer']


class Botclass:
    def __init__(self, takeninput):
        self.takeninput = takeninput
        self.inputlist = ' '.join(self.takeninput).split()
        self.reply = {'hellos': 0, 'wishes': 0, 'greet': 0, 'answer': 0}

    def basic_hellos(self):
        if self.inputlist in hellos:
            self.reply['hellos'] = 'hii'
            return 'hii'

    def basic_wishes(self):
        if self.inputlist in wishes or self.takeninput in wishes:
            self.reply['wishes'] = 'thank you sm!!'
            return 'thank you sm!!'

    def basic_greet(self):
        if self.takeninput in greetings:
            self.reply['greet'] = "i'm good, hbu"
            return "i'm good, hbu"

    def basic_answers(self):
        for item in basic_answers:
            if self.takeninput == item:
                self.reply['answer'] = 1
            elif self.takeninput != item:
                split_item = ' '.join(item).split()
                for each_item in split_item:
                    if each_item in self.inputlist:
                        self.reply['answer'] = 1
                    else:
                        pass


class Execute:
    def __init__(self, takeninput):
        self.takeninput = takeninput
        self.inputlist = ' '.join(self.takeninput).split()
        # x = 0


def takeinput():

    on = True

    while on:
        takeinput = input().lower()
        reply = Botclass(takeinput)
        basichellos = reply.basic_hellos()
        basic
        reply_dict = reply.reply()
