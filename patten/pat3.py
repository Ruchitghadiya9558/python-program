
# 		  *    = 4   i = 1  6-1 = 5
# 	    * *   = 3   i = 2  6-2 = 4
#     * * *  = 2   i = 3  6-3 = 3
#   * * * *  = 1   i = 4  6-4 = 2
# * * * * *  = 0   i = 5  6-5 = 1

for i in range(1, 6):
	#space
	for k in range(1, 6-i):
		print(" ", end="")

	for j in range(1, i+1):
		print("*", end="")

	print("")

print("------------------------------------")

#        *
#		* *
#      * * *
#     * * * *
#	 * * * * *

for i in range (1,6):
	# space
	for k in range(1,6-i):
		print(" ",end="")

	for j in range (1,i+1):
		print("* ",end="")
	print("")


