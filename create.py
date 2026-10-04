from db_config import Message


def create_message():
    # パターン1
    message = Message(user="Bob", content="Hello Tom!")
    message.save()

    # パターン2
    Message.create(user="Tom", content="Hello Bob!")


if __name__ == "__main__":
    create_message()
