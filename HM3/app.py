import math

#Number 1: 198 and 243
#Number 2: 1819 and 3587




def find_gcd(num1, num2):
	answer = 0
	#quotient = math.floor(num1 / num2)
	if num1 != 0 and num2 == 0:#Base case
		return num1
	remainder = num1 % num2
	answer = find_gcd(num2, remainder)
	return answer



def main():
	answer = find_gcd(198, 243)
	print(answer)

if __name__ == "__main__":
	main()