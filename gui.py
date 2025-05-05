# import tkinter as tk
#
# root = tk.Tk()
# root.title("Kalkulator Python")
# root.geometry("400x600")
#
# frame = tk.Frame(root, bg='#252525')
# frame.pack()
#
# def get_number():
#    print("Message", "Hey There! I hope you are doing well.")
#
# window = tk.Frame(frame, background='#253025', height=100, width=400)
# window.grid(row=0, columnspan=3)
# labelL = ""
# label = tk.Label(frame, bg="#253025", fg="white", font=("Arial", 12), text=labelL)
# label.grid(row=0, column=1)
#
# # TABLICA PRZYCISKÓW
#
# button = tk.Button(frame, text="7", font=("Arial", 16), background="#441fdb",  fg="white", bd=0, width=5, height=2, command=get_number )
# button.grid(row=1, column=0, pady=5, padx=5)
#
# button = tk.Button(frame, text="8", font=("Arial", 16), background="#441fdb",  fg="white", bd=0, width=5, height=2)
# button.grid(row=1, column=1, pady=5, padx=5)
#
# button = tk.Button(frame, text="9", font=("Arial", 16), background="#441fdb", fg="white", bd=0, width=5, height=2)
# button.grid(row=1, column=2, pady=5, padx=5)
#
# #
#
#
# button = tk.Button(frame, text="4", font=("Arial", 16), background="#441fdb",  fg="white", bd=0, width=5, height=2)
# button.grid(row=2, column=0, pady=5, padx=5)
#
# button = tk.Button(frame, text="5", font=("Arial", 16), background="#441fdb",  fg="white", bd=0, width=5, height=2)
# button.grid(row=2, column=1, pady=5, padx=5)
#
# button = tk.Button(frame, text="6", font=("Arial", 16), background="#441fdb", fg="white", bd=0, width=5, height=2)
# button.grid(row=2, column=2, pady=5, padx=5)
#
# #
#
# button = tk.Button(frame, text="1", font=("Arial", 16), background="#441fdb",  fg="white", bd=0, width=5, height=2)
# button.grid(row=3, column=0, pady=5, padx=5)
#
# button = tk.Button(frame, text="2", font=("Arial", 16), background="#441fdb",  fg="white", bd=0, width=5, height=2)
# button.grid(row=3, column=1, pady=5, padx=5)
#
# button = tk.Button(frame, text="3", font=("Arial", 16), background="#441fdb", fg="white", bd=0, width=5, height=2)
# button.grid(row=3, column=2, pady=5, padx=5)
#
#
#
#
# root.mainloop()