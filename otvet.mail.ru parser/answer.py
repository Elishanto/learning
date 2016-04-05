class Answer:
    def __init__(self, uid, text):
        self.uid = uid
        self.text = text

    def __repr__(self):
        return '{} {}'.format(self.uid, self.text)