import unittest
from unittest.mock import patch
from io import StringIO
import importlib
import sys

def load_module():
    if 'src.guess_number' in sys.modules:
        importlib.reload(sys.modules['src.guess_number'])
    else:
        import src.guess_number

class TestGuessingGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['17', '13', '14'])
    @patch('random.randint', return_value=14)
    def test_win_case(self, mock_randint, mock_input):
        with patch("sys.stdout", new_callable = StringIO) as fake_out:

            load_module()
                
            output = fake_out.getvalue()

            assert "¡Felicitaciones! ¡Has adivinado el número!" in output

    @patch('builtins.input', side_effect=['6', '19', '15'])
    @patch('random.randint', return_value=16)
    def test_lose_case(self, mock_randint, mock_input):
        with patch("sys.stdout", new_callable = StringIO) as fake_out:

            load_module()
                
            output = fake_out.getvalue()

            assert "Lo siento, no adivinaste el número. El número correcto era 16." in output
