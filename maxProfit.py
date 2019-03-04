class Sol:
    def maxProf(self,prices):
        prof=[]
        for i in range(len(prices)):
            if i==0:
                prof.append(0)
            else:
                prof.append(max(prices[i]-min(prices[0:i]),0))
        print(max(prof))
if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    p1=Sol()
    p1.maxProf(prices)
