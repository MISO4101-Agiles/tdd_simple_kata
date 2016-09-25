__author__ = 'Luis_Sebastian_Talero'


class Calculator:
    def sumar(cadena):
        if not cadena:
            return 0
        else:
            nums = cadena.split(",")
            if nums.__len__() == 1:
                return int(nums[0])
            else:
                tot = 0
            for num in nums:
                tot += int(num)
            return tot
