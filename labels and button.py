import tkinter
from tkinter import ttk

root=tkinter.Tk()
root.title("Health App")
bg_color="#FFC0CB"
root.config(bg=bg_color)

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

submit_button=tkinter.Button(root, text="Calculate")
submit_button.pack()

result_box=tkinter.Text(root, height=4, width=40)
result_box.pack()

root.mainloop()
