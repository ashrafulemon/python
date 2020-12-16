import pyautogui
import time
m = 987
while m<=1000:
	time.sleep(2.5)
	pyautogui.typewrite('Comment Number {} !!!'.format(m))
	pyautogui.press('enter')
	print('{}'.format(m))
	m = m+1