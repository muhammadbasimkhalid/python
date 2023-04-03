List=["Cyclosporiasis","cough","headache","typhoid","pneumonia"]
Medicine=[["Cinnarizine","cyclizine","promethazine","Hyoscine","haloperidol"],["Triaminic Cold and Cough","Robitussin Cough","Vicks 44 Cough and Cold","Mucinex","Robitussin Chest Congestion"],["Aspirin","Acetaminophen","paracetamol","Ibuprofen","Prochlorperazine"],["Fluoroquinolones","Cephalosporins","MacrolidesCarbapenems","ciprofloxacin"],["Fluoroquinolones","Macrolides","Azithromycin","Antibiotics","Lincosamide"]]
name=input("Enter your name:-")
disease=input("Hey "+name+" Enter the disease you are suffering with:-")
def cure(List,disease):
    a= 0
    for i in range (len(List)):
        if List[i]==disease:
            a= 1
            print("please take these medicines",Medicine[i])
            break
    if a==0:
        print("disease not found")
cure(List,disease)         
        

