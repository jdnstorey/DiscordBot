import json


# ------------------------------------------ BALANCE ------------------------------------------
def open_file_balance(uuid: int):
    with open('UserData/UserBalance.json') as userData:
        # open file
        data = json.load(userData)
        # obtain balance info
        if f'{uuid}' in data:
            uuid_balance = data[f'{uuid}']
            return int(uuid_balance)
        elif f'{uuid}' not in data:
            write_file_balance(uuid, 0)
            userData.close()
            open_file_balance(uuid)

def write_file_balance(uuid: int, balance: str):
    with open('UserData/UserBalance.json', 'r+') as f:
        data = json.load(f)
        data[f'{uuid}'] = balance  # <--- add `id` value.
        f.seek(0)  # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()  # remove remaining part

def open_file_free_credits(uuid: int):
    with open('UserData/FreeCredits.json') as fc:
        data = json.load(fc)
        if f'{uuid}' in data:
            return True
        elif f'{uuid}' not in data:
            write_file_free_credits(uuid)
            fc.close()
        else:
            return

def write_file_free_credits(uuid: int):
    with open('UserData/FreeCredits.json', 'r+') as fc:
        data = json.load(fc)
        data[f'{uuid}'] = "y"
        fc.seek(0)
        json.dump(data, fc, indent=4)
        fc.truncate()
# ------------------------------------------ BALANCE ------------------------------------------



# ------------------------------------------ BLACKJACK ------------------------------------------
def write_file_blackjack(uuid: int, score: str):
    with open('UserData/Blackjack.json', 'r+') as f:
        data = json.load(f)
        data[f'{uuid}'] = score  # <--- add `id` value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

def open_file_blackjack(uuid: int):
    userData = open('UserData/Blackjack.json')
    data = json.load(userData)
    score = data[f'{uuid}']
    userData.close()
    return int(score)
