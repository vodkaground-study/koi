def main():
	n = int(input())
	arr = [int(input()) for i in range(n)]

	maxv, dap = -1, 0

	for v in arr[::-1]:
		if v > maxv:
			maxv = v
			dap += 1

	print(dap)

main()