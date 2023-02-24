import pandas as pd
import numpy as np

# Create df_teacher DataFrame
df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
    "married": [True, True, False, True],
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

# Create df_student DataFrame
df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino", "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
})

#python with specified fields :PART A
# filter teacher and school
df_teacher_filtered = df_teacher[(df_teacher["name"] == "Jurgen Klopp") & (df_teacher["school"] == "Liverpool High School") & (df_teacher["married"] == True)]

# filter students
df_students_filtered = df_student[df_student["teacher"] == "Jurgen Klopp"]
df_students_filtered = df_students_filtered[["name", "age", "height"]]

#LOCATE
output = {
    "teacher": {
        "name": df_teacher_filtered["name"].values[0],
        "married": df_teacher_filtered["married"].values[0],
        "school": df_teacher_filtered["school"].values[0]
    },
    "students": []
}

for _, row in df_students_filtered.iterrows():
    output["students"].append({
        "name": row["name"],
        "age": row["age"],
        "height": row["height"]
    })

# Convert To JSON
output_json = json.dumps(output)

print(output_json)



#PART B
