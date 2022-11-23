from evdev import ecodes as e
from g27 import EventMapper, TRIGGER_TRESHOLD

class PedalModeMapper(EventMapper):
    def clutch(self, event):
        if event.value < TRIGGER_TRESHOLD:
            self.send_key(e.KEY_ESC)

    def brake(self, event):
        pass

    def throttle(self, event):
        if event.value < TRIGGER_TRESHOLD:
            self.send_key(e.KEY_I)

    def shift_3(self, event):
        if event.value == 1:
            self.send_key(e.KEY_V)

    def shift_4(self, event):
        if event.value == 1:
            self.send_key(e.KEY_V, e.KEY_LEFTSHIFT)

MapperInstance = PedalModeMapper()
