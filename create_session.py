from urllib.request import Request, urlopen

def create_session(username, password):
    s = 'https://api.stibarc.gq/createsess.sjs?username=' + username +'&password=' + password
    print(s)
    req = Request(s, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    w = str(webpage)
    w = w.replace("'","")
    w = w.replace("b","")
    w = w.replace("n","")
    w = w.replace('\\',"")
    return w
  
print('Updated')