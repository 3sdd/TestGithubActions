import pytz

if __name__=="__main__":
    print("called")
    tz=pytz.timezone("Asia/Tokyo")
    print(tz)

    london = pytz.timezone('Europe/London')
    print(london)