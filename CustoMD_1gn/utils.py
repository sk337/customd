def read_line(buffer):
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
