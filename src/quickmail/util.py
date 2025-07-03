from exchangelib import Message



def print_message_details(message: Message) -> None:
    """
    Print details of the given message.
    
    Args:
        message (Message): The message to print details for.
    """
    print(f"Subject: {message.subject}")
    print(f"From: {message.sender.email_address}")
    print(f"To: {', '.join([recipient.email_address for recipient in message.to_recipients])}")
    print(f"Date: {message.datetime_received}")
    print(f"Is Read: {message.is_read}")
    print(f"Body: {message.body}")  # Note: This may be large, consider truncating if necessary

def print_messages_list(messages: list[Message]) -> None:
    """
    Print a list of messages with their details.
    
    Args:
        messages (list[Message]): The list of messages to print.
    """
    for message in messages:
        has_attachments = "📎" if getattr(message, "attachments", []) else "  "
        unread = "✉️" if not message.is_read else "✅"
        received = message.datetime_received.strftime("%Y-%m-%d %H:%M") if message.datetime_received else ""
        from_addr = message.sender.email_address if message.sender else ""
        subject = message.subject if message.subject else ""
        # Clean body: remove newlines and truncate for display
        clean_body = str(message.body).replace('\n', ' ').replace('\r', ' ')
        clean_body = (clean_body[:40] + "...") if len(clean_body) > 43 else clean_body
        print(f" {has_attachments} | {unread} {received} | {from_addr} | {subject} | {clean_body}")