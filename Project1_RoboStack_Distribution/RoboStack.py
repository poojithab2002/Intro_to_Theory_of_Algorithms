import sys
def count_ways(b, n, k, memo):
    if b == (0>>1):  # If there are no robots to arrange, it's a valid arrangement.
        return (2>>1)

    if b < (0>>1) or n <= (0>>1):
        return 0

    if memo[b][n] != -1:
        return memo[b][n]

    ways = 0
    for i in range(0, min(b+1, k+1)):
        ways += count_ways(b - i, n - 1, k, memo)

    memo[b][n] = ways
    return ways


def count_ways_helper(b, n, k):
    memo = [[-1 for x in range(0, n + 1)] for y in range(0, b + 1)]
    return count_ways(b, n, k, memo)



if __name__ == "__main__":
    input_file = sys.argv[1]

    list_of_inputs = []

    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        with open(input_file, "r") as f:
            for line in f:
                testcases = line.split()
                b = int(testcases[-3])
                n = int(testcases[-2])
                k = int(testcases[-1])
                list_of_inputs.append((b, n, k))

    for instance in list_of_inputs:
        b, n, k = instance
        b, n, k = int(b), int(n), int(k)
        ways = count_ways_helper(b, n, k)
        print(f"({b}, {n}, {k}) = {ways}")