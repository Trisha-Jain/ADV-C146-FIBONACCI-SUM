from tkinter import*

root=Tk()

root.title("Fibonacci")
root.geometry ("400x400")

entry_no = Entry(root)

label = Label(root,text="Fibonacci Series:  ")
label2 = Label(root,text="Fibonacci Sum ")

def Fibonacci():
    
    input_no = int(entry_no.get())
    first_no = 0
    second_no = 1
    sum = 0
    sum2 = 0
    counter = 1
    
    while(counter <= input_no):
        label["text"] +=str(sum) + " "
        label2["text"] = " Fibonacci sum :" + str(sum2)
        counter = counter + 1
        first_no = second_no
        second_no = sum 
        sum = first_no + second_no
        sum2= sum2 + sum
             
        
btn = Button(root, text="Show Fibonacci Series ", command=Fibonacci)

btn.pack()
entry_no.pack()
label.pack()
label2.pack()



root.mainloop()

