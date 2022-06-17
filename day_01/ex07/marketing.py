import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
           'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']


def call_center():
    return list((set(clients) | set(participants)) - set(recipients))


def potential_clients():
    return list(set(participants) - set(clients))


def loyalty_program():
    return list(set(clients) - set(participants))


def ft_sets(arg):
    cmds = ["call_center", "potential_clients", "loyalty_program"]
    try:
        if arg not in cmds:
            raise Exception()
    except:
        print("wrong name is given")

    if arg == "call_center":
        print(call_center())
    elif arg == "potential_clients":
        print(potential_clients())
    elif arg == "loyalty_program":
        print(loyalty_program())


if __name__ == "__main__":
    if len(sys.argv) == 2:
        ft_sets(sys.argv[1])
