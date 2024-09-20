import tkinter
from tkinter import ttk

root=tkinter.Tk()
root.title("Health App")
bg_color="#FFC0CB"
root.config(bg=bg_color)
def calculate():
    option=combo_ques.get()
    result_message =("")
    try:
        weight=float(entry_weight.get())
        height=float(entry_height.get())
        if(option=="BMI"):
            bmi=weight/(height**2)
            if(bmi<16.0):
              x="Underweight(not healthy)"
            elif(16<=bmi<16.9):
               x="Underweight(Moderate thinness)"   
            elif(16.9<=bmi<18.4):
               x="Underweight(Mild thinness)"   
            elif(18.4<=bmi<=24.9):
               x="Normal range"   
            elif(25<=bmi<29.9):
                x="Overweight (Pre-obese)"
            elif(29.9<=bmi<34.9):
                x="Obese(Class I)" 
            elif(34.9<=bmi<35.9):
                x="Obese(Class II)"
            else:
                x="Obese(Last stage)"  
            result_message=f"Your BMI is:{bmi:.2f}({x})"
            
        elif(option=="BMR"):
            age=int(entry_age.get())
            gender = combo_gender.get()    
            if(gender=="Male"):
                bmr=(10*weight)+(6.25*height*100)-(5*age)+5
            else:
                bmr=(10*weight)+(6.25*height*100)-(5*age)-161
            result_message=f"Your BMR is: {bmr:.2f} kcal/day"
        elif(option=="BSA"):
            bsa=(weight**0.425*height**0.725)*0.007184
            result_message=f"Your BSA is: {bsa:.2f} m²"
        elif(option=="PI"):
            pi=weight*1.6
            result_message=f"PI(Protein Intake):{pi:.2f}grams"
        elif(option=="LBM"):
            body_fat_percentage=float(entry_body_fat.get())
            lbm=weight*(1-(body_fat_percentage/100))
            result_message=f"Your Lean Body Mass is:{lbm:.2f} kg"
        else:
            result_message="Please select an option."
    except ValueError:
        result_message="Please enter valid numbers."

    result_box.delete(1.0,tkinter.END) 
    result_box.insert(tkinter.END,result_message)

label_name=tkinter.Label(root, text="Name:")
label_name.pack()
entry_name=tkinter.Entry(root)
entry_name.pack()

label_country=tkinter.Label(root, text="Country:")
label_country.pack()
entry_country= tkinter.Entry(root)
entry_country.pack()

label_weight=tkinter.Label(root, text="Weight(kg):")
label_weight.pack()
entry_weight=tkinter.Entry(root)
entry_weight.pack()

label_height=tkinter.Label(root, text="Height(m):")
label_height.pack()
entry_height=tkinter.Entry(root)
entry_height.pack()

label_age=tkinter.Label(root, text="Age (years):")
label_age.pack()
entry_age=tkinter.Entry(root)
entry_age.pack()

label_gender=tkinter.Label(root, text="Gender:")
label_gender.pack()
combo_gender=ttk.Combobox(root, values=["Male","Female"])
combo_gender.pack()

label_body_fat = tkinter.Label(root, text="Body Fat Percentage (%):")
label_body_fat.pack()
entry_body_fat =tkinter.Entry(root)
entry_body_fat.pack()

label_ques=tkinter.Label(root, text="What do you want to calculate?")
label_ques.pack()
combo_ques=ttk.Combobox(root, values=["BMI","BMR","BSA","PI","LBM"])
combo_ques.pack()

submit_button=tkinter.Button(root, text="Calculate", command=calculate)
submit_button.pack()

result_box=tkinter.Text(root, height=4, width=40)
result_box.pack()

root.mainloop()
