import pytest
import numpy as np
from main import normalize_ref, normalize_vec


# Using pytest, write test functions that call both versions on the same input and assert they agree — use np.allclose for the comparison, not ==, and explain in a comment why. Cover: a normal case (e.g. [1,2,3,4,5]), an empty input [], a boundary case (a single element, and an array where every value is identical — which makes max-min zero), an aliasing case (pass the same array object in twice and confirm neither function mutates the original), and a non-finite case (an input containing nan or inf)

def test_normal_case():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    arr = np.array(data)
    # We use np.allclose to compare because floating point arithmetic can introduce small rounding errors.
    assert np.allclose(normalize_ref(data.copy()), normalize_vec(arr))

def test_empty_case():
    data = []
    arr = np.array(data)
    assert np.allclose(normalize_ref(data.copy()), normalize_vec(arr))

def test_boundary_case_single_element():
    data = [42.0]
    arr = np.array(data)
    assert np.allclose(normalize_ref(data.copy()), normalize_vec(arr))

def test_boundary_case_identical_elements():
    data = [7.0, 7.0, 7.0]
    arr = np.array(data)
    assert np.allclose(normalize_ref(data.copy()), normalize_vec(arr))

def test_aliasing_case():
    data = [1.0, 2.0, 3.0]
    arr = np.array(data)
    data_copy = data.copy()
    arr_copy = arr.copy()
    normalize_ref(data_copy)
    normalize_vec(arr_copy)
    # Confirm neither function mutates the original
    assert data == [1.0, 2.0, 3.0]
    assert np.allclose(arr, np.array([1.0, 2.0, 3.0]))

def test_non_finite_case():
    data = [1.0, np.nan, np.inf]
    arr = np.array(data)
    with pytest.raises(ValueError):
        np.allclose(normalize_ref(data.copy()), normalize_vec(arr), equal_nan=True)
