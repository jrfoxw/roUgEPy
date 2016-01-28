class Xp():
    def __init__(self):
        self.this_xp = 0

    def level_gen(self):
        self.xperience_spread = {0: 50,
                                 1: 70,
                                 2: 350,
                                 3: 700,
                                 4: 1800,
                                 5: 4200,
                                 6: 7500}

        for each in self.xperience_spread.items():
            if each[1] >= self.this_xp:
                yield each

    def xp_add(self, xp):
        self.this_xp = self.this_xp+xp
        return self.this_xp


if __name__ == '__main__':
    new = Xp()
    for x in range(20):
        b = new.level_gen()
        ask = int(input("XP:>> "))
        new.xp_add(ask)
        ret = next(b)
        print("LEVEL: {} XP: {}\{}".format(ret[0], new.this_xp, ret[1]))