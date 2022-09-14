from colorama import Fore, Style

with open('balance') as b:
    balance = int(b.readline())

new_transactions = []

with open('transactions') as t:
    oldtransactions = list(t.readlines())
    for line in oldtransactions:
        if line.rstrip():
            new_transactions.append(line)


def bank_menu():
    print(Fore.CYAN + '\nБаланс: ' + str(balance))
    print(Style.RESET_ALL)
    print('МЕНЮ\n1. пополнить счёт;\n2. снять деньги;\n3. история транзакций;\n4. выход.\n')
    choice = input('Выберите один из пунктов: ')
    return choice


loop = 1
while loop == 1:

    choice = bank_menu()

    if choice == '1':
        adding = int(input('Сумма пополнения: '))
        balance = balance + adding
        new_transactions.append('Пополнение +' + str(adding)  + ';')
        print('Баланс пополнен на ' + str(adding) + '\n')

    elif choice == '2':
        withdrawal = int(input('Сумма снятия: '))

        if withdrawal <= balance:
            balance -= withdrawal
            new_transactions.append('Снятие     -' + str(withdrawal) + ';')
            print('С счёта были сняты ' + str(withdrawal) + '\n')
        if withdrawal >> balance:
            print(Fore.RED + 'Недостаточно средств'+ Style.RESET_ALL)

    elif choice == '3':
        print('\nИстория транзакций:')
        for i in new_transactions:
            print(i)

    elif choice == '4':
        print('\nДо свидания!')
        break


with open('balance', 'r+') as b:
    newbalance = str(balance)
    plug = ''
    b.writelines(plug)
    b.writelines(str(newbalance))

with open('transactions', 'r+') as t:
    for transaction in new_transactions:
        t.writelines(transaction + '\n')

#newtransactions = transactions
#t.writelines(plug)
#t.writelines(newtransactions)