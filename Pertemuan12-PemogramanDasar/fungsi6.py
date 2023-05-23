def jumlah(*args) :
    if args is None : return 0.0
    total = 0.0
    for a in args :
        total += a
    return total

def main() :
    print("1 + 2 + 3 + 4 + 5 = %d" % jumlah(1, 2, 3, 4, 5))
    
if __name__ == '__main__' :
    main()
