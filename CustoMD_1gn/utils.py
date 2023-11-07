"""
Utilites for _init_.py to make code cleaners
"""

def read_line(buffer):
    """
    Read to end of line
    """
    data=""
    read = True
    while read:
        char = buffer.read(1)
        if char != b"\n":
            data += chr(char[0])
        else:
            read = False
    return data

def read_header(buffer, start):
    """
    Read a markdown header child
    """
    header_lvl =1
    read=True
    while read:
        c = buffer.read(1)
        if c == b"#":
            header_lvl += 1
        elif c == b" ":
            data = read_line(buffer)
    if header_lvl >6:
        buffer.seek(start)
        return {"type": "text", "content": read_line(buffer)}
