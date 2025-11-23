import numpy as np
denomination=np.array([2000,500,200,100])
notes=np.array([10,20,30,50])
# atm has 10 notes of 2000,20 notes of 500,30 notes of 200 and 50 notes of 100
def total_cash():
    '''retun toral cash available in atm'''
    return np.sum(denomination*notes)
def show_atm_status():
    print('\n====Atm status====')
    for d,n in zip(denomination,notes):
        print(f'{d}*{n} notes')
    print('Total cash:',total_cash())
    print('======================\n')
def withdraw(amount):
    '''withdraw money using numpy(from largest notes to smallest notes)'''
    global notes
    if amount>total_cash():
        print('Atm doesnt ahve enough cash, please enter valid amount')
        return
    # required notes
    required=np.zeros_like(notes)
    remaining_amount=amount
    for i in range(len(denomination)):
        note_value=denomination[i]
        max_notes_needed=remaining_amount//note_value
        notes_to_give=min(max_notes_needed,notes[i])
        required[i]=notes_to_give
        remaining_amount-=notes_to_give*note_value
    if remaining_amount!=0:
        print('cannot dispense the exact amount with avaliable notes')
        return
    # update atm notes
    notes-=required
    print('\n withdraw successfull, please collect your cash as below:')
    for d,r in zip(denomination,required):
        if r>0:
            print(f'{d}*{r}')
    print('remaning atm status:',total_cash())
def deposit(den,count):
        '''deposit notes into atm'''
        global notes
        index=np.where(denomination==den)[0]
        if len(index)==0:
            print('invalid denomination!')
            return
        notes[index]+=count
        print(f'deposited {count} notes of {den} successfully')
while True:
    print("\n===== ATM CASH MANAGEMENT =====")
    print("1. Show ATM Status")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Total Cash")
    print("5. Exit")
    choice=int(input("Enter your choice (1-5): "))
    if choice==1:
        show_atm_status()
    
    elif choice == 2:
        amt = int(input("Enter amount to withdraw: "))
        withdraw(amt)

    elif choice == 3:
        den = int(input("Enter denomination (2000/500/200/100): "))
        cnt = int(input("Enter number of notes: "))
        deposit(den, cnt)

    elif choice == 4:
        print("Total Cash in ATM:", total_cash())

    elif choice == 5:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice! Try again.")