from mycroft import MycroftSkill, intent_file_handler


class Hebert(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hebert.intent')
    def handle_hebert(self, message):
        self.speak_dialog('hebert')


def create_skill():
    return Hebert()

