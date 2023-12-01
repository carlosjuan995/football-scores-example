import pytest
import football_exercise

# single test
def test_calculate_points_tie():
    assert football_exercise.calculate_points(2, 2) == (1, 1)

# # This test uses a pytest parametrize decorator . Match the defined variables with the test input .
# # The different cases are defined as a list of tuples .
@pytest.mark.parametrize('score_t1, score_t2, points_t1, points_t2', [
    (0, 0, 1, 1),
    (1, 0, 3, 0),
    (0, 1, 0, 3)
])
def test_calculate_points(score_t1, score_t2, points_t1, points_t2):
    assert football_exercise.calculate_points(score_t1, score_t2) == (points_t1, points_t2)