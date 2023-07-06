#! python3

###                                                                 Raising Exceptions
# raise Exception('This is Raising an Exception')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol Must Be a Single Character String')
    if width <= 2:
        raise Exception('Width Must Be Greater Than 2')
    if height <= 2:
        raise Exception('Height Must Be Greater Than 2')
    

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

boxPrint('*', 5, 4)

for sym, w, h in (('*', 5, 2),('O', 2, 2),('w', 25, 5)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An Exception happened: ' + str(err))
        

