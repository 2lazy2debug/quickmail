from exchangelib import Account, Message
from quickmail.account import is_valid_account
from exchangelib.folders import Mailbox, Messages, MailFolder

current_folder = "Inbox"

def get_inbox_messages(account: Account, is_read : bool = False) -> list[Message]:
    if is_valid_account(account):
        try:
            inbox = account.inbox
            messages = inbox.filter(is_read=is_read)
            return messages
        except Exception as e:
            print(f"Failed to retrieve messages: {e}")
            return []
    return []

def get_folders_list(account: Account) -> list[str]:
    if is_valid_account(account):
        try:
            folders = account.root.walk()
            folder_names = [
                folder.name
                for folder in folders
                if isinstance(folder, MailFolder)
            ]
            return folder_names
        except Exception as e:
            print(f"Failed to retrieve folders: {e}")
            return []
    return []

def set_current_folder(folder_name: str) -> None:
    global current_folder
    current_folder = folder_name

def get_current_folder() -> str:
    return current_folder

def toggle_read_unread(account: Account, message_id: str) -> bool:
    if is_valid_account(account):

        try:
            message = account.inbox.get(id=message_id)
            message.is_read = not message.is_read
            message.save()
            return True
        except Exception as e:
            print(f"Failed to mark message as read/unread: {e}")
            return False
    return False
    
def delete_message(account: Account, message_id: str) -> bool:
    if is_valid_account(account):
        try:
            message = account.inbox.get(id=message_id)
            message.delete()
            return True
        except Exception as e:
            print(f"Failed to delete message: {e}")
            return False
    return False