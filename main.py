from googlesearch import search
import pandas as pd
import requests
from tabulate import tabulate
import webbrowser


n = 1


while(n != 0):
    print("Вас приветствует Автоматизированная информационно-аналитическая система google search")
    a = ["да", "нет"]
    b = "/".join(a)
    print(f"Новый запрос?{b}")
    ans = str(input())
    if(ans == a[0]):
        theme = str(input("Введите тему запроса:"))
        count = int(input("Введите кол-во ссылок:"))
        res1 = search(theme, stop=count)
        res = list(res1)
        id = [int(i) for i in range(len(res))]
        work = []
        nums = [0 for i in range(len(res))]
        for i in res:
            try:
                r = requests.get(i)
                work.append("+")
            except requests.exceptions.ConnectionError:
                work.append("-")
            except requests.exceptions.ReadTimeout:
                work.append("-")
        df = pd.DataFrame({})
        df["id"] = id
        df["results"] = res
        df["work"] = work
        df["nums"] = nums
        print(tabulate(df,headers = "keys",tablefmt = "psql"))
        ans = ["да", "нет"]
        ans_n = "/".join(ans)
        print(f"Хотите ли вы перейти на один из работающих сайтов?{ans_n}")
        s = str(input("Введите ответ:"))
        if (s == ans[0]):
            s = int(input("Введите строку, соответствующую вашему сайту:"))
            if(0 <= s < len(res)):
                if (df.at[s, "work"] != "-"):
                    webbrowser.open(df.at[s, "results"])
                else:
                    print("???")
            else:
                print("Нет строки!")

        else:
            print("OK")

    else:
        print("OK")
    ans = ["да", "нет"]
    ans_n = "/".join(ans)
    print(f"Хотите ли вы продолжить работу с данным ПО?{ans_n}")
    s = str(input("Введите ответ:"))
    if (s == ans[0]):
        n += 1
    elif (s == ans[1]):
        break
    else:
        print("Ничего непонятно")
