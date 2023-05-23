def kali(a, b) :
    return a * b

def echo(s, n) :
    for i in range(n) :
        print(s)
        
def main() :
    print("\nPemanggilan pertama fungsi kali() : ")
    print(f"2 x 3 = {kali(2, 3)}")
    
    print("\nPemanggilan kedua fungsi kali() : ")
    print(f"10 x 20 = {kali(10, 20)}")
    
    print("\nPemanggilan pertama fungsi echo() : ")
    echo("Python", 5)
    
    print("\nPemanggilan kedua fungsi echo() : ")
    echo('Pemograman Python', 3)
    
if __name__ == '__main__' :
    main()
    
