#!/usr/bin/python

import RPIO

RPIO.cleanup()

# This function will be called whenever the value of the pin changes
def gpio_callback(gpio_id, value):
	print "Callback %i %s" % (gpio_id, value)

# Set up interrupts for a specific pin
def interrupt(pin):
	RPIO.setup(pin, RPIO.IN)
	RPIO.add_interrupt_callback(pin, gpio_callback)

# These are the common input pins on the PiRoCon
# Note these are the # numbers as noted on the board, 
# so 4 is the input marked "#04" on the silkscreen.
# Use hashes to comment/uncomment these lines, then
# trigger the inputs to see the values change - e.g.
# wave your hands in front of the IR sensors, spin the
# wheels (gently) etc.
interrupt(4);
#interrupt(14);
interrupt(17);
#interrupt(18);
#interrupt(27);
#interrupt(22);
#interrupt(23);

# This loops round infinitely - ctrl+C the script to exit this routine
RPIO.wait_for_interrupts()

# Clean up any opened GPIO for other programs
RPIO.cleanup()
