class CallBack(object):
    """docstring for CallBack"""
    def __init__(self):
        super(CallBack, self).__init__()
        self.callbacks = []
        
    def add_callback(self, callback):
        self.callbacks.append(callback)

    def callback(self, data):
        print "callback list: " + str(self.callbacks)
        for callback in self.callbacks:
            callback(data)