import requests

def toFTC(v,c='gbp',j='0'):
    payload = {'output': c, 'amount': v, 'json': j}
    to_ftc_url = 'http://api.feathercoin.com/'
    fvalue=-1
    try:
        r = requests.get(to_ftc_url, params=payload)
        if r.status_code == 200:
            fvalue = round(float(r.text) ,6)
            print fvalue
    except:
        pass
    return fvalue

