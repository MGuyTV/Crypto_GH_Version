import time









def findInverse(num):
	return 0


#After 5 minutes this is the number: 1932672011
#After 1 hour, this is the number: 21227158564
def doNothing(minutes):
	start = time.time()
	i = 0
	while True:
		potentialEnd = time.time() - start
		if(potentialEnd >= minutes * 60):# Times 60 to convert it to minutes
			break
		i = i + 1
	
	return i




def main():
	#findInverse()
	digits = doNothing(60)#First 5 minutes,then 60 minutes or 1 hour
	print(digits)

if __name__ == "__main__":
	main()