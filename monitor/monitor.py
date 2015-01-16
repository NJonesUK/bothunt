class Monitor(object):
    """docstring for Monitor"""
    def __init__(self):
        super(Monitor, self).__init__()
        self.callbacks = []

    def add_callback(self, callback):
        try:
            self.callbacks.append(callback)
            return True
        except:
            return False

    def remove_callback(self, callback):
        try:
            self.callbacks.remove(callback)
            return True
        except:
            return False
    def start(self):
        pass

    def stop(self):
        pass