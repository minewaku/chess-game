class Message:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message

    def __str__(self):
        return f'{self.sender} -> {self.receiver}: {self.message}'