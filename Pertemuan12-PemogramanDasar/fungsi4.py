def kali() :
    return 10 * 20

def echo() :
    for i in range(3) :
        print('Python')
        
def main() :
    print("Memanggil fungsi kali() : ")
    print('10 x 2 = %d' % kali())

    print("\nMemanggil fungsi echo() : ")
    echo()
    
if __name__ == '__main__' :
    main()
    
    