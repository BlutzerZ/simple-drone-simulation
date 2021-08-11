'''
┏━┳┓╋╋╋╋╋╋╋╋╋╋ ┏┓╋╋╋╋╋╋╋╋╋ ┏━┳┓╋╋╋╋╋╋╋╋╋┏┓┏┓
┃━╋╋━━┳━┳┓┏━┓ ┏┛┣┳┳━┳━┳┳━┓ ┃━╋╋━━┳┳┳┓┏━┓┃┗╋╋━┳━┳┓
┣━┃┃┃┃┃╋┃┗┫┻┫ ┃╋┃┏┫╋┃┃┃┃┻┫ ┣━┃┃┃┃┃┃┃┗┫╋┗┫┏┫┃╋┃┃┃┃
┗━┻┻┻┻┫┏┻━┻━┛ ┗━┻┛┗━┻┻━┻━┛ ┗━┻┻┻┻┻━┻━┻━━┻━┻┻━┻┻━┛
╋╋╋╋╋╋┗┛

Made by: BlutzerZ

Features:
	- Using Thread to simulate battery
	- Simulation loc of drone with simple (X, Z)


GITHUB: https://github.com/BlutzerZ/simple-drone-simulation/
'''

from threading import Thread
import time, sys

def battery():
	i = 100
	global battery_status
	for x in range(i):
		i -= 1
		battery_status = i
		time.sleep(0.1)

		if battery_status == 0:
			print("\nbattery empty")
			time.sleep(1)
			print("turning off...")
			time.sleep(3)
			print("press ENTER to exit")
			sys.exit()

def command(command):
	global x
	global y
	global fly
	global batt

	if str(command) == "fly":
		if fly == False:
			fly = True
			batt = Thread(target = battery)
			batt.start()
			print('\n[>] flying your drone..')
			time.sleep(2)
			print('[>] Your drone now fly')
			time.sleep(1)
			print('[>] Now you can control with entering command')
			print('[>] Command to move [forward/backward/left/right]')
			time.sleep(1)
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			return
		else:
			print('\n[!] Your Drone already fly')
			time.sleep(1)
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			return

	elif str(command) == "battery":
		if fly == True:
			print("\n[>] Remaining battery = "+ str(battery_status) +"%")
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			return
		else:
			print("\n[>] Remaining battery = 100%")
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			return

	elif str(command) == "help":
		print("\n==[HELP]==")
		print("'fly' | to fly your drone")
		print("'forward' | to fly your drone forward")
		print("'backward' | to fly your drone backward")
		print("'left' | to fly your drone left")
		print("'right' | to fly your drone rigt")
		print("'battery' | to check your battery percentage")
		print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
		return

	elif fly == True:
		if str(command) == "left":
			print("\n[>] Turning left...")
			time.sleep(1)
			x -=1
			print("[*] Loc = ("+str(x)+","+str(y)+")")
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			return

		elif str(command) == "right":
			print("\n[>] Turing right...")
			time.sleep(1)
			x +=1
			print("[*] Loc = ("+str(x)+","+str(y)+")")
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			return

		elif str(command) == "forward":
			print("\n[>] Turning forward...")
			time.sleep(1)
			y += 1
			print("[*] Loc = ("+str(x)+","+str(y)+")")
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			return

		elif str(command) == "backward":
			print("\n[>] Turing backward...")
			time.sleep(1)
			y -= 1
			print("[*] Loc = ("+str(x)+","+str(y)+")")
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			return

		else:
			print("\n[!] Wrong command, Please re-entering command")
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			return

	else:
		print("\n[!] Wrong command or your drone aren't fly")
		print("[!] Please re-entering command or fly your drone")
		print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
		return

def main():
	global x
	global y
	global fly
	global batt

	batt = 'idle'
	x = 0
	y = 0
	print("This is drone, enter fly to fly your drone")
	print("type 'help' to show all command")
	fly = False
	while True:
		inputcommand = input("[COMMAND] = ") 
		if batt == 'idle' or batt.is_alive() == True:
			command(inputcommand)
		else:
			sys.exit()

if __name__ == '__main__':
	main()
