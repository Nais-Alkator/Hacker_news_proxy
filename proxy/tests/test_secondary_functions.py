import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from secondary_functions import get_edited_string


def test_get_edited_string():
	assert get_edited_string("Nikita") == "Nikita™"
	assert get_edited_string("Nikita:") == "Nikita™:"
	assert get_edited_string("Dima") == "Dima"
	assert get_edited_string('"Andrey') == '"Andrey™'
	assert get_edited_string('"Andrey:') == '"Andrey™:'