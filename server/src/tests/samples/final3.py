# This sample tests the "Final" type annotation
# introduced in Python 3.8.

import typing
from typing import Final

foo1: typing.Final = 3

must_be_int: int = foo1

# This should generate an error because
# reassignment of a Final variable should
# not be allowed.
foo1 = 4

# This should generate an error because there
# is a previous Final declaration.
foo1: Final[int]

# This should generate an error because
# the type doesn't match.
foo2: Final[str] = 3

# This should generate an error because
# we expect only one type argument for Final.
foo3: Final[str, int] = 'hello'

class Foo:
    member1: Final = 4
    
    # This should generate an error because only
    # one declaration can have a Final attribute.
    member1: Final

    member2: typing.Final[int] = 3

    member4: Final[int]

    # This should generate an error because there is
    # no assignment.
    member5: Final[str]

    member6: Final[int]

    def __init__(self):
        # This should generate an error because a Final
        # member outside of a stub file or a class body
        # must have an initializer.
        self.member3: Final

        # This should generate an error because this symbol
        # already has a final declaration.
        self.member2: Final[int]

        self.member4 = 5

        # This should generate an error because only one
        # assignment is allowed.
        self.member4 = 6

    def another_method(self):
        # This should generate an error because assignments
        # can occur only within class bodies or __init__ methods.
        self.member6 = 4


class Bar(Foo):
    # This should generate an error because we are overriding
    # a member that is marked Final in the parent class.
    member1 = 5

    def __init__(self):
        # This should generate an error because we are overriding
        # a member that is marked Final in the parent class.
        self.member6 = 5
    

