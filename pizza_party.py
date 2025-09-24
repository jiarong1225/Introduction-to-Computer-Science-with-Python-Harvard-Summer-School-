
from pizza import Pizza

def main():
    appetizer = Pizza("Mushroom", 16, 10.50, 10)
    print(appetizer)

    dinner = Pizza("Anchovy & Pineapple", 20, 11.95, 8)
    print(dinner)

    # Demonstrate method usage
    print()
    print("Area per slice:")
    print(f"Appetizer: {appetizer.area_per_slice()} square inches")
    print(f"Dinner: {dinner.area_per_slice()} square inches")

    print()
    print("Cost per slice:")
    print(f"Appetizer: ${appetizer.cost_per_slice()}")
    print(f"Dinner: ${dinner.cost_per_slice()}")

    print()
    print(f"\nCost per square inch:")
    print(f"Appetizer: ${appetizer.cost_per_square_inch()}")
    print(f"Dinner: ${dinner.cost_per_square_inch()}")

if __name__ == "__main__":
    main()
