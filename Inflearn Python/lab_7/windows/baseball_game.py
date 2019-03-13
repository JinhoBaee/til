# -*- coding: utf-8 -*-

import random


def get_random_number():              #랜덤한 난수 발생(백의 자리)
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)

#-----------------------------------------------------

def is_digit(user_input_number):    #정수가 영보다 크다면 True를 리턴, 아닐 시 False 리턴
    try:
        if int(user_input_number) > 0:
            return True
        else:
            return False

        
        return result
    except:
        return False

#------------------------------------------------------

def is_between_100_and_999(user_input_number):             #100보다 작거나 1000보다 크다면, False 
    if int(user_input_number) >= 100:
        if int(user_input_number) < 1000:
            result = True
        else:
            result = False
    else:
        result = False
    return result

   


def is_duplicated_number(three_digit):
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # Hint - Len과 Set을 써서 할 수 있음, 중복되는 값의 str 길이는 1 또는 2
    # Three digit 의 길이가 3일시 False 를 리턴하고 그렇지 않을시 True return
    if len(set(three_digit)) == 3:
        result = False
    else:
        result = True
    # ==================================
    return result


def is_validated_number(user_input_number):
    if is_digit(user_input_number) is True:
        if is_between_100_and_999(user_input_number) is True:
            if is_duplicated_number(user_input_number) is False:
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False
    # ==================================
    return result




def get_not_duplicated_three_digit_number():
    a = "0"
    is_validated_number(a)
    
    while is_validated_number(a) is not True:
        a = str(get_random_number())
        result = a
    # ==================================
    return result



def get_strikes_or_ball(user_input_number, random_number):
   
    i = 0                #초기 설정값 (i = loop)
    strike = 0
    ball = 0
    user_input_number = user_input_number.strip()
    random_number = random_number.strip()
    
    while(i < 3):
        j = 0
        while(j < 3):
            if is_validated_number(user_input_number) == False:   #애초에 유효한 수가 아니라면 Break
                break
            
            elif (i == j) is True:              #strike 가 되던가
                if random_number[i] == user_input_number[j]:
                    strike += 1
            else:                               #Ball 이 된다
                if random_number[i] == user_input_number[j]:
                    ball += 1
            j += 1
        i += 1
    result = [strike, ball]
    # ==================================
    return result


def is_yes(one_more_input):
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
   

    if one_more_input.upper() == 'Y':
        result = True
    else:
        if one_more_input.upper() == 'YES':
            result = True
        else:
            result = False
    # ==================================
    return result


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
  
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    if one_more_input.upper() == 'N':
        result = True
    else:
        if one_more_input.upper() == 'NO':
            result = True
        else:
            result = False
    # ==================================
    return result



def main():
    print("Play Baseball")

    random_number = str(get_not_duplicated_three_digit_number())

    print("Random Number is : ", random_number)
    user_input = '999'

    while(get_strikes_or_ball(user_input, random_number) != [3, 0]):

        user_input = input("Input guess number : ")

        if user_input != '0':

                if is_validated_number(user_input) is True:
                    get_strikes_or_ball(user_input, random_number)
                    print("Strikes : " +
                    str(get_strikes_or_ball(user_input, random_number)[0]) + " , " +
                    "Balls : " + str(get_strikes_or_ball(user_input, random_number)[1]))
                else:
                    print("Wrong Input, Input again")

        else:
            break

    if user_input is not '0':
        one_more_input = 'Y'
        while(is_no(one_more_input)) is not True:
            one_more_input = input("You win, one more(Y/N) ?")

            if is_yes(one_more_input) is True:
                random_number = str(get_not_duplicated_three_digit_number())

                print("Random Number is : ", random_number)
                user_input = '999'

                while(get_strikes_or_ball(user_input, random_number) != [3, 0]):

                    user_input = input("Input guess number : ")

                    if user_input != '0':

                            if is_validated_number(user_input) is True:
                                get_strikes_or_ball(user_input, random_number)
                                print("Strikes : " +
                                str(get_strikes_or_ball(user_input, random_number)[0]) + " , " +
                                "Balls : " + str(get_strikes_or_ball(user_input, random_number)[1]))
                            else:
                                print("Wrong Input, Input again")

                    else:
                        break

            elif is_no(one_more_input) is True:
                break
            else:
                print("Wrong Input, Input again")

    print("Thank you for using this program")
    print("End of the Game")
    # ===Modify codes below=============
    # 위의 코드를 포함하여 자유로운 수정이 가능함
    # ==================================

if __name__ == "__main__":
    main()