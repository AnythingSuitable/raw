#
# Follow on GitHub : https://github.com/AnythingSuitable
#

from os import system, path, geteuid
from sys import exit

print('\n[+] Installing : TorghostNG GUI\n\n')

if geteuid() != 0:
	print("Program requires Super-User Access.\nRun with 'sudo' privileges...\nExiting :/")
	exit()

print('[#] Checking for desired Files ...')

if path.exists('torghostng') == True and path.exists('torngSRC') == True:
	print('[$] Hmmm.... Seems everything Fine...')
	print('[$] Continuing Installation')

else:
	print("[!] TorghostNg/GUI Lacking some Files... Kindly Download again from GitHub.\nExitting...")
	exit()

try:
	system('sudo cp torghostng /usr/bin/')
	system('sudo cp -r torngSRC/ /usr/bin/')
	system('chmod +x /usr/bin/torghostng')

except KeyboardInterrupt:
	print()
	exit()

except Exception as e:
	print("\n[!] Something's getting wrong while installing TorghostNg-GUI...\nExitting...")
	exit()