import datetime

def get_current_time():
    now = datetime.datetime.now()
    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    return now

if __name__ == "__main__":
    get_current_time()
