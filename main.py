from googlesearch import search
import pandas as pd
import requests
import json

import data

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
        df1 = df.to_json()
        df2 = json.loads(df1)
        print(json.dumps(df2,indent=len(df2)))
        df3 = json.dumps(df2,indent=len(df2))
        name = str(input("Введите имя таблицы:"))
        with open("1.txt", "a+") as f:
            f.write(f'{name}\n')
        with open(f"{name}.json", "a+") as f:
            f.write(df3)
    dir = ["Получить доступ к таблицам(нажмите 1)","Нарисовать гистограмму(нажмите 2)"]
    dir1 = ",".join(dir)
    r = str(input("Введите ответ:"))
    if(r == "1"):
        data.get()
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
