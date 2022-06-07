def show_message(msg_list, printed_msg):

    while msg_list:
        msg = msg_list.pop()
        print(msg.title())
        printed_msg.append(msg)


a_msg_list = ['Bonjour', 'hello', 'howdy', 'greetings', 'cheers']
another_list = []

show_message(a_msg_list[:], another_list)
print(f"Initial list: {a_msg_list}")
print(f"Completed list: {another_list}")
