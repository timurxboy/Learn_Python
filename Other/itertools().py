import itertools as it

""" repeat() """
repeat_module = it.repeat('WIN', 10)
print(repeat_module)


""" cycle() """
cycle_module = it.cycle(['A', 'B', 'C'])
print(list(next(cycle_module) for _ in range(10)))


""" accumitale() """
accumulate_module = it.accumulate([1, 2, 3, 4, 5])
print(*accumulate_module)


accumulate_module_1 = it.accumulate([3, 1, 4, 2, 7, 3, 8, 5, 9 ], max)
print(*accumulate_module_1)


""" chain()  chain.from_iterable() """
chain_module = it.chain('ABC', 'DEF')
print(*chain_module)

chain_from_iterable_module = it.chain.from_iterable(['ABC', 'DEF'])
print(*chain_from_iterable_module)


""" takewhite() """
takewhite_module = it.takewhile(lambda x: x<3, [1,2,3,4,5])
print(*takewhite_module)


""" dropwite() """
dropwite_module = it.dropwhile(lambda x: x<3, [1,2,3,4,5])
print(*dropwite_module)


""" filterfalse() """
filterfalse_module = it.filterfalse(lambda x: x%2==0, range(10))
print(*filterfalse_module)


""" tee() """
tee_module1, tee_module2 = it.tee([1,2,3], 2)
print(*tee_module1)
print(*tee_module2)


""" zip_longest() """
names = ['Carlen', 'caruna', 'Mamedyarov', 'Ding', 'Giri', 'Kramnik']
scores = [2848, 2822, 2801, 2797, 2780]
players = dict(it.zip_longest(names, scores, fillvalue=0))
print(players)


""" groupby() """
lst = [1, 2, 1, 2, 2, 3, 3, 2]
for keys, values in it.groupby(sorted(lst)):
    print('{}:{}'.format(keys, list(values)))

forecasr = [
    { 'humidity' : 20,  'temperature' : 78, 'wind' : 7 },
    { 'humidity' : 50,  'temperature' : 61, 'wind' : 10 },
    { 'humidity' : 100, 'temperature' : 81, 'wind' : 5 },
    { 'humidity' : 90,  'temperature' : 62, 'wind' : 15 },
    { 'humidity' : 20,  'temperature' : 84, 'wind' : 19 },
    { 'humidity' : 0,   'temperature' : 66, 'wind' : 28 },
    { 'humidity' : 100, 'temperature' : 87, 'wind' : 12 },
    { 'humidity' : 0,   'temperature' : 68, 'wind' : 14 },
    { 'humidity' : 90,  'temperature' : 86, 'wind' : 4 },
    { 'humidity' : 50,  'temperature' : 68, 'wind' : 0 },
]
def group_sorted(iterable, key=None):
    return it.groupby(sorted(iterable, key=key), key=key)
grouped_data = group_sorted(forecasr, key=lambda x: x['humidity'])
for keys, values in grouped_data:
    print('{}:{}'.format(keys, list(values)))


""" count()   islise() """
event_numbers = it.count(0,2)
print(list(it.islice(event_numbers, 2, 10, 2)))

event_numbers = it.count(0,2)
print(list(it.islice(event_numbers, 2, 4)))

event_numbers = it.count(0,2)
print(list(it.islice(event_numbers, 4)))


""" permutations() """
pin = [7, 5, 2, 8]
print(list(it.permutations(pin)))



""" product() """
ranks = ['6', '7', '8', '8', '9', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']
lst = list(it.product(ranks, suits))
print(lst)


""" combinations() """
print(list(it.combinations('ABCD',2)))





















