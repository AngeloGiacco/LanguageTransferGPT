with open("corpus/german.txt", "r", encoding="utf-8") as input_file, \
     open("corpus/german_modified.txt", "w", encoding="utf-8") as output_file:
    isTeacher = True
    startOfLesson = False
    prevIsTeacher = False
    for line in input_file:
        if line.strip() == "":
            if not startOfLesson:
                isTeacher = not isTeacher #teacher and student alternate on every new line in a lesson                
            continue 
        if line[:12] == "German Track":
            output_file.write(line)
            startOfLesson = True
            isTeacher = True
            prevIsTeacher = False
        else:
            startOfLesson = False
            if isTeacher:
                if prevIsTeacher:
                    output_file.write("   " + line)
                if not prevIsTeacher:
                    output_file.write("Teacher: " + line)
                    prevIsTeacher = True
            else:
                if prevIsTeacher:
                    output_file.write("Student: " + line)
                    prevIsTeacher = False 
                else:
                    output_file.write("   " + line)

print("Processing complete.")