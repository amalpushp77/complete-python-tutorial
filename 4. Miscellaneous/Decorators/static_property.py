class Target():
    cat = ''

    def f1(self):
        print('f1')

    @property
    def score(self):
        return Target.cat

    @staticmethod
    @score.setter
    def score(self, string):
        Target.cat = Target.cat + string
        return Target.cat


t1 = Target()
t1.score = '1'
t2 = Target()

t2.score = '2'
print(t2.cat)


