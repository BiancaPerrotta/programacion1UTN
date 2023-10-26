import pytest
from funciones import*
@pytest.mark.parametrize("a,res")[
(100,1),
(123,6),
(14,5)
]
def test_add_diggit(a,res):
    assert test_add_diggit(a)==res