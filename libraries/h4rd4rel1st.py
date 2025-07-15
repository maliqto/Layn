import subprocess as sp

def h4rd4rel1st():
    try:
        result = sp.Popen("wmic cpu get name,NumberOfCores,NumberOfLogicalProcessors /format:list", stderr=sp.PIPE, stdin=sp.DEVNULL, stdout=sp.PIPE, shell=True, text=True)
        out, err = result.communicate()
        result.wait()
        return out
    except Exception as e:
        return str(e)