list_operationst = ['+', '-', '*', '/']
input_data =input("Введите выражение в виде польской нотации: математическкая операция и два положительных числа, разделенных пробелом: ")
data_list = input_data.split()
if len(data_list) == 3:
    arithmetic_sign = data_list[0]
    number1 = data_list[1]
    number2 = data_list[2]
    print(data_list)
    assert int(number1) >= 0 ,"Первое значение введено некорректно: или не положительное или не число" 
    assert int(number2) >= 0 ,"Второе значение введено некорректно: или не положительное или не число" 
    assert arithmetic_sign in list_operationst,"Нет такой " 
    #if int(number1) >= 0 and int(number2) >= 0:
    if arithmetic_sign == list_operationst[0]:
      print(f"Значение сложение {int(number1)+int(number2)}")
    elif arithmetic_sign == list_operationst[1]:
      print(f"Значение вычитания {int(number1)-int(number2)}")
    elif arithmetic_sign == list_operationst[2]:
       print(f"Значение умножения {int(number1)*int(number2)}")
    elif arithmetic_sign == list_operationst[3]:
       try:
         print(f" Значение  {int(number1)/int(number2)}")
       except ZeroDivisionError:
         print("Вы ввели 0, деление на 0 невозможно") 
    
      
else:
  print("Вы ввели некорректное выражение")