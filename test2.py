from uiautomator import Device
import time
def protect():
	for i in range(10):
		d=Device('fa3fb4067d52')
		#d.close()
		#print (dir(d))
		el1=d(text='继续安装')
		if el1.exists:
			el1.click()
			print ('yes')
		else:
			print ('not')
		time.sleep(1)
protect()
