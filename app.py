def main():
    # 3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},

        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},

        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温は？
    total = 0
    size = len(weather_information)

    for information_dict in weather_information:
        total += information_dict["temperature"]

    weather_average = total / size

    print(f"全国の平均気温: {weather_average}")
    print()


    # Q2. 大阪府のすべての駅名を出力してね。
    print("大阪府の駅は")
    for information_dict in weather_information:
        if information_dict["prefecture"] == "大阪府":
            print(information_dict["station"])
    print()


    # Q3. 福岡県の平均気温は？
    total_fukuoka = 0
    size_fukuoka = 0

    for information_dict in weather_information:
        if information_dict["prefecture"] == "福岡県":
            total_fukuoka += information_dict["temperature"]
            size_fukuoka += 1

    average_fukuoka_temperature = total_fukuoka / size_fukuoka
    print(f"福岡の平均気温は: {average_fukuoka_temperature}")
    print()

    # 04. 気温が9度以上の地域の平均気温
    total_9up = 0
    size_9up = 0

    for information_dict in weather_information:
        if information_dict["temperature"] >= 9:
            total_9up += information_dict["temperature"]
            size_9up += 1

    average_9up_temperature = total_9up / size_9up
    print(f"気温が9度以上の地域の平均気温は: {average_9up_temperature}")
    print()

    # 05. 気温が8度以下の駅名
    total_8down = 0
    size_8down = 0

    input_temperature = int(input(f"気温が○度以下の駅は? (気温を入力してね):"))
    for information_dict in weather_information:
        if information_dict["temperature"] <= input_temperature:
            print(information_dict["station"])
    print()

if __name__ == "__main__":
    main()
