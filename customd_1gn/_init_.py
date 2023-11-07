from io import BytesIO
from xml.etree import ElementTree as ET
import utils

class customd:
  def _genAST(self, text):
    def readElement(self, buffer):
      c=buffer.read(1)
      if c == b"#":
        utils.readHeader(buffer, buffer.tell())

    ast = {
      "elements": []
    }
    buffer = BytesIO(text.encode())
    runASTwalker= True


  def __init__(self, c):
    self.text = c
    self.ast = self._genAST(self.text)
    return None
