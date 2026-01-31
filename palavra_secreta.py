import os

palavra = "Python"
letra_errada = ""
letra_correta = ""
tentativas = 0

while True:
    saida = ["sair," , "s", "sim", "ss", "eu quero sair"]

    print()
    letra_digitada = input("Digite uma letra: ").lower()

    if len(letra_digitada) > 1:
        print("Digite somente uma letra. Tente novamente!")
        print()
        continue

    if not letra_digitada.isalpha():
        print("Digite somente letras. Tente novamente!")
        print()
        continue

    if letra_digitada in letra_correta or letra_digitada in letra_errada:
        print(f'Você já digitou a letra "{letra_digitada}". Tente outra!')
        print()
        continue

    tentativas += 1

    if letra_digitada in palavra:
        letra_correta += letra_digitada
    else:
        letra_errada += letra_digitada

    palavra_formada = ""

    for letra in palavra:
        if letra in letra_correta:
            palavra_formada += letra
        else:
            palavra_formada += "*"

    print(f"Palavra: {palavra_formada}")
    print(f"Letras erradas: {letra_errada}")

    if "*" not in palavra_formada:
        os.system('cls')
        print(f'Parabéns, você ganhou o jogo e a palavra era "{palavra}"')
        print(f'Você precisou de: {tentativas}')

        if letra_digitada in saida:
            print("Obrigado por jogar. Encerrando...")
        break
