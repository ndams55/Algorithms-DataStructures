from typing import Any


class StaticArray:
    def __init__(self, n) -> None:
        self.data = [None] * n

    def __getattr__(self, i: int) -> int:
        if not (0 <= i < len(self.data)) : raise IndexError
        return self.data[i]
    
    def __setattr__(self,  i: int, k:int) -> None:
        if not (0 <= i < len(self.data)) : raise IndexError
        self.data[i] = k

class Array_Seq:
    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self): return self.size

    def __iter__(self): yield from self.A

    def build(self, X):
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i): return self.A[i]
    def set_at(self, i, x): self.A[i] = x

    def __copy_forward__(self, i, n, A ,j):
        for k in range(n):
            A[j + k] = self.A[i + k]
        return A
    
    def __copy_backward__(self, i, n, A, j):
        for k in range(-n, -1, -1):
            A[j + k] = self.A[i + k]
        return A
    
    def insert_at(self, i, x):
        n = self.size
        A = [None] * (n+1)
        self.__copy_forward__(0, i, A, 0)
        A[i] = x
        self.__copy_forward__(i, n - 1, A, i+1)
        self.build(A)

    def delete_at(self, i):
        n = self.size
        A = [None] * (n-1)
        self.__copy_forward__(0, i, A, 0)
        x = self.A[i]
        self.__copy_forward__(i-1, n-i-1, A, i)
        self.build(A)
        return x
    
    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): return self.delete_at(len(self) - 1)
    




