import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(15, GPIO.OUT)

GPIO.output(15, GPIO.HIGH)
