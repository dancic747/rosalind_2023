#BA5a
'''Find the Minimum Number of Coins Needed to Make Change'''

def dpChange(money,coins):
    minNumCoins=(money+1)*[0]
    for m in range(1,money+1):
        minNumCoins[m]=money+1
        for i in range(1,len(coins)):
            if m>=int(coins[i]):
                if minNumCoins[m-int(coins[i])]+1<minNumCoins[m]:
                    minNumCoins[m]=minNumCoins[m-int(coins[i])]+1
    return minNumCoins[money]


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba5a.txt", "r") as f:
        money=int(f.readline().strip())
        coins=f.readline().split(',')

    res=dpChange(money,coins)
    print(res)