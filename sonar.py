#!/usr/bin/python

import RPIO, time

# This was mostly taken from Scratch GPIO - https://github.com/cymplecy/scratch_gpio

def query(pin):
	RPIO.setup(pin, RPIO.OUT)
	ti = time.time()
       
	distlist = [0.0,0.0,0.0]
	ts=time.time()
        
	for k in range(3):
		RPIO.output(pin, 1)
		time.sleep(0.00001)
		RPIO.output(pin, 0)
		t0=time.time()
		RPIO.setup(pin, RPIO.IN)
           
		t1=t0
		while ((RPIO.input(pin)==0) and ((t1-t0) < 0.02)):
			t1=time.time()

		t1=time.time()
		t2=t1

		while ((RPIO.input(pin)==1) and ((t2-t1) < 0.02)):
			t2=time.time()
		t2=time.time()

		t3=(t2-t1)

		distance=t3*343/2*100
		distlist[k]=distance

		RPIO.setup(pin, RPIO.OUT)
		tf = time.time() - ts
		
		distance = sorted(distlist)[1]
        
		if (distance > 280):
			distance = 299
		if (distance < 2):
			distance = 1

	return distance

start = time.time()
print query(14)
end = time.time()
print (end-start)

RPIO.cleanup()
