from exchangelib import Credentials, Account

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
    if not account or not account.is_authenticated:
        print("Invalid account.")
        return False
    return True