from datetime import datetime, timedelta


def main():
    def display_current_datetime():
        current_date = datetime.now()
        print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

    display_current_datetime()

    def calculate_future_date():
        number_of_days = int (input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=number_of_days)
        print(f"Future date after {number_of_days} days will be:", future_date.strftime("%Y-%m-%d %H:%M:%S"))

    calculate_future_date()

if __name__ == "__main__":
    main()