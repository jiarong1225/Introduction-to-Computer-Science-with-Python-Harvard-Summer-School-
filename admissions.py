# Make sure to import the admitted student data
import students
def generate_letter(student):
    with open("letter.txt","r") as g:
        letter=g.read()
        all_modified_letters = []
        for this_dict in student.admitted:
            name=this_dict["NAME"]
            content_modified=letter
            for i in this_dict.keys():
                content_modified=content_modified.replace(i,this_dict[i])
            save_letter(name,content_modified)
            all_modified_letters.append(content_modified)
    return all_modified_letters

    '''Generates and returns the letter for the given student.'''

def save_letter(student_name, letter_content):
    with open(f"{student_name}.txt", "x") as f:
        f.write(letter_content)
        f.close()


    '''Writes out the given letter to a file based on the student name.'''

def main():
    x=generate_letter(students)
    for i in x:
        print(i)
    # Generate and write out a letter for each admitted student.


if __name__ == "__main__":
    main()
