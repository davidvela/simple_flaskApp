from requests import put, get

def main():
    # print("hi");  return
    
    ret = get('http://localhost:5000/hello').json()
    print(ret) # hello world 
    return

    ret = put('http://localhost:5000/todo1', data={'data': 'Remember the milk2'}).json()
    print(ret) # {u'todo1': u'Remember the milk'}

    ret = get('http://localhost:5000/todo1').json()
    print(ret) # {u'todo1': u'Remember the milk'}
    ret = put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
    print(ret) # {u'todo2': u'Change my brakepads'}
    ret = get('http://localhost:5000/todo2').json()
    print(ret) # {u'todo2': u'Change my brakepads'}

    
if __name__ == "__main__":
    main()