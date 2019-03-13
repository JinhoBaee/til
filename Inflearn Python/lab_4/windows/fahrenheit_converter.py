# -*- coding: utf-8 -*-


#입력 함수
def input_celsius_value():        
    user_input = input("변환하고 싶은 섭씨 온도를 입력해주세요: ")
    celsius_value = float(user_input)
    return celsius_value


#온도 변환 함수(섭씨->화씨)
def convert_celsius_fahrenheit(celsius_value):
    fahrenheit_value = ((9 / 5) * float(celsius_value)) + 32
    return fahrenheit_value


#출력 함수
def print_fahrenheit_value(celsius_value, fahrenheit_value):
    print("섭씨온도: ",celsius_value)
    print("화씨온도: ",fahrenheit_value)
    return
  
    
#메인 함수
def main():
    print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================
    celsius_value = input_celsius_value()
    fahrenheit_value = convert_celsius_fahrenheit(celsius_value)
    print_fahrenheit_value(celsius_value, fahrenheit_value)
    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")


if __name__ == '__main__':
    main()
