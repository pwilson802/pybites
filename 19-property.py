from datetime import datetime

NOW = datetime.now()

class Promo:
    def __init__(self, text, time):
        self.text = text
        self.time = time
    
    @property
    def expired(self):
        return self.time < NOW
        # if self.time < NOW:
        #     return True
        # else:
        #     return False
        
        
past_time = NOW - timedelta(seconds=3)
twitter_promo = Promo('twitter', past_time)

future_date = NOW + timedelta(days=1)
newsletter_promo = Promo('newsletter', future_date)
