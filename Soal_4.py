beratbadan  = int(input(f"masukkan berat badan (Kg)  : "))
tinggibadan = float(input(f"masukkan tinggi badan (M) : "))

BMI = (beratbadan)/(tinggibadan**2)

if BMI < 18.5 :
    kategori = "berat badan kurang"
elif 18.5 <= BMI < 24.9 :
    kategori = "berat badan normal"
elif 25 <= BMI < 29.9 :
    kategori = "kelebihan berat badan "
elif BMI >= 30 :
    kategori = "obesitas"

print(f"berat badan     : {beratbadan} Kg")
print(f"tinggi badan    : {tinggibadan} M")
print(f"Nilai BMI anda  : {BMI}")
print(f"Kategori BMI    : {kategori}")




