from Constants import Constants as con
class Add_Subscription:
    list_of_subscribe,list_category = [], []
    list_of_amount = []
    def subscription(self,values):

          self.add_subscribe = values[0]+" "+values[1]
          self.list_of_subscribe.append(self.add_subscribe)
          self.list_category.append(values[0])
          return self.list_of_subscribe,self.list_category
    def each_subscription_rate(self,subscribes):
           for each in subscribes:
               if each == con.MUSIC_FREE or each == con.MUSIC_PERSONAL or each ==con.MUSIC_PREMIUM:

                   self.list_of_amount.append(self.music_rate(each))
               elif each == con.VIDEO_FREE or each ==con.VIDEO_PERSONAL or each ==con.VIDEO_PREMIUM:

                   self.list_of_amount.append(self.video_rate(each))
               elif each == con.PODCAST_FREE or each ==con.PODCAST_PERSONAL or each == con.PODCAST_PREMIUM:
                   self.list_of_amount.append(self.podcast_rate(each))

           return self.list_of_amount
    def music_rate(self,each):
               if each == con.MUSIC_FREE:
                   return con.MUSIC_FREE_AMOUNT_PER_MONTH
               elif each == con.MUSIC_PERSONAL:
                   return con.MUSIC_PERSONAL_AMOUNT_PER_MONTH
               elif each == con.MUSIC_PREMIUM:
                   return con.MUSIC_PREMIUM_AMOUNT_PER_THREE_MONTH
    def video_rate(self,each):
        if each == con.VIDEO_FREE:
            return con.VIDEO_FREE_AMOUNT_PER_MONTH
        elif each == con.VIDEO_PERSONAL:

            return con.VIDEO_PERSONAL_AMOUNT_PER_MONTH
        elif each == con.VIDEO_PREMIUM:
            return con.VIDEO_PREMIUM_AMOUNT_PER_THREE_MONTH
    def podcast_rate(self,each):
        if each == con.PODCAST_FREE:
            return con.PODCAST_FREE_AMOUNT_PER_MONTH
        elif each == con.PODCAST_PERSONAL:
            return con.PODCAST_PERSONAL_AMOUNT_PER_MONTH
        elif each == con.PODCAST_PREMIUM:
            return con.PODCAST_PREMIUM_AMOUNT_PER_THREE_MONTH


if __name__=='__main__':
    add_sub=Add_Subscription()
    add_sub.subscription()
    add_sub.each_subscription_rate()