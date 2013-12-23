#!/usr/bin/python

import RPIO, time

RPIO.cleanup()

# These are the motor output pins, A is usually the left
# motor and B is the right, 1 and 2 differentiates the pins
a1 = 7
a2 = 9
b1 = 8
b2 = 10

# Setup the 4 pins
RPIO.setup(a1, RPIO.OUT)
RPIO.setup(a2, RPIO.OUT)
RPIO.setup(b1, RPIO.OUT)
RPIO.setup(b2, RPIO.OUT)

def dirs(d1, d2, d3, d4):
	RPIO.output(a1, d1)
	RPIO.output(a2, d2)
	RPIO.output(b1, d3)
	RPIO.output(b2, d4)

# True for on, False for off. Note these work
# as a difference between the pins - TT or FF
# for a pair is off, TF is forwards and FT is
# reverse - so this is left fowards, right back
# so rotate clockwise
dirs(True, False, False, True)

# Wait for a bit
time.sleep(1)

# Turn everything off
dirs(False, False, False, False)

RPIO.cleanup()
