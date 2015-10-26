import RPi.GPIO as GPIO
PIN_A_USAR=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_A_USAR, GPIO.IN)

while True:
  input_value = GPIO.input(PIN_A_USAR)
  if input_value == False:
    print("The button has been pressed.")
    while input_value == False:
      input_value = GPIO.input(PIN_A_USAR)

