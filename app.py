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

    # for dict_number in range(0, len(weather_information)-1):
    for information_dict in weather_information:
        total += information_dict["temperature"]

    size = len(weather_information)

    weather_average = total / size

    print(f"全国の平均気温: {weather_average}")
    print("\n")


    # Q2. 大阪府のすべての駅名を出力してね。
    print("大阪府の駅は")
    for dict_number in range(0, len(weather_information)-1):
        information_dict = weather_information[dict_number]
        if information_dict["prefecture"] == "大阪府":
            print(information_dict["station"])
    print("\n")


    # Q3. 福岡県の平均気温は？
    total_fukuoka = 0
    size_fukuoka = 0

    for dict_number in weather_information:
        if dict_number["prefecture"] == "福岡県":
            total_fukuoka += information_dict["temperature"]
            size_fukuoka += 1

    average_fukuoka_temperature = total_fukuoka / size_fukuoka
    print(f"福岡の平均気温は: {average_fukuoka_temperature}")


if __name__ == "__main__":
    main()
