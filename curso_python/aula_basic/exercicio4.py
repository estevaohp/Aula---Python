palavra_secreta = 'perfume'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada


    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if palavra_secreta in letras_acertadas:
             palavra_formada +=letra_secreta

        else:
             palavra_formada += '*'
        print("palavra formada")

    if palavra_formada == palavra_secreta:
        print('Você ganhou!')
        print('A palavra secreta era: ', palavra_secreta)


        