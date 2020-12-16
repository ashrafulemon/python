import pyautogui
import time
i=300
while i<310:
	time.sleep(1)
	if i==300:
		time.sleep(3)
	pyautogui.typewrite('{}'.format(i))
	pyautogui.press('enter')
	pyautogui.hotkey('ctrl','a')
	#pyautogui.press('del')
	i=i+1