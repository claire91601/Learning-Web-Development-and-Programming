# Code Your Solution Here

import os # Imports the operating system module to use to access the files.

def calculate_average_grade(grades): # Defines a function to calculate the average grade
    return sum(grades) / len(grades) # Adds together all of the grades and then divides it by the number of grades(or the length of the list of grades). Then it "returns" it or stores the value for later use

def determine_letter_grade(average_grade): # Defines a functino to determine the letter grade
    if average_grade >= 90: # if the average grade is greater than or equal to 90.. 
        return "A" # Stores the letter grade for later use
    elif average_grade >= 80:
        return "B"
    elif average_grade >= 70:
        return "C"
    elif average_grade >= 60:
        return "D"
    else:
        return "F"

def create_gradebook(gradebook_path): # creates a function that processes the gradebook
    with open(gradebook_path, mode = 'r') as file: # Reads the chosen gradebook path
        gradebook = [line.split(',') for line in file.readlines()] # Separates the file by lines and reads the lines individually
    final_grades = [] # Puts the final grades into a list
    for student_row in gradebook[0:]: # Starts reading from the first row in the gradebook file
        student_name = student_row[0] # Defines the student name as the first item in the list
        grades = [int(grade) for grade in student_row[1:]] # Uses the items in the list starting from the second item to calculate the grades
        average_grade = calculate_average_grade(grades) # Calls the calculate_average_grades function, uses the grades listed, and stores the output in the average_grades value
        letter_grade = determine_letter_grade(average_grade) # Calls the determine_letter_grade function and uses the average grade that was calculated to store it in the letter_grade variable
        final_grades.append([student_name, average_grade, letter_grade]) # Adds the student name, average grade, and letter grade to the final_grades list.
    chosen_filename = input("Please enter a name for your .txt file:\n") # Allows the user to choose a name for their .txt file
    chosen_filename_txt = chosen_filename + ".txt" # Turns the filename into a .txt file without the user having to type in .txt
    output_filename = open(chosen_filename_txt, "w", newline = '') # This is what will open the new file
    
    with open(chosen_filename_txt, "w") as output_file: # This will be used to add the stuff into the file
        for student_grade in final_grades:
            student_grade_string = str(student_grade) # I added this at some point while writing the code but I'm not sure if it's needed anymore
            output_file.write(student_grade_string + "\n") # This will write out the lists of student names, average grades, and letter grades in lists that are separated by lines
    print(f"Final grades have been written to {output_filename}") # Tells the user where to find their file and the name of the file


folder = input("Enter a folder name:\n") # Allows the user to choose the "gradebooks" folder.

gradebook_choice = input("Enter the name of the gradebook file you would like to use:\n") # Allows the user to choose which gradebook text file they want to use.
gradebook_choice_txt = gradebook_choice + ".txt" # Converts the users choice into a text file that can be read by the program
filepath = os.path.join(folder, gradebook_choice_txt) # Creates a filepath using the folder and filename inputs.


if os.path.exists(filepath): # Checks to make sure that the gradebook chosen exists.
    print("The gradebook", filepath, "exists.") # If the gradebook chosen exists, this tells the user that it does.
    file_variable = open(filepath, "r") # Opens the gradebook for reading the file
    create_gradebook(filepath)
    
else: # If the gradebook chosen does not exist:
    print("The path", filepath, "does not exist.") # Tells the user that the gradebook does not exist.