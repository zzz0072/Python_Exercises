#!/usr/bin/env python3

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, next_frac):
        res_num = self.num * next_frac.den + next_frac.num * self.den
        res_den = self.den * next_frac.den
        common_den = gcd(self.den, next_frac.den)

        return Fraction(res_num // common_den, res_den // common_den)

    def __sub__(self, next_frac):
        res_num = self.num * next_frac.den - next_frac.num * self.den
        res_den = self.den * next_frac.den
        common_den = gcd(self.den, next_frac.den)

        return Fraction(res_num // common_den, res_den // common_den)

    def __mul__(self, next_frac):
        new_num = self.num * next_frac.num
        new_den = self.den * next_frac.den
        common_den = gcd(new_den, new_num)
        return Fraction(new_num // common_den, new_den // common_den)

    def __truediv__(self, next_frac):
        new_num = self.num * next_frac.den
        new_den = self.den * next_frac.num
        common_den = gcd(new_den, new_num)
        return Fraction(new_num // common_den, new_den // common_den)

    def __eq__(self, cmp_frac):
        num_1 = self.num * cmp_frac.den
        num_2 = cmp_frac.num * self.den
        return num_1 == num_2

    def __lt__(self, cmp_frac):
        return self.num * cmp_frac.den < cmp_frac.num * self.den

    def __gt__(self, cmp_frac):
        return self.num * cmp_frac.den > cmp_frac.num * self.den

if __name__ == "__main__":
    myfac = Fraction(1, 4)
    print(myfac)

    myfac2 = Fraction(1, 2)

    myfac = myfac + myfac2
    print(myfac)

    myfac = myfac - myfac2
    print(myfac)

    print(str(gcd(4, 2)))

    print(myfac == myfac2)

    myfac3 = Fraction(2, 4)
    print(myfac2 == myfac3)

    print(myfac) 
    print(myfac2)
    print(myfac * myfac2)
    myfac3 = myfac / myfac2
    print(myfac / myfac2)

    print(myfac < myfac2)
    print(myfac2 < myfac)
