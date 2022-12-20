import matplotlib.pyplot as plt
import pandas as pd
def draw():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    u1 = set(u)
    u2 = list(u1)
    for i in u2:
        print(i)
    h = str(input("Введите название таблицы для работы:"))
    if (h in u):
        df = pd.read_json(f"{h}.json")
        col = list(df["nums"])
        col1 = list(df["results"])
        plt.pie(col,labels=col1)
        plt.show()
    else:
        print("???")