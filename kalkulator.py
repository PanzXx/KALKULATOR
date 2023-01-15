#define funcoes

def adi(num1, num2):
  return num1 + num2
  
def sub(num1, num2):
  return num1 - num2
  
def mult(num1, num2):
  return num1 * num2
  
def div(num1, num2):
  return num1 / num2
  
#printa e define a realizacao das operacoes
  
print("PILIH OPERASINYA\n" \

        "1. PENAMBAHAN\n" \

        "2. PENGURANGAN\n" \

        "3. PERKALIAN\n" \

        "4. PEMBAGIAN\n")
        
select = int(input("PILIH DENGAN MENGETIKAN ANGKA YANG DIINGINKAN :"))

number_1 = int(input("ANGKA PERTAMA: "))
number_2 = int(input("ANGKA KEDUA: "))

if select == 1:

    print(number_1, "+", number_2, "=",

                    adi(number_1, number_2))
 

elif select == 2:

    print(number_1, "-", number_2, "=",

                    sub(number_1, number_2))
 

elif select == 3:

    print(number_1, "*", number_2, "=",

                    mult(number_1, number_2))
 

elif select == 4:

    print(number_1, "/", number_2, "=",

                    div(number_1, number_2))

else:
  print("Valor inserido invalido!")
 

  
                                                                    