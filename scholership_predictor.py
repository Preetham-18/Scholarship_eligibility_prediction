import pandas as pd

df = pd.read_csv("dataset.csv")

# print(df)

# print("\nNumber of rows and columns:")
# print(df.shape)

# print("\nColumn Names:")
# print(df.columns)

# print("\nFirst 5 Records:")
# print(df.head())



def sequential_covering(df):
        eligible_students = df[df.Scholarship == "Eligible"]
        print("\nEligible Students:")
        print(eligible_students)  

        not_eligible_students = df[df.Scholarship == "Not Eligible"]       
        print("\nNot Eligible Students:")
        print(not_eligible_students)

        min_cgpa = eligible_students["CGPA"].min()

        rules = []

        rule = "If CGPA >= " + str(min_cgpa) + " THEN Scholarship = Eligible"
        rules.append(rule)

        wrongly_covered = not_eligible_students[not_eligible_students["CGPA"] >= min_cgpa]

        print("\n Wrongly covered students:")
        print(wrongly_covered)

        print("\n Number of students wrongly covered:", len(wrongly_covered))

        rule2 = "If CGPA >= " + str(min_cgpa) + " AND Backlogs = 0 " " THEN Scholarship = Eligible"
        

        wrongly_covered2 = not_eligible_students[
                (not_eligible_students["CGPA"] >= min_cgpa) &
                (not_eligible_students["Backlogs"] == 0)]

        print("\n Wrongly covered by rule2:")
        print(wrongly_covered2)

        print("\n Wrongly covered students by rule2:", len(wrongly_covered2))


        if len(wrongly_covered2) < len(wrongly_covered):
                rules[0] = rule2
        else:
                rules[0] = rule

        print("\n Selected Rule:")
        print(rules[0])

        selected_rule = rules[0]
        
        if "Backlogs = 0" in selected_rule:
                covered_students = eligible_students[
                (eligible_students["CGPA"] >= min_cgpa) &
                (eligible_students["Backlogs"] == 0)
        ]
        else:
             covered_students = eligible_students[
             eligible_students["CGPA"] >= min_cgpa
    ]

        print("\n Students covrered by the selected rule:")
        print(covered_students)

        print("\n Number of covered students:", len(covered_students))

        if len(covered_students) == len(eligible_students):
                print("All eligible students are covered.")
                print("No more rules are required.")

        print("\n Learned rules:")
        for rule in rules:
                print(rule)

        return min_cgpa, selected_rule
                  

# print("\nSequential Covering Algorithm:")
# min_cgpa, selected_rule = sequential_covering(df)


def predict_scholarship(cgpa, backlogs, min_cgpa, selected_rule):

        if "Backlogs = 0" in selected_rule:

                if cgpa >= min_cgpa and backlogs == 0:
                         return "Eligible"
                else:
                        return "Not eligible" 
        else:
                if cgpa >= min_cgpa:
                        return "Eligible"
                else:
                        return "Not eligible"




# cgpa = float(input("Enter your cgpa:"))
# backlogs = int(input("Enter your number of backlogs:"))

# result = predict_scholarship(cgpa, backlogs, min_cgpa, selected_rule)
# print("Scholarship:", result)


def main():
    print("\n========================================")
    print("   SCHOLARSHIP RULE LEARNING SYSTEM")
    print("========================================")

    min_cgpa = None
    selected_rule = None

    while True:
        print("\n1. Learn Scholarship Rules")
        print("2. Predict Scholarship")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nLearned Scholarship Rule:")
            min_cgpa, selected_rule = sequential_covering(df)

        elif choice == "2":

            if selected_rule is None:
                print("\nPlease learn the scholarship rules first.")
            else:
                cgpa = float(input("Enter your CGPA: "))
                backlogs = int(input("Enter your number of backlogs: "))

                result = predict_scholarship(
                    cgpa, backlogs, min_cgpa, selected_rule
                )

                print("Scholarship:", result)

        elif choice == "3":
            print("Thank you for using Scholarship Rule Learning System.")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

main()