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

        rule = " If CGPA >= " + str(min_cgpa) + " THEN Scholarship = Eligible"
        rules.append(rule)

        wrongly_covered = not_eligible_students[not_eligible_students["CGPA"] >= min_cgpa]

        print("\n Wrongly covered students:")
        print(wrongly_covered)

        print("\n Number of students wrongly covered:", len(wrongly_covered))

        rule2 = " If CGPA >= " + str(min_cgpa) + " AND Backlogs = 0 " " THEN Scholarship = Eligible"
        

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
                  

print("\nSequential Covering Algorithm:")
sequential_covering(df)


