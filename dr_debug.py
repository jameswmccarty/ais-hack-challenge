"""
Defeating Dr. D. Bugg

Solved 29 time(s)

Scrambled, just in case.

Dr. D Bugg has unleashed a doomsday robot to wreak havoc upon the world! But because he is so overly confident in his evil capabilities, he has given away two things: the command to stop the robot, and the software that transmits commands to the robot. Though he has tricked us all, because he did not mention that the capitalization of the command was important! Fortunately, Dr. Bugg is known to have some particularly strange coding habits. It's up to you to figure out the real deactivation code. Good luck!
command-transmitter.so
MD5: c9b630d15dcacd9e26d651437d973702
SHA256: 070b573adee5d473d65db96c04bad...

Enter command that gives "quietrobotplease" after scrambling.

My evil plan is finally complete! My robot will destroy everything! I gave out the command for deactivation, as well as the command transmitter, but the transmitter will change any commands to be shouted at the robot! And the robot ignores any commands that are shouted at it, because it only accepts commands from polite people! I left in 2 working command capitalization combinations so that I may deactivate the robot at some point, but nobody will ever figure either of them out! Mwahahahahaha!
Note to self (the handsome Dr. Dastardly): remember not to compile the command transmitter in debug mode when you give it away, or else your variable names will be on full display! And fix that bad habit of using strings as documentation!
D Bugg Documentation: The scrambling is based on the formula: (n*13+7)mod16=result. The numbers 13 and 7 are crucial, so make sure nobody finds them out!
D Bugg Documentation: Do not let users try to trick the system! Away with all wrong-length commands!
D Bugg Documentation: This pays attention to both the value of a character and its capitalization. Twice the influences means twice the confusion! Very secure!

"""

def dfs(s,g,built=''):
	if len(built) == len(g) and transmit(built) == g:
		print(built)
	elif len(s) > 0:
		dfs(s[1:],g,built+s[0].lower())
		dfs(s[1:],g,built+s[0].upper())

def transmit(cmd):
	out = ''
	for n in range(16):
		idx = (n*13+7) % 16
		current = cmd[n]
		if ord(cmd[idx]) % 2 == 0:
			current = current.swapcase()
		if cmd[idx].isupper():
			current = current.swapcase()
		out += current
	return out

dfs("quietrobotplease","quietrobotplease")

