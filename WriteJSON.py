import json
import serial
import time



def main():
	name = 1
	dict = {}
	s = serial.Serial('/dev/ttyACM2', 9600)
	time.sleep(2)
	for var in range(10):
		str = s.readline()
		dict[name] = int(str)
		name += 1
	
	f = open('s.json', 'w')
	json.dump(dict, f, indent=4, sort_keys=True)
	f.close()

if __name__=='__main__':
	main()		

