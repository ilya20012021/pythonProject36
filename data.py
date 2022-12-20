import pandas as pd
import webbrowser
import json
def get():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    u1 = set(u)
    u2 = list(u1)
    for i in u2:
        print(i)
    h = str(input("Введите название таблицы для работы:"))
    if (h in u):
        with open(f"{h}.json","r") as f:
            print(f.read())
        df = pd.read_json(f"{h}.json")
        s = int(input("Введите строку, соответствующую вашему сайту:"))
        if (0 <= s < len(df["work"])):
            if (df.at[s, "work"] != "-"):
                webbrowser.open(df.at[s, "results"])
                df.loc[s, "nums"] += 1
            else:
                print("???")
        else:
            print("Нет строки!")

        df1 = df.to_json()
        df2 = json.loads(df1)
        print(json.dumps(df2, indent=len(df2)))
        df3 = json.dumps(df2, indent=len(df2))
        with open(f"{h}.json", "a+") as f:
            f.truncate(0)
        with open(f"{h}.json", "a+") as f:
            f.write(df3)

    else:
        print("???")