import os

def isc0nd3file(path):
    try:
        os.system(f'attrib +h "{path}"')
        return True
    except Exception as e:
        return str(e)

def isc0nd3file2(path):
    try:
        os.system(f'attrib -h "{path}"')
        return True
    except Exception as e:
        return str(e)