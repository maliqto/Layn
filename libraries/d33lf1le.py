import os

def d33l3t33(path):
    try:
        os.remove(path)
        return True
    except Exception as e:
        return str(e)