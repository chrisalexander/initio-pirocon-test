initio-pirocon-test
===================

Test scripts for an Initio powered by Raspberry Pi and PiRoCon

These are test scripts, you will probably need to modify them to your setup, but they should help you get the general gist of what to do.

The scripts are:

* input.py - test various inputs using interrupts
* motor.py - test the motors are working
* reset.py - helper to reset the gpio in case something crashes
* sonar.py - test the ultrasonic distance measurement

Note to use the wheel encoders with PiRoCon you will need an unsupported configuration.

To set this up, the outline of the procedure is:

* Select the GPIO pins you are going to use. Each side has a speed and direction output, so you will need 4 in total if you want all the data. I chose speed only, as I only had 2 inputs available and you can infer direction from what command you are sending. So my GPIO pins are going to be #04 and #17, you will need to adapt these instructions if yours are different.
* Unhook the jumpers from the JP4A/B pins for the GPIO you are going to use.
* Prepare the JP6 and JP7 female terminals by separating 2 6-pin blocks of the Male-Male pins included on the basic chassis and plugging them in to these terminals.
* For the left sensor's cables, plug the RED cable on to the pin that is marked "3V3" on JP6. Plug the BLACK cable into "GND" pin on JP6. Plug the ORANGE pin (for speed) OR BROWN pin (for direction) into the JP4A/B terminal. Choose the pin on the ROW marked with your GPIO number (e.g. #04) but NOT the one next to that marking - place it on the unmarked side.
* Repeat for the right sensor cables, except the RED and BLACK cables go on the JP7 array (same markings as before) and the ORANGE or BROWN cable goes on its own respective row.
* Note this configuration will work, but that the rows on the JP3 pins corresponding to what jumpers you unhooked will cease to function.
