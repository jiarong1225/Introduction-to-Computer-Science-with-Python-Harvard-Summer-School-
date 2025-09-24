# Define your clock class here!
class Clock:
    def __init__(self,hour,minute):
        if hour>=24 or minute>=60:
            print("It is not valid!")
        else:
            self._hours=hour
            self._minutes=minute

    def __str__(self):
        if self._hours==12 and self._minutes==0:
            return f"12:00 PM"
        elif self._hours==0 and self._minutes==0:
            return f"12:00 AM"
        elif self._hours<=11:
            return f"{self._hours}:{self._minutes} AM"
        elif self._hours>=12:
            return f"{self._hours-12}:{self._minutes} PM"


def main():
    class_time = Clock(15, 15)
    print(class_time)  # Should output: 3:15 PM

    midnight = Clock(0, 0)
    print(midnight)  # Should output: 12:00 AM

    noon = Clock(12, 0)
    print(noon)  # Should output: 12:00 PM

    # This should raise a ValueError
    # invalid_time = Clock(24, 60)

if __name__ == "__main__":
    main()
