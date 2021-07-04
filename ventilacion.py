import time
import RPi.GPIO as GPIO

led_pin = 37 #37 led #22 en

in1 = 18
in2 = 16

def temperatura():
	tempcpu = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
	#print("Temp.CPU = ",tempcpu)
	return int(tempcpu)

def config():
	# set GPIO mode to GPIO.BOARD
	GPIO.setmode(GPIO.BOARD)
	# set puin as input
	GPIO.setup(led_pin, GPIO.OUT)
	
	GPIO.setup(in1,GPIO.OUT)
	GPIO.setup(in2,GPIO.OUT)
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)

def programa():
	dc=50
	t_min=35
	t_max=55
	x=GPIO.PWM(led_pin,300)
	x.start(50)
	while 1:
		temp=temperatura()
		if t_min<temp<t_max:
			dc=3*temp-75   #ecuacion de mi recta de temperatura
			x.ChangeDutyCycle(dc)
			print('temperatura cpu:',temp,'duty cycle:',dc)
		elif temp<=t_min:
			dc=15	
			x.ChangeDutyCycle(dc)
			print('temp baja')
		elif t_max<=temp:
			dc=99
			x.ChangeDutyCycle(dc)
			print('temp alta')
		time.sleep(0.25)
						
def main():
	config()
	try:
		programa()
		
	except:
		raise
		
	finally:
		GPIO.cleanup()
		print('limpiando')

if __name__ == "__main__":
	# execute only if run as a script
	main()
