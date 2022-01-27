from browser import document, console, alert

input = document['input']
button = document['btn']
output = document['output']
select = document['select']

def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is int:
            alert('Harap masukkan Kata!')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp
            

def formula(x, y):
    if x == 'Upper':
        Upper = 'Uppercase = ' + y.upper()
        return Upper
    elif x == 'Lower':
        Lower = 'Lowercase = ' + y.lower()
        return Lower
    else :
        return 0


def main(ev):
    num = getNum(input.value)
    result = formula(select.value, num)
    output.textContent = result

def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)
        
button.bind('click', main)
input.bind("keypress", keyEnter)
