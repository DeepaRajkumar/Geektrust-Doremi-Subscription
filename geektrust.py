from sys import argv
from Constants import Constants as con
import Subscription as ss
import  Each_Subscription_detail as  ad
import Topup_rates as tp
import display_detail as dis
def get_input_into_command_and_value(input):
    values = []
    splited_text = input.split()

    command = splited_text[0]

    values = splited_text[1:]
    return command,values

def main():
    count, amount, topup_rate, =0,0,0
    list_topup,subscribe,category=[],[],[]
    date=00-00-000
    add_subscription = ad.Add_Subscription()
    # read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    for line in Lines:
        comment,value=get_input_into_command_and_value(line)
        if comment== con.START_SUBSCRIPTION:
            subscription=ss.Start_subscription()
            count,date=subscription.check_subscription(value[0])
        elif comment== con.ADD_SUBSCRIPTION:

            subscribe,category=add_subscription.subscription(value)

        elif comment == con.ADD_TOPUP:
            topup=tp.Top_up()
            topup_rate,list_topup=topup.Topup_details(value)

    amount = add_subscription.each_subscription_rate(subscribe)
    display=dis.displays()
   # print(count,date,amount,subscribe,category,topup_rate,list_topup)
    display.displays_detail(count,date,amount,
                            subscribe,category,
                            topup_rate,list_topup)


    
if __name__ == "__main__":
    main()