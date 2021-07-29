import pytest

from workouts import print_workout_days


@pytest.mark.parametrize("str_workout, expected",
                         [
                             ("upper", "Mon, Thu"),
                             ("lower", "Tue, Fri"),
                             ("cardio", "Wed"),
                             ("stretching", "No matching workout"),
                             ("yoga", "No matching workout"),
                             ("", "Mon, Tue, Wed, Thu, Fri")
                         ])
def test_print_workout_days(capsys, str_workout, expected):
    print_workout_days(str_workout)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected    # strip out the new lines
