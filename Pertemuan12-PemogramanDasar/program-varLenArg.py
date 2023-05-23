def varLenArg(*daftarNamaMhs) :
    j = 10
    for i in daftarNamaMhs :
        j = j + 1  
        print(f"Nama ke-{j} = {i}")
        
varLenArg("Melani", "Fikri", "DimasChelli", "Pirton")