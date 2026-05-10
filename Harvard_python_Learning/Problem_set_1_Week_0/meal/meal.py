def main():
    time = input("what time is it?: ")
    hours = convert(time)
    if 7 <=hours <=8:
        print("breakfast time")
    elif 12 <= hours <=13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    time = time.strip()

    if "a.m" in time:
        time = time.replace("a.m.", "")
        h, m = time.split(":")
        h, m = int(h), int(m)
        if h == 12:
            h = 0
        return h + m / 60
    elif "p.m" in time:
        time = time.replace("p.m.", "")
        h, m = time.split(":")
        h, m = int(h), int(m)
        if h != 12:
            h += 12
        return h + m / 60
    else:
        h, m = time.split(":")
        return int(h) + int(m) / 60

if __name__ == "__main__":
    main()
