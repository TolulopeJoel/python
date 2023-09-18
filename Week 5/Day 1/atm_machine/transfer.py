def same_bank():
    pass


def other_banks():
    pass


def check_bank(bank):
    our_bank = 'default'
    if bank == our_bank:
        return same_bank()
    else:
        return other_banks()
