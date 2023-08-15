table_card = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_card = ["J_D", "3_D"]

table_suites = [i[-1] for i in table_card]
hand_suites = [i[-1] for i in hand_card]

flush = False
summ = list(table_suites+hand_suites)
count = 0
for i in 'SHDC':
    if summ.count(i) >= 5:
        flush = True

if flush:
    print('Flush!')
else:
    print('No Flush!')