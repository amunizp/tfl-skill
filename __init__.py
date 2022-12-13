from mycroft import MycroftSkill, intent_file_handler


class Tfl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tfl.intent')
    def handle_tfl(self, message):
        self.speak_dialog('tfl')


def create_skill():
    return Tfl()

