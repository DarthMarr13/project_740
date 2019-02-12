SSN_white_list = [2312, 5436, 9012, 7777]

while True:

    user_ssn_number = input("Enter your SSN number in format 0000: ")
    #Length Checker
    if len(user_ssn_number) != 4:
        print ('Invalid SSN, please check the format (0000) !!!')
        continue
    if not user_ssn_number.isdigit():
        print ('Please enter SSN as number')
        continue
    if int(user_ssn_number) not in SSN_white_list:
        print ('Invalid SSN number')
        continue