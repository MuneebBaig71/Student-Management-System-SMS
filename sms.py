import pandas as pd
print("Welcome to the student management system")

name:str = input("Enter your name: ")
Roll_no:str = input("Enter your Roll no: ")

print(f"Hi {name}, your Roll no is {Roll_no}")

def subjects()->tuple[str,str,str]:
    sub1 = "maths"
    sub2 = "english"
    sub3 = "computer science"
    return sub1, sub2, sub3

results:list = []

def marks()->tuple[int,int,int]:
    while True:
        sub1, sub2, sub3 = map(int, input("Enter your marks for all three subjects: ").split())
        if all(0 <= mark <= 100 for mark in [sub1, sub2, sub3]):
                return sub1, sub2, sub3
        else:
                print("Please enter valid marks (0-100)")
    
    
available_subjects:tuple[str,str,str] = subjects()
print("Available subjects are: " ,",".join(available_subjects))

again = "y"
while again.lower() == "y":
       
        sub1, sub2, sub3 = marks()

        if sub1 >= 40:
                print("Passed")
                print(f"Maths marks {sub1}")
        else:
                print("Fail in Maths")

        if sub2 >= 40:
                print("Passed")
                print(f"English marks {sub2}")
        else:
                print("Fail in English")

        if sub3 >= 40:
                print("Passed")
                print(f"Computer Science marks {sub3}")
        else:
                print("Fail in Computer Science")

        print(f"Total marks: {sub1 + sub2 + sub3}")
        percentage = (sub1 + sub2 + sub3) / 300 * 100
        print(f"Percentage: {percentage:.2f}%")

        
        results.append({
        'Subject': available_subjects,
        'Marks': [sub1, sub2, sub3],
        'Names': [name]* len(available_subjects)
         })

        again = input("Would you like to enter again? (y/n): ")
        if again.lower() == "n":
                break
all_subjects = []
all_marks = []
all_names = []

for result in results:
    all_subjects.extend(result['Subject'])
    all_marks.extend(result['Marks'])
    all_names.extend(result['Names'])
    

if len(all_names) == len(all_subjects) == len(all_marks):
    df = pd.DataFrame({
        'Names': all_names,
        'Subject': all_subjects,
        'Marks': all_marks
    })

    try:
        df.to_excel('results.xlsx', index=False)
        print("Results have been saved to 'results.xlsx'.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
else:
    print("Error: All arrays must be of the same length. Please check your data.")
    df = None  # Ensure df is defined even if not used

# Ensure df exists before trying to use it
if df is not None:
    # (Optional) Further processing with df can go here
    pass

