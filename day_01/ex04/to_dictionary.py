def get_country():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]


    new_dict = dict()
    for i in range(len(list_of_tuples)):
        if list_of_tuples[i][1] in new_dict:
            new_dict[list_of_tuples[i][1]].append(list_of_tuples[i][0])
        else:
            new_dict[list_of_tuples[i][1]] = [list_of_tuples[i][0]]

    for key, value in new_dict.items():
        for i in value:
            print(f"'{key}' : '{i}'")


if __name__ == '__main__':
    get_country()
