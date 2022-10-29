# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import  defaultdict
class Node:
    def __init__(self):
        self.lista= defaultdict(list)
        self.d = set()

    def connect(self,a,b):
        self.lista[a].append(b)
        self.lista[b].append(a)

    def print(self):
        print(self.lista)

    def DFS(self,n):
        print(n)

        self.d.add(n)
        a=self.lista[n]
        for i in a:
            if i not in self.d:
                self.DFS(i)
            else:
                print("loop found ")
                return




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = Node()
    n.connect(1,2)
    n.connect(3,4)
    n.connect(1,3)
    n.connect(2,4)
    n.connect(3,5)
    n.connect(2,6)
    n.print()
    n.DFS(1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
