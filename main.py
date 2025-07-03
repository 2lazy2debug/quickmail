import quickmail as qm

def main():

    print("📬 Inbox Lite - Last update 🕑: [GET-DATE] - Showing [FOLDER] - [READ/UNREAD] \
    - ⬆️⬇️ to navigate \
    - Enter to view \
    - 'd' to delete e-mail \
    - 'u' to update the list \
    - 't' to toggle between unread/all \
    - 'l' to change folder \
    - 'q' to quit \
    ")

    if(not qm.account.is_logged_in()):
        
        print("Please login first.")
        username = input("Enter your username (user@domain.com): ")
        password = input("Enter your password: ")
        account = qm.account.login(username, password)

        if account:
            qm.mail.get_inbox_messages(account, is_read=False)
            messages = qm.mail.get_inbox_messages(account, is_read=False)
            qm.util.print_messages_list(messages)
        else:
            print("No account found. Please login first.")