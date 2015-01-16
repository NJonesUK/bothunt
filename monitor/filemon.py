# Notifier example from tutorial
#
# See: http://github.com/seb-m/pyinotify/wiki/Tutorial
#
import pyinotify

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events


class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, callbacks):
        self.callbacks = callbacks

    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname
        for callback in self.callbacks:
            print "calling" + str(callback)
            callback(event.pathname)

    def process_IN_DELETE(self, event):
        pass

    def process_IN_MODIFY(self, event):
        print "Modifying:", event.pathname
        for callback in self.callbacks:
            print "calling" + str(callback)
            callback(event.pathname)


class FileMonitor(object):
    def __init__(self, callbacks=[], paths=[]):
        self.wm = pyinotify.WatchManager()  # Watch Manager
        self.mask = pyinotify.ALL_EVENTS  # watched events
        self.callbacks = callbacks
        self.handler = EventHandler(self.callbacks)
        self.notifier = pyinotify.Notifier(self.wm, self.handler)
        for path in paths:
            self.wdd = self.wm.add_watch(path, self.mask, rec=True)

    def start(self):
        self.notifier.loop()

#    def stop(self):
#        self.notifier.stop()

#'/home/nick/3yp/hg/src/monitor/'

if __name__ == "__main__":
    filemon = FileMonitor(paths=["/tmp",])
