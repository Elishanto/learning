class Question:
    def __init__(self, qid, uid, title, desc):
        self.qid = qid
        self.uid = uid
        self.name = title
        self.desc = desc
        self.answers = []

    def __str__(self):
        return 'Question ID: {}\nUser ID: {}\nName: {}\nDescription: {}\nAnswers: {}\n'.format(self.qid, self.uid, self.name, self.desc, self.answers)