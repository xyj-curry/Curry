def hanoi(cs, a="A", b="B", c="C"):
    if cs == 1:
        print(f"{a}-->{c}")
    else:
        hanoi(cs - 1, a=a, b=c, c=b)
        print(f"{a}-->{c}")
        hanoi(cs - 1, a=b, b=a, c=c)


if __name__ == "__main__":
    n = int(input("汉诺塔的层数:"))
    f = 2 ** n - 1
    if n > 20:
        raise TypeError(f"您输入的数过大,系统怕您的电脑炸掉所以报错了,不过电脑可以告诉您一共要操作{f}步")
    hanoi(n)
    print(f"一共要操作{f}步", end="")
    
