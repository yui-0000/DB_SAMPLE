from db_config import Message
from read_all import display_all_messages


def update_message():
    id = 2
    msg = Message.get_by_id(id)
    msg.user = "Tom Cruise"
    msg.save()


if __name__ == "__main__":
    display_all_messages()

    update_message()

    display_all_messages()
