# example on how modules can be useful

import withdrawal
import deposit
import transfer

import deposit
import transfer
import withdrawal


def atm():
    user_option = input('')
    amount = 300
    account = input('account: ')
    transfer_bank = input('bank: ')

    if user_option in ['Withdrawal', 'deposition', 'transfer']:
        if user_option == 'Withdrawal':
            withdrawal.withdraw_money(amount)
        elif user_option == 'deposition':
            deposit.check_account_type(account)
            deposit.check_amount_type(amount)
        elif user_option == 'transfer':
            transfer.check_bank(transfer_bank)
    else:
        print('Unknown user option')
