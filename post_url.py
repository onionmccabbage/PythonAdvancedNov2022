import requests

def makePost():
    url = 'https://httpbin.org/post'
    # the POST method requires a payload
    payload = {'item':'pencil', 'status':'sharp', 'cost':3.99}
    h = {"Content-Type":"application/json; charset=utf-8"}
    try:
        res = requests.post(url, json=payload, headers=h)
        print(res.text)
    except Exception as err:
        print( f'Something went wrong {err}' )

if __name__ == '__main__':
    makePost()