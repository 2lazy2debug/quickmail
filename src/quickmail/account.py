from exchangelib import Credentials, Account

logged_in :bool = False

def login(username : str, password : str) -> Account | None:
    credentials = Credentials(username=username, password=password)
    try:
        account = Account(
            primary_smtp_address=username,
            credentials=credentials,
            autodiscover=True,
        )
        return account
    except Exception as e:
        print(f"Login failed: {e}")
        return None

def is_valid_account(account: Account | None) -> bool:
    global logged_in
    if not account or not account.is_authenticated:
        print("Invalid account.")
        logged_in = False
        return False
    logged_in = True
    return True