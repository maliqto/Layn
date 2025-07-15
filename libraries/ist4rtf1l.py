import os

def st44rtf1l3(path):
    try:
        os.startfile(path)
        return True
    except Exception as e:
        return str(e)