import random
wrong = 0
right = 0
for n in range(0, 1000):  # povtorjenije
    a = [False, False, False]  # dverji
    rightOne = random.randint(0, 2)  # randomno vibirajem pravilnuju
    a[rightOne] = True  # prisvajevajem znacenije pravelnoj

    choice = random.randint(0, 2)  # chto igrok vibirajet

    b = 0  # dverj kotoruju otkrojut
    if a[choice] == False:
        # esli igrok vibral ne pravilnuju to tut ja scitaju edinstvennuju dverj kotoruju mozno otkritj
        b = 3 - choice - rightOne
    else:
        # esli igrok vibral pravilnuju to sluchaino iz ostavshihsja 2 vibiraju kokuju otkritj
        b = (choice + random.randint(1, 2)) % 3

    if a[choice]:
        print('RIGHT!')
        right += 1
    else:
        print("unlucky")
        wrong += 1  # chitaju rezultati
print('wrong: ' + str(wrong))
print('right: ' + str(right))  # vivozu rezultati
