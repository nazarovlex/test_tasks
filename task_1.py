class Solution:
    def find_right_sum(self, n: int, m: int) -> list[str]:
        # Елси n>m то правильных вариантов быть не может, поэтому сразу возвращается пустой массив
        if n > m:
            return []

        # Строка из всех доступных для комбинации чисел
        possible_numbers = "".join(str(x) for x in range(1, n + 1))

        # Массив со всеми правильными результатами
        res = []
        # i проходится по номерам всех возможных комбинаций, начиная с 0
        for i in range(2 ** (len(possible_numbers) - 1)):
            # начинается комбинация всегда с 1
            combination = str(possible_numbers[0])
            # j проходится по индексам всей строки кроме '1', которая уже записана в комбо
            for j in range(1, len(possible_numbers)):
                # i преобразуется в двоичную систему и проверяется число на каждой позиции в двоичном представлении i
                # если на позиции 0, то "+" не ставится перед тем как добавить следующее число в комбо,
                # а если 1, то "+" ставится перед тем как добавить следующее число в комбо
                if (i >> (j - 1)) & 1:
                    combination += "+" + str(possible_numbers[j])
                else:
                    combination += str(possible_numbers[j])
            # обработчик исключений, который ловит ошибку когда создается комбинация, содержащая "+0[1-9]"
            # так как данная комбинация неправильная просто пропускаем ее
            try:
                if eval(combination) == m:
                    res.append(combination)
            except SyntaxError:
                continue

        # Возвращаем все правильные варианты в массиве
        return res


# Проверка правильности ввода n и m
while True:
    try:
        n, m = map(int, input().split())
        result = Solution().find_right_sum(n, m)
        if result:
            for num in result:
                print(num + "=" + str(m))
        else:
            print("Нет правильных вариантов")
    except ValueError:
        print("Введите два натуральных числа через пробел")
        continue
    break
