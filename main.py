import sys
import evdev
import time
import pedal_mode as pedal_mode
import shifter_mode as shifter_mode

MODES = {
    'pedals': pedal_mode.MapperInstance,
    'shifter': shifter_mode.MapperInstance,
}

def find_wheel_event_file():
    """
    Finds the /dev/input/event<id> path for the G27 wheel.

    :returns: Path to the wheel event file
    """
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    for device in devices:
        if "G27 Racing Wheel" in device.name:
            return device.path

if __name__ == "__main__":
    mode = MODES['shifter']
    if len(sys.argv) > 1:
        mode = MODES.get(sys.argv[1], MODES['shifter'])

    event_file = find_wheel_event_file()
    try:
        device = evdev.InputDevice(event_file)
    except Exception as e:
        print(f"Failed to open device at {event_file}: {e}")
        exit(1)

    print("Reading events from device: ", device.path)
    for event in device.read_loop():
        if event.code == 0:
            continue

        mode.call_handler(event)
