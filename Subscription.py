import datetime

class Start_subscription:
    def check_subscription(self,start_subscription_date):
        self.count=0
        self.new_date_object=00-00-000

        try:
          self.new_date_object = datetime.datetime.strptime(start_subscription_date,"%d-%m-%Y")
         # self.checked_date=
        except:
            self.count+=1

        return self.count,self.new_date_object

