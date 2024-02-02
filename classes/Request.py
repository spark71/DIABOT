class Request:
    def __init__(self, update):
        self.update = update
        self.user_id = update.message.from_user.id
        self.user_name = update.message.from_user.username
        self.chat_id = update.message.chat_id
        self.text = update.message.text

    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name

    def get_chat_id(self):
        return self.chat_id

    def get_text(self):
        return self.text

