def readLine(buffer):
  data=""
  read = True
  while read:
    char = buffer.read(1)
    if char != b"\n":
      data += chr(char[0])
    else:
      read = False
  return data

def readHeader(buffer, start):
  headerLvl =1
  read=True
  while read:
    c = buffer.read(1)
    if c == b"#":
      headerLvl += 1
    elif c == b" ":
      data = readLine(buffer)
  if headerLvl >6:
    buffer.seek(start)
    return {"type": "text", "content": readLine(buffer)}