from debounce import debounce
from evdev import uinput, ecodes as e

RESOLUTION = 255
TRIGGER_TRESHOLD = 0.8 * RESOLUTION

class EventMapper:
    def __init__(self):
        self.ui = uinput.UInput()
        self.handlers = {
            1: self.clutch,
            2: self.throttle,
            4: self.shift_neutral,
            5: self.brake,
            300: self.shift_1,
            301: self.shift_2,
            302: self.shift_3,
            303: self.shift_4,
            704: self.shift_5,
            705: self.shift_6,
        }

    def send_key_raw(self, key, mod=None):
        try:
            if mod:
                self.ui.write(e.EV_KEY, mod, 1)
            self.ui.write(e.EV_KEY, key, 1)
            self.ui.write(e.EV_KEY, key, 0)
            if mod:
                self.ui.write(e.EV_KEY, mod, 0)
            self.ui.syn()
        except Exception as ex:
            print("Could not send key", ex)
            return

    @debounce(0.1)
    def send_keys(self, keys):
        for key in keys:
            if type(key) is tuple:
                (k, mod) = key
                self.send_key_raw(k, mod)
            else:
                self.send_key_raw(key)

    @debounce(0.1)
    def send_key(self, key, mod=None):
        self.send_key_raw(key, mod)

    def clutch(self, event):
        pass

    def brake(self, event):
        pass

    def throttle(self, event):
        pass

    def shift_neutral(self, event):
        pass

    def shift_1(self, event):
        pass

    def shift_2(self, event):
        pass

    def shift_3(self, event):
        pass

    def shift_4(self, event):
        pass

    def shift_5(self, event):
        pass

    def shift_6(self, event):
        pass

    def call_handler(self, event):
        handler = self.handlers.get(event.code)
        if handler:
            handler(event)
        else:
            print("Unhandled event", event)
