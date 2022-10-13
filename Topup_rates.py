from Constants import Constants as con
class Top_up:
    list_device = []
    def Topup_details(self,top_detail):

        self.list_device.append(top_detail[0])
        self.topup_rate = 0
        if top_detail[0] == con.FOUR_DEVICE:
            self.topup_rate = con.FOUR_DEVICE_AMOUNT_PER_MONTH * int(top_detail[1])
        elif top_detail[0] == con.TEN_DEVICE:
            self.topup_rate = con.TEN_DEVICE_AMOUNT_PER_MONTH * int(top_detail[1])
        return self.topup_rate,self.list_device