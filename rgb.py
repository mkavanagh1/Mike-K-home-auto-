import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16,GPIO.OUT)
GPIO.output(16,1)
GPIO.setup(20,GPIO.OUT)
GPIO.output(20,1)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,1)

except KeyboardInterrupt:
        GPIO.cleanup()
