def remove_lowest(grade_list):
    removed_lowest = grade_list.copy()
    if len(grade_list) <= 1:
        return grade_list
    else:
        lowest = min(grade_list)
        for i in range(len(grade_list) -1, -1, -1):
            if grade_list[i] == lowest:
                removed_lowest.pop(i)
    return removed_lowest


def main():
    print(remove_lowest([23, 90, 47, 55, 88]))


if __name__ == "__main__":
    main()

