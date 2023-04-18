class Solution():
    def find_right_sum(self, n, m):
        # In correct answer n can't be bigger then m
        if n > m:
            return []

        # Array of possible numbers in combination
        possible_numbers = [x for x in range(1, n + 1)]

        # Result array
        res = []

        for i in range(1, len(possible_numbers)):
            for j in range(i + 1, len(possible_numbers) + 1):
                # first number
                start = "".join(str(possible_numbers[x]) for x in range(0, i))
                # middle slice with "+" between numbers
                middle = "+".join(str(possible_numbers[x]) for x in range(i, j))
                # the last number
                end = "".join(str(possible_numbers[x]) for x in range(j, n))

                # Combination of numbers
                combination = start + '+' + middle + end

                # If sum of combination == m , write down it  to res
                if eval(combination) == m:
                    res.append(combination)
        # Return correct results
        return res


# Check correct input
while True:
    try:
        n, m = map(int, input().split())
        result = Solution().find_right_sum(n, m)
        if result:
            for num in result:
                print(num + "=" + str(m))
        else:
            print("None")
    except ValueError:
        print("Enter two integers separated by a space")
        continue
    break

