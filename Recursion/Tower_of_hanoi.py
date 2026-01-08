def tower_of_hanoi(n, source, destination, auxiliary):
    if n==0:
        return 
    
    if n ==1:
        print(source, '--->', destination)
        return 
    
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(source, '--->', destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)

tower_of_hanoi(3, 'source', 'destination', 'auxiliary')

