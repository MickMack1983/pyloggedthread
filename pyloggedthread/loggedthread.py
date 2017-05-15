from threading import Thread
import logging
import traceback


class LoggedThread:
    def __init__(self, group=None, target=None, name=None, log=None, *args, **kwargs):
        self.__target = target
        self.log = log if log else None
        self.t = Thread(group=group, target=self.wrapper, name=name, *args, **kwargs)

    def start(self):
        self.t.start()
        if not self.log:
            self.log = logging.getLogger("LoggedThread-" + str(self.t.ident))
        self.log.debug("started")

    def wrapper(self, *args, **kwargs):
        # noinspection PyBroadException
        try:
            self.__target(*args, **kwargs)
        except:
            if not self.log:
                self.log = logging.getLogger("LoggedThread-" + str(self.t.ident))
            self.log.error(traceback.format_exc())
        finally:
            if not self.log:
                self.log = logging.getLogger("LoggedThread-" + str(self.t.ident))
            self.log.debug("terminated")
