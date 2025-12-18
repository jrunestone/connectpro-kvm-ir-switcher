# connectpro-kvm-ir-switcher
## What
Tiny python HTTP server that will emit a compatible IR pulse to switch the devices on a ConnectPro KVM using `ir-ctl`.

Handy if you don't have the remote.

## Compatible KVM devices
Tested on the ConnectPro UDP2-14AP.

## How
I use this on a Raspberry Pi 3b+ with just a 30mA IR diode directly shoved into a GPIO and GND. No resistors or transistor. You might want to check out "correct" circuits.

## Setup and run
1. Add the following line to your Pi:s `/boot/firmware/config.txt`: `dtoverlay=gpio-ir-tx,gpio_pin=17`.
2. Connect an IR diode to your chosen GPIO. Again, look up IR circuits.
3. Verify it works by calling `ir-ctl -S nec:866b02fd` (select device 1).
3. Start the server by `python kvm-server.py`.
4. Make a request to `http://<ip>:5000/1` etc.

## Arduino
If you're porting this to Arduino you can use the [Arduino-IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote) library and send the codes like this:

```
// code to switch to device 1
uint8_t buffer[4] = {0x86, 0x6B, 0x05, 0xFA};
IrSender.sendPulseDistanceWidthFromArray(&NECProtocolConstants, (IRRawDataType*)buffer, 8 * sizeof(buffer)/sizeof(buffer[0]), 0);
```

## References
See all compatible codes in `CODES.md`.