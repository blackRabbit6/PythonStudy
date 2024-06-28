#전달값과 반환값
def deposit(balance, money): # 입금
    print("입금 완료되었습니다. 현재 잔액: {0}원".format(balance+money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액 >= 출금
        print("출금 완료되었습니다. 현재 잔액: {0}원".format(balance-money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액: {0}".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw_night(balance, 500)
commission, balance = withdraw_night(balance,500)
print("수수료 {0}원, 잔액: {1}원".format(commission, balance))