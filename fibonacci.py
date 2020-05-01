def fibonacci(n):
	if n == 0:
		return 0

	sequence = [0, 1]

	for i in range(abs(n) - 1):
		new = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
		sequence.append(new)
		sequence.pop(0)					#prevents pc from crashing with high numbers

	if n > 0:
		return (sequence[len(sequence) - 1])

	else:
		if -n % 2 == 0:
			return -(sequence[len(sequence) - 1])
		else:
			return (sequence[len(sequence) - 1])

print(fibonacci(-51))