import pickle

# Сериализация (пиклинг) объекта в файл
data = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# Восстановление (анпиклинг) объекта из файла
with open('data.pickle', 'rb') as f:
    restored_data = pickle.load(f)

print(restored_data)