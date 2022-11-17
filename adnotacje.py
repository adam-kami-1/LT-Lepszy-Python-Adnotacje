"""Przykłady użycia adnotacji typu."""

import typing


def heading(title: str) -> None:
    """_summary."""
    print(50 * "#" + "\n" + title + "\n" + len(title) * "-")


#################################################
heading("Kontrola parametrów funkcji.")
"""
W wersji poniżej 3.9 zamiast list[int]) czy tuple[str, ...]
trzeba uzyć typing.List[int]) czy typing.Tuple[str, ...].
Podobnie jest z dict[key_type, value_type], w wersji poniżej 3.9
jest typing.Dict[key_type, value_type]
"""


def list_2_tuple_1(param: list[int]) -> tuple[str, ...]:
    """_summary_.

    Args:
        param: _description_
    """
    return tuple(str(elem) for elem in param)


# prm = 1, 2, 3            # prm to krotka, wykrywane przez linter.
# prm = "ABC"              # prm to string, wykrywane przez linter.
# prm = 1                  # prm to integer, wykrywane przez linter.
prm = [1, 2, 3]            # prm to lista, zgodnie z adnotacją.
print(F"{prm = !r}")
print(F"{list_2_tuple_1(prm) = !r}")


#################################################
heading("Definicja aliasu typu.")


IntList = list[int]
StrTuple = tuple[str, ...]

"""
Kiedy z powyżym są problemy to od wersji 3.10 można użyć poniższe.
Czasem lintery próbują zinterpretować definicję aliasu jako
ustawienie zmiennej.
"""

# IntList: typing.TypeAlias = list[int]
# StrTuple: typing.TypeAlias = tuple[str, ...]


def list_2_tuple_2(param: IntList) -> StrTuple:
    """_summary_.

    Args:
        param: _description_
    """
    return tuple(str(elem) for elem in param)


# prm = 1, 2, 3            # prm to krotka, wykrywane przez linter.
# prm = "ABC"              # prm to string, wykrywane przez linter.
# prm = 1                  # prm to integer, wykrywane przez linter.
prm = [1, 2, 3]            # prm to lista, zgodnie z adnotacją.
print(F"{prm = !r}")
print(F"{list_2_tuple_2(prm) = !r}")


#################################################
heading("Definicja 'nowego' typu.")

"""Bez konieczności budowy całej nowej klasy."""

UserId = typing.NewType("UserId", int)


def check_user_id(uid: UserId) -> str:
    """_summary_.

    Args:
        uid: _description_
    """
    if uid == 0:
        return "admin"
    else:
        return "regular user"


# ui = 1                    # Integer to nie UserId, wykrywane przez linter.
ui = UserId(1)

print(check_user_id(ui))
print(check_user_id(UserId(0)))


#################################################
heading("Definicja typu funkcyjnego.")


"""
Ogólna postać: typing.Callable[[typy_parametrów], typ_wyniku]

typing.Callable[..., typ_wyniku]    - dowolna lista parametrów

typing.Callable[..., typing.Any]  =  typing.Callable
"""


Callback = typing.Callable[[int, int], float]


def call_back_div(param1: int, param2: int) -> float:
    """_summary_.

    Args:
        param1: _description_
        param2: _description_

    Returns:
        _description_
    """
    return param1 / param2


def call_back_mul(param1: int, param2: int) -> float:
    """_summary_.

    Args:
        param1: _description_
        param2: _description_

    Returns:
        _description_
    """
    return param1 * param2


def caller(func: Callback, param1: int, param2: int) -> str:
    """_summary_.

    Args:
        func: _description_
        param1: _description_
        param2: _description_
    """
    return F"{func(param1, param2) = }"
    """
    Jeżeli chcesz to możesz wyświetlić bardzo szczegółowe informacje
    o callbacku
    """
    # return F"{func.__name__}({param1}, {param2}) = {func(param1, param2)}"


print(caller(call_back_div, 2, 6))
print(caller(call_back_mul, 2, 6))
# caller(print, 2, 6)     # Funkcja print zwraca None, wykrywane przez linter.


#################################################
heading("Definicja dowolnego typu: Any i None.")


def show(name: str, param: typing.Any) -> None:
    """_summary_.

    Args:
        name: _description_
        param: _description_
    """
    print(F"{name}: {type(param).__qualname__} = {repr(param)}")


