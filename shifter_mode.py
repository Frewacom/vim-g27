from evdev import ecodes as e
from g27 import EventMapper, TRIGGER_TRESHOLD

class ShifterModeMapper(EventMapper):
    def shift_neutral(self, event):
        self.send_key(e.KEY_ESC)

    def shift_1(self, event):
        if event.value == 1:
            self.send_keys([e.KEY_ESC, e.KEY_V])

    def shift_2(self, event):
        if event.value == 1:
            self.send_keys([e.KEY_ESC, (e.KEY_V, e.KEY_LEFTSHIFT)])

    def shift_3(self, event):
        if event.value == 1:
            self.send_keys([e.KEY_ESC, e.KEY_I])

    def shift_4(self, event):
        print("asd")
        if event.value == 1:
            self.send_keys([e.KEY_ESC, (e.KEY_SEMICOLON, e.KEY_LEFTSHIFT), e.KEY_W, e.KEY_ENTER])

    def shift_5(self, event):
        pass

    def shift_6(self, event):
        if event.value == 1:
            self.send_keys([e.KEY_ESC, (e.KEY_SEMICOLON, e.KEY_LEFTSHIFT), e.KEY_W, e.KEY_Q, e.KEY_ENTER])

MapperInstance = ShifterModeMapper()
