if __name__ == "__main__":
    from BOARD import BOARD_CL
    from LED import LED_CL
    from time import sleep
    rpi = BOARD_CL()
    rled = LED_CL(rpi, 16)
    gled = LED_CL(rpi, 20)
    bled = LED_CL(rpi, 21)
    rled.ledOn()
    sleep(1)
    rled.ledOff()
    gled.ledOn()
    sleep(1)
    gled.ledOff()
    bled.ledOn()
    sleep(1)
    bled.ledOff()
