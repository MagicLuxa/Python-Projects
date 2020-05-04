def findLongestSubstring(string):
	longest = 0
	output = ""
	string += string[len(string) - 1]
	for start in range(len(string) - 1):
		dict = {}
		new = ""
		for i in range(start, len(string)):
			if string[i] in dict.keys():
				if len(new) > longest:
					longest = len(new)
					output =  new
					new = ""
			
			else:
				dict[string[i]] = string[i]
				new += string[i]
	print(longest)
	print(output)


findLongestSubstring("")