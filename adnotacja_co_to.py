"""Co może być adnotacją?"""


def funkcja7(par1: 2 * 3,
             par2: open,  # type: ignore
             par3: print('Niepotrzebny parametr') = None
             ) -> "Funkcja zwraca co może":
    """_summary_."""
    if par2 is None:
        return
    else:
        return par1 + par2


print(F"{funkcja7(1, 2) = }")
print(F"{funkcja7('1', '2') = }")
print(F"{funkcja7(1, 2.0) = }")
