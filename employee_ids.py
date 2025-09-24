import csv

def main():
    # Modify this code to generate employee ids and print a csv table
    # as described in the problem set.
    with open("employees.csv", "r") as file:
        employees = list(csv.DictReader(file))
        full_name_dict = {}
        print("Id,ManagerId,LastName,FirstName")
        for n in range(len(employees)):
            Lastname = employees[n]['LastName']
            Firstname = employees[n]['FirstName']
            full_name = f"{Firstname} {Lastname}"
            full_name_dict[full_name] = n+1
        for m in range(len(employees)):
            Lastname_2 = employees[m]['LastName']
            Firstname_2 = employees[m]['FirstName']
            full_name_2 = f"{Firstname_2} {Lastname_2}"
            Id = int(full_name_dict[full_name_2])
            manager_full_name = employees[m]['Manager']
            print(f"{Id},",end='')
            ManagerId = full_name_dict.get(manager_full_name)
            if ManagerId == None:
                print(f",{Lastname_2},{Firstname_2}")
            else:
                print(f"{ManagerId},{Lastname_2},{Firstname_2}")


if __name__ == "__main__":
    main()



