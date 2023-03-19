# python3
import time

def parallel_processing(n, m, data):
    output = []
    apstradesLaiks=[(l, i) for i, l in enumerate(data)]
    pavediens= [0]*n
    #pavediens=[(i, 0) for i in range(n)]
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    while apstradesLaiks:
        skaits= pavediens.skaits(min(pavediens))
        output.append((skaits, pavediens[skaits]))
        ilgums, apstrade= apstradesLaiks.pop(0)
        pavediens[skaits]+= ilgums
    #output.append((pavediens[0], pavediens[1]))
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    n, m=map(int, input().split())
    # TODO: create the function
    data=list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for pavediens, time in result:
        print(pavediens, time)
    # TODO: print out the results, each pair in it's own line

if __name__ == "__main__":
    main()
