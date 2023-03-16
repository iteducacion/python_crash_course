


import subprocess as so

import pandas


# out_command = so.run('pwd', shell=True)


# print(dir(out_command))

# print(out_command)


# for entry in dir(so):
#     print (entry)
#     print (getattr(so, entry))
#     print (type(getattr(so, entry)))
#     print ('-'*50)

contador = 0
for show in dir(locals()['__builtins__']):
    if( 'Error' in show):
        print(f" nro: {contador} excepción: {show}")
        contador += 1