a = 7
show("a", a)

b = "ABCDEF"
show("b", b)

show("<literal>", [1, 2, 3])


#################################################
heading("Unia typów.")


"""
StrOrInt = str | int

W wersji poniżej 3.10 trzeba stosować bardziej rozwlekły zapis:
"""

StrOrInt = typing.Union[str, int]


def multiply(param: StrOrInt, counter: int) -> StrOrInt:
    """_summary_.

    Args:
        param: _description_
        counter: _description_

    Returns:
        _description_
    """
    return param * (counter + 1)


print(F"{multiply(5, 3) = }")
print(F"{multiply('5', 3) = }")
"""Niezgodność typów argumentów, wykrywane przez linter."""
# print(F"{multiply(3, '5') = }")


#################################################
heading("Konkretny typ lub None.")


IntOrNone = typing.Union[int, None]

# IntOrNone = int | None                  # Tylko od wersji 3.10.

# IntOrNone = typing.Optional[int]        # To samo inaczej podane.


def check_if_none(param: IntOrNone) -> bool:
    """_summary_.

    Args:
        param: _description_

    Returns:
        _description_
    """
    if param is None:
        return True
    else:
        return False


print(F"1 - {check_if_none(1)}")
print(F"None - {check_if_none(None)}")

#################################################
heading("Lista możliwych wartości.")

Justify = typing.Literal["L", "C", "R"]


def format_text(text: str,
                size: int,
                just: Justify = "L",
                fill: str = "*") -> str:
    """_summary_."""
    if just == "L":
        jst = "<"
    elif just == "R":
        jst = ">"
    elif just == "C":
        jst = "^"
    else:
        jst = "<"
    return F"{text:{fill}{jst}{size}s}"


print("  -", format_text(" A B C ", 20))
print("L -", format_text(" A B C ", 20, "L"))
print("C -", format_text(" A B C ", 20, "C"))
print("R -", format_text(" A B C ", 20, "R"))

"""Linter wykrywa błędny argument."""
# print("J -", format_text(" A B C ", 20, "J"))


#################################################
heading("Manualne wymuszenie typu obiektu.")


"""
Na przykład, zamiast używać typing.Optional
można 'castować' None na określony typ.
"""


def my_format(param: int) -> str:
    """_summary_.

    Args:
        param: _description_

    Returns:
        _description_
    """
    if param is None:
        return "nic"
    else:
        return str(param)


print(my_format(5))
# print(my_format(None))                  # Linter wykrywa, że None to nie int.
print(my_format(typing.cast(int, None)))  # Ładny casting na właściwy typ.


#################################################
heading("Użycie typów jeszcze nie zdefiniowanych.")

"""
O ile typ będzie zdefiniowany w bieżącym module to wystarczy
zastosować w adnotacji nazwę typu jako string.

Jeśli typ jest zdefiniowany w module, którego nie możemy zaimportować
( bo na przykład nasz moduł jest importowany z tego właśnie modułu
« Czy to jest sensowny układ? » ) to jesteśmy w kropce, a nawet czterech.
Na dzisiaj nie wiem czy jest to możliwe, a jeżeli tak, to jak to zrobić.
😞☹😞☹   👎
"""


def pokazuj(objekt: 'MojaKlasa') -> None:
    """_summary_."""
    print(objekt.value)


class MojaKlasa:
    """_summary_."""

    def __init__(self, value: int):
        """_summary_."""
        self.value = value

    def skopiuj(self, inny: 'MojaKlasa') -> None:
        """_summary_."""
        self.value = inny.value


print("Tworzymy dwa obiekty:")
ob1 = MojaKlasa(9)
ob2 = MojaKlasa(21)

pokazuj(ob1)
pokazuj(ob2)

print("Kopiujemy drugi do pierwszego:")
ob1.skopiuj(ob2)

pokazuj(ob1)
pokazuj(ob2)


#################################################
heading("'Droga, z której się nie wraca'")


# def koniec() -> None:
def koniec() -> typing.NoReturn:
    """_summary_."""
    print("Kończymy pracę")
    quit()
    print("Może tu jeszcze uda się coś wydrukować")


koniec()
print("To może chociaż tutaj uda się coś wydrukować")
