import pytest
from Alumettes_humain_vs_humain import victoire
from Morpion_H_vs_H import est_gagnant, Match_nul

# ---------------------------------------------------------
# TEST 1 — victoire() : ARRANGE / ACT / ASSERT
# ---------------------------------------------------------
def test_victoire_true():
    # Arrange
    val_principal = 3
    nombre = 3

    # Act
    result = victoire(val_principal, nombre)

    # Assert
    assert result is True


def test_victoire_false():
    # Arrange
    val_principal = 5
    nombre = 2

    # Act
    result = victoire(val_principal, nombre)

    # Assert
    assert result is False


# ---------------------------------------------------------
# TEST 2 — est_gagnant() : ARRANGE / ACT / ASSERT
# ---------------------------------------------------------
def test_est_gagnant_line_win():
    # Arrange
    tab = [
        "X", "X", "X",
        " ", " ", " ",
        " ", " ", " "
    ]

    # Act
    result = est_gagnant(tab)

    # Assert
    assert result == 1


def test_est_gagnant_no_win():
    # Arrange
    tab = [
        "X", "O", "X",
        "O", "X", "O",
        "O", "X", "O"
    ]

    # Act
    result = est_gagnant(tab)

    # Assert
    assert result != 1


# ---------------------------------------------------------
# TEST 3 — Match_nul() : ARRANGE / ACT / ASSERT
# ---------------------------------------------------------
def test_match_nul_true():
    # Arrange
    tab = [
        "X", "O", "X",
        "O", "X", "O",
        "O", "X", "O"
    ]

    # Act
    result = Match_nul(tab)

    # Assert
    assert result == 1


def test_match_nul_false():
    # Arrange
    tab = [
        "X", "O", " ",
        "O", "X", "O",
        "O", "X", "O"
    ]

    # Act
    result = Match_nul(tab)

    # Assert
    assert result == 0