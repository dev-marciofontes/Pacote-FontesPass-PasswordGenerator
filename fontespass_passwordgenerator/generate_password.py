import random
import string


def _generate_password(tamanho):
    chars = string.ascii_letters + string.digits + '!çÇ@#$%&()=+*/,.;?[]{}><'
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars) for _ in range(tamanho))


def execute_fontespass():
    while True:
        escolha_tamanho = int(input("Digite o tamanho da senha que você deseja (valores acima de 12): "))

        if escolha_tamanho > 12:
            tamanho = escolha_tamanho

            print("#" * 60)
            print("A senha gerada foi:")
            print(_generate_password(tamanho))
            print("\nLembre-se de anotar em algum lugar!!")
            print("\n** Obrigado por usar o FontesPass **")
            print("#" * 60)
            break
        else:
            print("\n** Para a sua segurança, o tamanho da senha precisa ser maior do que 12!! **\n")


if __name__ == "__main__":
    execute_fontespass()
