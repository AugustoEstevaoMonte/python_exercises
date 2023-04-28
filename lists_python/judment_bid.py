import art
import subprocess

judgement_processes = {}

bid_amount = 0


def show_cool_art(text: str):
    art.tprint(text)


def ask_name() -> str:
    name = input("Digite o seu nome: ")
    return name


def ask_bid() -> float:
    bid = float(input("Digite o valor da oferta: "))
    return bid


def insert_into_dictionary(name: str, bid: float) -> None:
    judgement_processes[name] = bid


def ask_for_another_user():
    usr_choice = input("Tem algum outro usuário para o julgamento? Digite 'S' para sim, e 'N' para não ")
    return usr_choice.lower()


def find_hightest_bidder():
    bid_amount = 0
    winner = ""
    for name, bid in judgement_processes.items():
        if bid > bid_amount:
            bid_amount = bid
            winner = name
    return bid_amount, winner


def main() -> None:
    while True:
        show_cool_art("Julgamento da Oferta")
        name = ask_name()
        bid = ask_bid()
        choice = ask_for_another_user()
        match choice.lower():
            case 's':
                insert_into_dictionary(name, bid)
                find_hightest_bidder()
            case 'n':
                insert_into_dictionary(name, bid)
                bid_amount, winner = find_hightest_bidder()
                print(f'O(a) ganhador é: {winner}, com o valor de {bid_amount}R$')
                break
            case _:
                print("Escolha inválida!")


main()
