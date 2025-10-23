import unittest
from cli_tools.main import greet

def test_greet():
    assert greet("Rijul Belowo")=="Hey wassup,Rijul Belowo"