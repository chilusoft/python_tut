import math, time, subprocess


def bar(num):

	t1 = time.time()

	for x in range(0, num):
		print('initailising progress bar...')
		print(str(x) + '/' + str(num) + '| ' + '='*x + '=> ' + str(math.floor(x/num*100)) + '% done...')
		time.sleep(0.4)
		subprocess.call('clear', shell=True) #unix

		if x == num -1:
			print(str(num) + '/'+ str(num) + '='*num + ' 100% done!!!')
			print('loop ran for ' + str(math.floor(time.time() -t1)) + 'seconds ....')

n = int(input('enter the range for the progress bar'))

bar(n)
