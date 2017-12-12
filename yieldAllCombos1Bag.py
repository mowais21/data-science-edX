combs = []
def yieldAllCombos(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(1)
            else:
                combo.append(0)
        yield combo

ps1 = yieldAllCombos(['ball', 'pen','orange'])

for i in iter(ps1):
    print(i)
