penggunaan_elektrik1=int(input("Sila masukkan penggunaan elektrik1:"))

if 1<=penggunaan_elektrik1 <=200 :
    kadar_tarif1=0.218

elif 201<=penggunaan_elektrik1 <=300 :
    kadar_tarif1=0.334

elif 301<=penggunaan_elektrik1<=600 :
    kadar_tarif1=0.516

else:
    kadar_tarif1=0.546
    
print("Kadar tarif1 ialah:",kadar_tarif1)
bil_elektrik1=penggunaan_elektrik1*kadar_tarif1
print("Bil elektrik 1 ialah",bil_elektrik1)

penggunaan_elektrik2=int(input("Sila masukkan penggunaan elektrik2:"))
if 1<=penggunaan_elektrik2 <=200 :
    kadar_tarif2=0.218

elif 201<=penggunaan_elektrik2 <=300 :
    kadar_tarif2=0.334

elif 301<=penggunaan_elektrik2<=600 :
    kadar_tarif2=0.516

else:
    kadar_tarif2=0.546

print("Kadar tarif 2 ialah:",kadar_tarif2)
bil_elektrik2=penggunaan_elektrik2*kadar_tarif2
print("Bil elektrik 2 ialah",bil_elektrik2)

penggunaan_elektrik3=int(input("Sila masukkan penggunaan elektrik3:"))
if 1<=penggunaan_elektrik3 <=200 :
    kadar_tarif3=0.218

elif 201<=penggunaan_elektrik3 <=300 :
    kadar_tarif3=0.334

elif 301<=penggunaan_elektrik3<=600 :
    kadar_tarif3=0.516

else:
    kadar_tarif3=0.546
print("Kadar tarif 3 ialah:",kadar_tarif3)
bil_elektrik3=penggunaan_elektrik1*kadar_tarif3
print("Bil elektrik 3 ialah",bil_elektrik3)

penggunaan_elektrik4=int(input("Sila masukkan penggunaan elektrik4:"))
if 1<=penggunaan_elektrik4 <=200 :
    kadar_tarif4=0.218

elif 201<=penggunaan_elektrik4 <=300 :
    kadar_tarif4=0.334

elif 301<=penggunaan_elektrik4<=600 :
    kadar_tarif4=0.516

else:
    kadar_tarif4=0.546
print("Kadar tarif 4 ialah:",kadar_tarif4)
bil_elektrik4=penggunaan_elektrik1*kadar_tarif4
print("Bil elektrik 4 ialah",bil_elektrik4)

jumlah_bil_elektrik=bil_elektrik1+bil_elektrik2+bil_elektrik3+bil_elektrik4
print("Jumlah bil elektrik ialah RM:",jumlah_bil_elektrik)
