"""
_init_ file that contains AST generator and html builder (TBC)
"""

from io import BytesIO
from xml.etree import ElementTree as ET
import utils

class Customd:
    """
    Primary Class that contains all functionallity
    """
    def _gen_ast(self, text):
        def read_element(self, buffer):
            c=buffer.read(1)
            if c == b"#":
                utils.read_header(buffer, buffer.tell())

        ast = {
            "elements": []
        }
        buffer = BytesIO(text.encode())
        runASTwalker= True
        return ast


    def __init__(self, c):
        self.text = c
        self.ast = self._gen_ast(self.text)
        return None


