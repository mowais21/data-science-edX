for i in range(1,100000000000000000000000000):
    diff = (1141*(i**2) + 1)**0.5 - int((1141*(i**2) + 1)**0.5)
    if diff == 0:
        print(True)
        break