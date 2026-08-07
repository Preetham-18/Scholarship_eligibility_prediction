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


print("\nSequential Covering Algorithm:")
sequential_covering(df)


