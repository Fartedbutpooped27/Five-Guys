from rpn import evaluate
import pytest as p

def test_evaluate_edge_cases():
    """Creates tests functions that tests expressions that consistent of a 
    single integer, a single float, a negative number, and a two-digit number.
    """
    assert evaluate("7") == p.approx(7)
    assert evaluate("8.7") == p.approx(8.7)
    assert evaluate("-7") == p.approx(-7)
    assert evaluate("21") == p.approx(21)
    
def test_evaluate_happy_path():
    """Creates test functions that test expressions that perform addition, 
    subtraction, multiplication, and division. Also tests expressions with
    multiple numbers and operators in different order.
    """
    assert evaluate("6 5 +") == p.approx(11) 
    assert evaluate("8 3 -") == p.approx(5)
    assert evaluate("2 6 *") == p.approx(12)
    assert evaluate("20 5 /") == p.approx(4)
    assert evaluate("6 4 6 * +") == p.approx(30)
    assert evaluate("5 6 + 3 *") == p.approx(33)