from pathlib import Path as m_path
import time as m_time

print(m_time.time())
print(m_time.ctime())


# ===== code profiling using epoch unix timestamps
def c_product():
    p = 1
    for iter in range(1, 100001):
        p *= iter
    return p

get_starttime = m_time.time()
res = c_product()
get_endtime = m_time.time()
print(f'It took EXACTLY {1000 * (get_endtime - get_starttime)}')

# =====  KeyBoard Stop and Go Timer

print('start sswatch')
start_time = m_time.time()
end_time = start_time

l_num = 1

try:
    while True:
        input()
        lap_time = round(m_time.time()-end_time,2)
        total_time = round(m_time.time()-start_time,2)
        print(f'Loop Number {l_num}: {total_time} ({lap_time})')
        l_num+=1
        end_time = m_time.time()
except KeyboardInterrupt as e:
    print('\nExit')



# if __name__ == '__main__':
#     get_starttime = m_time.time()
#     res = c_product()
#     get_endtime = m_time.time()
#     print(f'It took EXACTLY {(get_endtime - get_starttime)}')
