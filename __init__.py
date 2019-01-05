from mycroft import MycroftSkill, intent_file_handler


class Mediaalarm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mediaalarm.intent')
    def handle_mediaalarm(self, message):
        self.speak_dialog('mediaalarm')


def create_skill():
    return Mediaalarm()

