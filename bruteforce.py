from itertools import product

word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{}[]:;\"'<>,.?/|\\"

start = input("start num: ")
finish = input("finish num: ")

for passwd_length in range(int(start),int(finish)+1):
    admin_pass =product(word,repeat=passwd_length)
    for passwd_value_store in admin_pass:
        passwd=''.join(passwd_value_store)
        print(passwd)

        request_login_packet={
            'ID' : '',
            'PassWord' : passwd,
            'submit_button' : 'submit',
        }
print(passwd)
