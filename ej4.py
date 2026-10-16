def main():
    celsius = float(input("introduce la temperatura en celsius: "))

    fahrenheit = celsius * 9 / 5 + 32

    print(f"Los {celsius} ºC en ºF son: {fahrenheit}")

if __name__ == "__main__":
    main()