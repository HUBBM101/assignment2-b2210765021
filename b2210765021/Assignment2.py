
d=open("doctors_aid_inputs.txt","r", encoding='utf-8')
a=d.readlines()

f=open("doctors_aid_outputs.txt","w", encoding='utf-8')

liste=[]
names = []

def create(e):
    m=e[7:-2]
    words = m.split(",")
    name=words[0]

    if name not in names:
        liste.append(m.split(","))
        names.append(name)
        return "Patient {} is recorded.".format((e.split(",")[0]).split(" ")[1]) + "\n"
    else:
        return f"Patient {name} cannot be recorded due to duplication.\n"




def remove(name):
    for i, person_list in enumerate(liste):
        if person_list[0] == name:
            del liste[i]
            names.remove(name)


def probability(name):
    if name not in names:
        f.write(f"Probability for {name} cannot be calculated due to absence." + "\n")
    else:
        index = 0
        for i, person_list in enumerate(liste):
            if person_list[0] == name:
                index = i
                break
        incidence = eval(liste[index][3])  * 100_000
        accuracy = float(liste[index][1])
        s = incidence / (((100000 - incidence) * (1 -  accuracy)) + 50)
        f.write("{} has a probablity of %{:.2f}".format(name,  100 * round(s,4)) + " of " +  liste[index][2] + ".\n")
def recommendation(name):
    if name not in names:
        f.write(f"Recommendation for {name} cannot be calculated due to absence." + "\n")
        return
    index = 0
    for i, person_list in enumerate(liste):
        if person_list[0] == name:
            index = i
            break
    incidence = eval(liste[index][3]) * 100_000
    accuracy = float(liste[index][1])
    s = incidence / (((100000 - incidence) * (1 - accuracy)) + 50)
    if s>0.40:
        f.write(f"System suggests {name} to have the treatment." + "\n")
    else:
        f.write(f"System suggests {name} NOT to have the treatment." + "\n")

def list_patients():
    line1_list = "Patient Diagnosis Disease Disease Treatment Treatment".split()
    line2_list = "Name Accuracy Name Incidence Name Risk".split()
    #f.write("\t\t\t\t\t\t".join(line1_list) + "\n")
    #f.write("\t\t\t\t\t\t".join(line2_list)  + "\n")
    line_1 = '{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format(*line1_list)
    line_2 = '{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format(*line2_list)

    f.write(line_1 + "\n")
    f.write(line_2 + "\n")

    f.write("---------------------------------------------------------------------------------------------\n")
    for person_list in liste:
        #f.write("\t\t\t\t\t\t".join(person_list) + "\n")
        temp = person_list[1]
        person_list[1] = float(person_list[1]) * 100
        person_list[1] = "{:.2f}%".format(person_list[1])
        line_3 = '{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format(*person_list)
        person_list[1] = temp
        f.write(line_3 + "\n")
def read_inputs():
    for e in a:
        if "create" in e.split(",")[0]:
            f.write(create(e))

        elif "probability" in e:
            words_of_prob = e.split()
            name = words_of_prob[1]
            probability(name)
        elif "recommendation" in e:
            words_of_recom=e.split()
            name=words_of_recom[1]
            recommendation(name)

        elif "remove" in e:
            if e.split()[1] not in names:
                f.write(f"{e.split()[1]} cannot be removed due to absence." + "\n")
            else:
                name = e.split()[1]
                remove(name)
                f.write("Patient" + " " + e.split()[1] + " " + "is removed." + "\n")
        elif "list" in e:
            list_patients()

read_inputs()











