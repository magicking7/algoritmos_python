print('########################################')
print('#         ALGORITMOS EM PYTHON         #')
print('########################################')
print('# Escolha a opção desejada:            #')
print('#                                      #')
print('# 1. Fibonacci                         #')
print('########################################')

try:
    choice = int(input())

    if choice == 1:
        print('FIB')
    else:
        print('Opção inválida!')
except:
    print('Ocorreu um erro...')