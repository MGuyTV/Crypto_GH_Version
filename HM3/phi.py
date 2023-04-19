from math import gcd













#m = 10, 24, 30
#https://www.quora.com/How-do-you-check-if-two-numbers-are-coprime-in-Python
#https://java2blog.com/count-down-for-loop-python/
def calculateWithOutPhi(m):#lists the number of coprimes that m has that is a number smaller than m
	f = 0#the count of coprimes between m and i
	for i in range(m, 0, -1):#counting backwards from m
		if gcd(m, i) == 1:#if the gcd between the two numbers is 1, then they are coprime
			f = f + 1
			print(str(i) + " is coprime with " + str(m))
	return f
	

def main():
	print("hello")
	m = calculateWithOutPhi(10)	
	print(str(m) + " is the number of coprimes that " + str(10) +  " has without the totient function")

	
	


if __name__ == "__main__":
	main()