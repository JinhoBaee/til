# -*- coding: utf-8 -*-


def is_positive_number(integer_str_value):       #자연수일 시 True 반환
    try:
        if int(integer_str_value) > 0:
            return True
        else:
            return False

        # ==================================
    except ValueError:
        return False
 
def get_factorial_value(integer_value):
    value = int(integer_value)
    if value == 1:
        return 1
    else:
        return value * (get_factorial_value(value - 1))
    
    
def main():
    user_input = 999
    while (user_input is not '0'):              #자연수라면 input을 넣어주고 
        user_input = input("Input a positive number:")       
        if is_positive_number(user_input):                 #get_factorial함수 실행
            result = get_factorial_value(int(user_input))    #결과값 반환
            print(result)
        elif user_input is '0':         #경우의 수 3가지, elif 구문 사용
            print("Thank you for using this program")
        else:
            print("Input again, Please")
                

if __name__ == "__main__":
    main()    
