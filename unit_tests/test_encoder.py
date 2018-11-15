import pytest
from encoder import GeneEncoder

@pytest.mark.parametrize("test_input,expected", [
    (3.776, "110111100110010"),
    (-3.776, "001000011001101"),
    (-5.12, "000000000000000"),
    (5.12, "111111111111111"),
    (0, "100000000000000")
])
def test_real_to_binary(test_input, expected):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    assert(gene_encoder.real_to_binary(test_input) == expected)

@pytest.mark.parametrize("test_input,expected", [
    ("110111100110010", 3.776),
    ("001000011001101", -3.776),
    ("000000000000000", -5.12),
    ("111111111111111", 5.12),
    ("100000000000000", 0.0)
])
def test_binary_to_real(test_input, expected):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    assert(gene_encoder.binary_to_real(test_input) == expected)

@pytest.mark.parametrize("test_input,expected", [
    ("110111100110010", "101100010101011"),
    ("001000011001101", "001100010101011"),
    ("000000000000000", "000000000000000"),
    ("111111111111111", "100000000000000"),
    ("100000000000000", "110000000000000")
])
def test_binary_to_gray(test_input, expected):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    assert(gene_encoder.binary_to_gray(test_input) == expected)

@pytest.mark.parametrize("test_input,expected", [
    ("101100010101011", "110111100110010"),
    ("001100010101011", "001000011001101"),
    ("000000000000000", "000000000000000"),
    ("100000000000000", "111111111111111"),
    ("110000000000000", "100000000000000")
])
def test_gray_to_binary(test_input, expected):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    assert(gene_encoder.gray_to_binary(test_input) == expected)

@pytest.mark.parametrize("test_input,expected", [
    (3.776, "101100010101011"),
    (-3.776, "001100010101011"),
    (-5.12, "000000000000000"),
    (5.12, "100000000000000"),
    (0, "110000000000000")
])
def test_real_to_gray(test_input, expected):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    assert(gene_encoder.real_to_gray(test_input) == expected)

@pytest.mark.parametrize("test_input,expected", [
    (3.776, "101100010101011"),
    (-3.776, "001100010101011"),
    (-5.12, "000000000000000"),
    (5.12, "100000000000000"),
    (0, "110000000000000")
])
def test_real_to_gray(test_input, expected):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    assert(gene_encoder.real_to_gray(test_input) == expected)

@pytest.mark.parametrize("test_input,expected", [
    ("101100010101011", 3.776),
    ("001100010101011", -3.776),
    ("000000000000000", -5.12),
    ("100000000000000", 5.12),
    ("110000000000000", 0.0)
])
def test_gray_to_real(test_input, expected):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    assert(gene_encoder.gray_to_real(test_input) == expected)

@pytest.mark.parametrize("test_input", [6,-6])
def test_real_to_binary_assertion(test_input):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    with pytest.raises(AssertionError):
        gene_encoder.real_to_binary(test_input)

@pytest.mark.parametrize("test_input", ["101100010101011111", "0", ""])
def test_binary_to_real_assertion(test_input):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    with pytest.raises(AssertionError):
        gene_encoder.binary_to_real(test_input)

@pytest.mark.parametrize("test_input", ["101100010101011111", "0", ""])
def test_binary_to_gray_assertion(test_input):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    with pytest.raises(AssertionError):
        gene_encoder.binary_to_gray(test_input)

@pytest.mark.parametrize("test_input", ["101100010101011111", "0", ""])
def test_gray_to_binary_assertion(test_input):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    with pytest.raises(AssertionError):
        gene_encoder.gray_to_binary(test_input)

@pytest.mark.parametrize("test_input", [6,-6])
def test_real_to_gray_assertion(test_input):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    with pytest.raises(AssertionError):
        gene_encoder.real_to_gray(test_input)

@pytest.mark.parametrize("test_input", ["101100010101011111", "0", ""])
def test_gray_to_real_assertion(test_input):
    gene_encoder = GeneEncoder(-5.12, 5.12, 15, 3)
    with pytest.raises(AssertionError):
        gene_encoder.gray_to_real(test_input)
