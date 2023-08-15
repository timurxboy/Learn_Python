import concurrent.futures

from multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main')

    data = read_ints('1Kints.txt')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        result = executor.map(count_three_sum, (data, data), ('t1', 't2'))
        print('after map')
        for r in result:
            print(f'{r=}')
        print('End of map')

    print('ended main') 
