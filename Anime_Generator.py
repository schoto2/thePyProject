import tkinter

root = tkinter.Tk()

homePage = tkinter.Frame(root, bg="black", height=500, width=500)
homePage.grid_propagate(False) #lock the home page and others are limited to this size
homePage.grid(row=0, column=0, sticky="nsew")
#if you fill any page with widgets that make it larger than this,
#that will set the new size for all pages


#add as many pages as you need
pageOne = tkinter.Frame(root, bg="blue")
pageOne.grid(row=0, column=0, sticky="nsew")
pageTwo = tkinter.Frame(root, bg="orange")
pageTwo.grid(row=0, column=0, sticky="nsew")
pageThree = tkinter.Frame(root, bg="red")
pageThree.grid(row=0, column=0, sticky="nsew")
pageFour = tkinter.Frame(root, bg="purple")
pageFour.grid(row=0, column=0, sticky="nsew")
pageFive = tkinter.Frame(root, bg="green")
pageFive.grid(row=0, column=0, sticky="nsew")
                    
homePage.tkraise() #brings the homepage to the top to start with (or which ever page you choose)

def showHome():
    homePage.tkraise()

def showPageOne():
    pageOne.tkraise()


def showPageTwo():
    pageTwo.tkraise()

def showPageThree():
    pageThree.tkraise()
    
def showPageFour():
    pageFour.tkraise()

def showPageFive():
    pageFive.tkraise()
    


    
#putting the widgets on and arranging the home page
goToTwo = tkinter.Button(homePage, text="Stragety", fg="red", command=showPageTwo)
goToTwo.grid(row=2, column=0, sticky="nsew")

goToOne = tkinter.Button(homePage, text="Power", fg="red", command=showPageOne)
goToOne.grid(row=0, column=0, sticky="nsew")





#putting the widgets on and arranging pageOne
goHome = tkinter.Button(pageOne, text="Pride", fg="brown", command=showPageThree)
goHome.grid(row=1, column=0, sticky="nsew")

goHome = tkinter.Button(pageOne, text="Training", fg="brown", command=showPageFour)
goHome.grid(row=2, column=0, sticky="nsew")

goHome = tkinter.Button(pageOne, text="Family", fg="brown", command=showPageFive)
goHome.grid(row=3, column=0, sticky="nsew")

goHome = tkinter.Button(pageOne, text="go home", fg="brown", command=showHome)
goHome.grid(row=4, column=0, sticky="nsew")




#putting the widgets on and arranging pageTwo
label1 = tkinter.Label(pageOne, text="What makes you gain power?")
label1.grid(row=0, column=0)





goHome = tkinter.Button(pageTwo, text="go to home", fg="brown", width=10, command=showHome)
goHome.grid(row=1, column=0)





root.mainloop()
