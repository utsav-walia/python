a=5
b=1

try:

	print("Opened the file")
	c = a/b
	print(c)
	k = int(input("Enter number: "))
	print(k)

except ZeroDivisionError as e:
	print("Zero error occured",e)

except ValueError as e:
	print("It is a value error")

except Exception as e:
	print("Unrecognized error",e)

finally:
	print("Close the file")