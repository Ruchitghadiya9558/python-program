class mycustomarerror():
    def __init__(self ,*args):
        if args:
            self.msg = args[0]
        else:
            self.msg = None
    def __str__(self):
        if self.msg is None:
            return "hamare code me error hai"
        else:
            return self.msg


