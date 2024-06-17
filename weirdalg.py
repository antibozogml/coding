x = int(input())
def EvenOrNot(x):
    if (x%2 == 0):
        return "Even"
    else:
        return "589632147"
WeirdAlgorithmList = [x]
while (x >= 2):
    if (EvenOrNot(x) == "Even"):
        x = int(x / 2)
        WeirdAlgorithmList.append(x)
    else:
        x = 3 * x + 1
        WeirdAlgorithmList.append(x)
i = 0
while (i < len(WeirdAlgorithmList)):
    print (str(WeirdAlgorithmList[i]))
    i += 1