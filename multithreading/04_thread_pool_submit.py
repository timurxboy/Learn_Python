import concurrent.futures
import time


def div(divisior, limit):
    print(f'started div={divisior}')
    result = 0
    for x in range(1, limit):
        if x%divisior == 0:
            result += x
            #print(f'divisior={divisior}, x = {x}')
        time.sleep(0.2)
    print(f'ended div={divisior}', end='\n')
    return result


if __name__ == '__main__':
    print('started main')

    future = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future.append(executor.submit(div, 3, 25))
        future.append(executor.submit(div, 5, 25))

        # while future[0].running() and future[1].running():
        #     print('.', end='')
        #     time.sleep(0.5)

        for f in future:
            print(f'{f.result()}')

    print('After with block')





    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    # executor.submit(div, 3, 25)
    # executor.submit(div, 5, 25)
    #
    # executor.shutdown(wait=True)