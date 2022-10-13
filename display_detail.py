from Constants import Constants as con
from datetime import timedelta
class displays:
    def displays_detail(self,count,dates,amount,subscribe,category,topup_rate,list_topup):
        if len(list_topup) >= con.TWO :
            print("ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY")
            print("ADD_TOPUP_FAILED DUPLICATE_TOPUP")
            self.new_date=dates + timedelta(days=con.TWENTY_ONE)
            self.new_date=self.only_date(self.new_date)
            print("RENEWAL_REMINDER",category[0],self.new_date)
            print("RENEWAL_AMOUNT",con.MUSIC_PERSONAL_AMOUNT_PER_MONTH + con.TEN_DEVICE_AMOUNT_PER_MONTH)
        elif  count==1:
            print("INVALID_DATE")
            print("ADD_SUBSCRIPTION_FAILED INVALID_DATE\nADD_SUBSCRIPTION_FAILED INVALID_DATE\nADD_TOPUP_FAILED INVALID_DATE\nSUBSCRIPTIONS_NOT_FOUND")

        elif con.MUSIC_PREMIUM in subscribe and con.VIDEO_PREMIUM in subscribe :
            self.music_video_premium(subscribe,category,dates)
            self.total_amount(amount,topup_rate)

        elif con.MUSIC_PREMIUM in subscribe:
            self.music_with_premium(subscribe,category,dates)
            self.total_amount(amount, topup_rate)

        elif con.MUSIC_PERSONAL in subscribe:
            self.music_without_premium(subscribe, category, dates)
            self.total_amount(amount, topup_rate)



    def music_video_premium(self,subscribe,category,dates):
        for each,cat in zip(subscribe,category):
            if each==con.MUSIC_PREMIUM or each==con.VIDEO_PREMIUM :
                self.new_date=dates + timedelta(days=con.EIGHTY_TWO)
                self.new_date = self.only_date(self.new_date)
            else:
                self.new_date = dates + timedelta(days=con.TWENTY_ONE)
                self.new_date = self.only_date(self.new_date)
            print("RENEWAL_REMINDER",cat,self.new_date)

    def music_with_premium(self,subscribe,category,dates):
        for each,cat in zip(subscribe,category):
            if each==con.MUSIC_PREMIUM :
                self.new_date=dates + timedelta(days=con.Eighty_ONE)
                self.new_date = self.only_date(self.new_date)
            else:
                self.new_date = dates + timedelta(days=con.TWENTY_ONE)
                self.new_date = self.only_date(self.new_date)
            print("RENEWAL_REMINDER",cat,self.new_date)
    def music_without_premium(self,subscribe,category,dates):
        for each,cat in zip(subscribe,category):
            if each == con.MUSIC_PERSONAL:
                self.new_date=dates + timedelta(days=con.EIGTHEEN)
                self.new_date = self.only_date(self.new_date)
            elif each==con.VIDEO_PREMIUM:
                self.new_date = dates + timedelta(days=con.SEVENTY_NINE)
                self.new_date = self.only_date(self.new_date)
            else:
                self.new_date = dates + timedelta(days=con.EIGTHEEN)
                self.new_date = self.only_date(self.new_date)
            print("RENEWAL_REMINDER",cat,self.new_date)
    def total_amount(self,amount,topup_rates):
        self.amounts=0
        for amt in amount:
            self.amounts+=amt
        self.total_amt=self.amounts +topup_rates
        print("RENEWAL_AMOUNT",self.total_amt)
    def only_date(self,dates):
        return dates.strftime("%d-%m-%Y")
if __name__=='__main__':
    ds=displays()