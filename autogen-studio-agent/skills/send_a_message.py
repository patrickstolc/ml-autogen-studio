from typing import Annotated


def send_a_message(message: Annotated[str, "Message to send"]) -> None:
    """
    Function to send a message.

    :param message: message to send.

    :return: None
    """
    print("sending message: ", message)

    return None


# Example usage of the function:
# send_a_message("hello, here is your result: " + result)
