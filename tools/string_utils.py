def decode_string(string):
    _string = string
    if isinstance(_string, bytes):
        _string = _string.decode()
    return _string
