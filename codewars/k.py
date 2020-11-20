# https://www.codewars.com/kata/51fda2d95d6efda45e00004e


class User:
    n = 0
    rank1 = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
    rank = rank1[n]
    progress = 0
    def inc_progress(self, rank):
        rankk = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        '''
        Error point: Must check first if the given rank is valid
        '''
        if rank in rankk:
            if rank == self.rank:
                self.progress += 3

            elif rank == self.rank1[self.n-1]:
                self.progress += 1

            elif rank > self.rank:
                '''Error point :
                Should have considered absolute value of self.n
                '''
                d = self.rank1.index(rank)-abs(self.n)
                self.progress += (10*d*d)

            if self.rank != 8:
                if self.progress >= 100:
                    self.n += (self.progress//100)
                    self.rank = self.rank1[self.n]
                    self.progress -= (self.progress//100)*100

            if self.rank == 8:
                self.progress = 0
        else:
            raise ValueError
