class Event(object):

    _event_register = {

    }

    @classmethod
    def register(cls, event, callback):
        if event in cls._event_register:
            cls._event_register[event].append(callback)
        else:
            cls._event_register[event] = [callback]

    @classmethod
    def trigger(cls, event):
        if event in cls._event_register:
            for callback in cls._event_register[event]:
                callback()
        else:
            raise ValueError("The given Event '{}' doesn't exist".format(event))


