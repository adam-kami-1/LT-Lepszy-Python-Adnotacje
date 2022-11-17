"""Przykłady pokazujące efekty braku i użycia adnotacji typu."""


def funkcja1(par1, par2):
    """Funkcja bez adnotacji."""
    if par2 is None:
        return
    else:
        return par1 + par2


print(F"{funkcja1(1, 2)=}")
print(F"{funkcja1('1', '2') = }")
print(F"{funkcja1(1, 2.0) = }")
print(F"{funkcja1(1, '2.0')}")


# def funkcja2(par1: int, par2: int):
#     """Oba parametry typu int."""
#     if par2 is None:
#         return
#     else:
#         return par1 + par2


# print(F"{funkcja2(1, 2) = }")
# print(F"{funkcja2('1', '2') = }")
# print(F"{funkcja2(1, 2.0) = }")
# print(F"{funkcja2(1, '2.0')}")


# def funkcja3(par1: float, par2: float):
#     """Oba parametry typu float."""
#     if par2 is None:
#         return
#     else:
#         return par1 + par2


# print(F"{funkcja3(1, 2) = }")
# print(F"{funkcja3('1', '2') = }")
# print(F"{funkcja3(1, 2.0) = }")
# print(F"{funkcja3(1, '2.0')}")


# def funkcja4(par1: str, par2: str):
#     """Oba parametry typu str."""
#     if par2 is None:
#         return
#     else:
#         return par1 + par2


# print(F"{funkcja4(1, 2) = }")
# print(F"{funkcja4('1', '2') = }")
# print(F"{funkcja4(1, 2.0) = }")
# print(F"{funkcja4(1, '2.0')}")


# def funkcja5(par1: int, par2: int) -> int:
#     """Oba parametry typu int, funkcja zwraca int."""
#     if par2 is None:
#         return
#     else:
#         return par1 + par2


# print(F"{funkcja5(1, 2) = }")
# print(F"{funkcja5('1', '2') = }")
# print(F"{funkcja5(1, 2.0) = }")
# print(F"{funkcja5(1, '2.0')}")


# def funkcja6(par1: int, par2: int = 0) -> int:
#     """Oba parametry typu int, drugi ma wartość domyślną, funkcja zwraca int."""
#     if par2 is None:
#         return
#     else:
#         return par1 + par2


# print(F"{funkcja6(1, 2) = }")
# print(F"{funkcja6('1', '2') = }")
# print(F"{funkcja6(1, 2.0) = }")
# print(F"{funkcja6(1, '2.0')}")
