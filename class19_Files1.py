'''
Manejo de archivos en Python
Con Python también podemos leer y escribir archivos del sistema.

Existen varios modos en los que podemos manejar archivos

‘r’ = leer
’w’ = escribir
’a’ = añadir
’r+’ = leer y escribir

Siempre recuerda cerrar el archivo.

El keyword with nos permite manejar el contexto al trabajar con archivos






defrun():
    counter = 0
    with open('aleph.txt', encoding='utf-8') as f:
        for line in f:
            counter += line.count('Beatriz')

    print('Beatriz se encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    run()```











'''
def run():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))


if __name__ == '__main__':
    run()