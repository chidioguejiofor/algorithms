from urllib.request import urlopen



def read(file_name = 'input'):
    numbers_list =[]
    with open('hacker_rank/special_multiple/{0}.txt'.format(file_name), 'r') as file:
        for line in file:
            numbers_list.append(line.split('\n')[0])
        return numbers_list

def solve(n):
    count = 1
    
    while True:
        binary_str ="{0:b}".format(count)
        x = int(binary_str) * 9 
        if x >= n and x % n == 0:
            return str(x) 
        
        
        count = count + 1

if __name__ == '__main__':
    output_list = read('output')
    for index,n in enumerate(read('input')):
        special_number = solve(int(n))
        if output_list[index] != special_number:
            print('Failed for value n = {}'.format(n)  )


