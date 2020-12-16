import pyautogui
import time
m = 1
while m<100:
	time.sleep(.5)
	if m==1:
		time.sleep(5)
	if m%2==0:
		pyautogui.typewrite('HAPPY BIRTHDAY to Anika !!')
		pyautogui.press('enter')
	if m%3==0:
		pyautogui.typewrite('Many many best wishes for you.')
		pyautogui.press('enter')
	if m%5==0:
		pyautogui.typewrite('Have a happy life ahead.')
		pyautogui.press('enter')
	print('{}'.format(m))
	m = m+1