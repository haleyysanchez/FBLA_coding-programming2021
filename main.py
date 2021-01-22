"""
Documentation done in pydoc format.
"""

# technologies used include sqlite3 and Tkinter
import sqlite3
from tkinter import *
from datetime import date
from tkinter import ttk
from tkinter import messagebox
import random

# connects/creates the database for this project and adds/updates it in this directory
conn = sqlite3.connect('quiz.db')

c = conn.cursor()

# # The code below only needs to be executed once to avoid the creation of multiple tables with the same name
# c.execute("""CREATE TABLE questions (
#             index_num integer,
#             question text,
#             fillInBlank integer,
#             multipleChoice integer,
#             tf integer,
#             dropdown integer,
#             answer text
#              )""")


# c.execute("INSERT INTO questions VALUES (0,'What does FBLA stand for?',1,0,0,0, 'Future Business Leaders of America')")
# c.execute("INSERT INTO questions VALUES (1,'FBLA stands for Future Business Leaders of America',0,0,1,0, 'True')")
# c.execute("INSERT INTO questions VALUES (2,'What kind of attire is acceptable for FBLA activities?',0,0,0,1, 'Business Attire, Casual Clothes, Lounge Wear, Black Tie')")
# c.execute("INSERT INTO questions VALUES (3,'What kind of attire is acceptable for FBLA activities?',0,1,0,0, 'Business Attire, Casual Clothes, Lounge Wear, Black Tie')")

# c.execute("INSERT INTO questions VALUES (4,'What are the official colors of FBLA?',0,1,0,0, 'Blue and Gold, Yellow and Red, Black and Blue, Red and Green')")
# c.execute("INSERT INTO questions VALUES (5,'The FBLA creed contains how many stanzas?',0,1,0,0, '7, 6, 8, 4')")
# c.execute("INSERT INTO questions VALUES (6,'In the officer installation ceremony what color candle represents the chapter in its entirety?',0,1,0,0, 'White, Blue, Gold, Red')")
# c.execute("INSERT INTO questions VALUES (7,'What color of candle symbolizes the office of the president?',0,1,0,0, 'Red, Blue, Gold, White')")
# c.execute("INSERT INTO questions VALUES (8,'The first FBLA chapter was chartered where?',0,1,0,0, 'Johnson City Tennessee, Tallahassee Florida, Raleigh North Carolina, Atlanta Georgia')")
# c.execute("INSERT INTO questions VALUES (9,'What date was the first FBLA chapter chartered?',0,1,0,0, 'February 3rd 1942, February 4th 1942, December 11th 1964, December 10th 1964')")
# c.execute("INSERT INTO questions VALUES (10,'How many team events are there in FBLA-Middle Level Junior High district competitive events?',0,1,0,0, '4, 5, 3, 6')")
# c.execute("INSERT INTO questions VALUES (11,'How many divisions of FBLA-PBL are there?',0,1,0,0, '4, 5, 3, 6')")
# c.execute("INSERT INTO questions VALUES (12,'How many goals does FBLA-Middle have?',0,1,0,0, '8, 7, 6, 5')")
# c.execute("INSERT INTO questions VALUES (13,'What was the first state to have a FBLA state chapter?',0,1,0,0, 'Iowa, Arkansas, Indiana, Ohio')")
# c.execute("INSERT INTO questions VALUES (14,'In what year was the FBLA-PBL Alumni Division approved?',0,1,0,0, '1979, 1980, 1981, 1982')")

# c.execute("INSERT INTO questions VALUES (15,'What year was the first state FBLA chapter chartered?',0,0,0,1, '1947, 1964, 1847, 1864')")
# c.execute("INSERT INTO questions VALUES (16,'Who is the founder of FBLA?',0,0,0,1, 'Hamden L. Forkner, Troy Aikman, Patricia Nixon, Jillian Perry')")
# c.execute("INSERT INTO questions VALUES (17,'In what year was Phi Beta Lambda created?',0,0,0,1, '1958, 1959, 1858, 1859')")
# c.execute("INSERT INTO questions VALUES (18,'In what year was the Professional Division created?',0,0,0,1, '1989, 1990, 1991, 1992')")
# c.execute("INSERT INTO questions VALUES (19,'Who was the first executive director of FBLA-PBL?',0,0,0,1, 'Dr. Edward Miller, Alexander T. Graham, Patricia Nixon, Elena Daly')")
# c.execute("INSERT INTO questions VALUES (20,'Who is the current executive director of FBLA-PBL?',0,0,0,1, 'Alexander T. Graham, Dr. Edward Miller, Patricia Nixon, Elena Daly')")
# c.execute("INSERT INTO questions VALUES (21,'Who was the executive director of FBLA-PBL in 1997?',0,0,0,1, 'Jean Buckley, Dr. Edward Miller, Alexander T. Graham, Elena Daly')")
# c.execute("INSERT INTO questions VALUES (22,'Which officer presides over and conducts meetings according to Parliamentary Procedure?',0,0,0,1, 'President, Vice-President, Secretary, Historian')")

# c.execute("INSERT INTO questions VALUES (23,'The National FBLA-PBL Center is located in Reston Virgina',0,0,1,0, 'True')")
# c.execute("INSERT INTO questions VALUES (24,'The National FBLA-PBL Center is located in Blacksburg Virgina',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (25,'The National FBLA-PBL Center is located in Tallahassee Florida',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (26,'The founder of FBLA is Hamden L. Forkner',0,0,1,0, 'True')")
# c.execute("INSERT INTO questions VALUES (27,'Troy Aikman was an FBLA member',0,0,1,0, 'True')")
# c.execute("INSERT INTO questions VALUES (28,'Patricia Nixon was an FBLA member',0,0,1,0, 'True')")
# c.execute("INSERT INTO questions VALUES (29,'There is an eagle on the FBLA emblem',0,0,1,0, 'True')")
# c.execute("INSERT INTO questions VALUES (30,'There is a dove on the FBLA emblem',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (31,'There is a dolphin on the FBLA emblem',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (32,'There is a turtle on the FBLA emblem',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (33,'There is a horse on the FBLA emblem',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (34,'FBLA-PBL Inc. is primarily funded through membership dues',0,0,1,0, 'True')")
# c.execute("INSERT INTO questions VALUES (35,'FBLA-PBL Inc. is primarily funded through donations',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (36,'Iowa was the first state to have a FBLA state chapter',0,0,1,0, 'True')")
# c.execute("INSERT INTO questions VALUES (37,'Arkansas was the first state to have a FBLA state chapter',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (38,'Indiana was the first state to have a FBLA state chapter',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (39,'Ohio was the first state to have a FBLA state chapter',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (40,'2016 was the year that FBLA-PBL celebrated 75 years',0,0,1,0, 'True')")
# c.execute("INSERT INTO questions VALUES (41,'2015 was the year that FBLA-PBL celebrated 75 years',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (42,'2014 was the year that FBLA-PBL celebrated 75 years',0,0,1,0, 'False')")
# c.execute("INSERT INTO questions VALUES (43,'2017 was the year that FBLA-PBL celebrated 75 years',0,0,1,0, 'False')")

# c.execute("INSERT INTO questions VALUES (44,'In what year was the groundbreaking ceremony for the National Center held?',1,0,0,0, '1990')")
# c.execute("INSERT INTO questions VALUES (45,'What symbol on the emblem denotes our belief in democracy and liberty?',1,0,0,0, 'Eagle')")
# c.execute("INSERT INTO questions VALUES (46,'What year did FBLA-PBL celebrate 75 years?',1,0,0,0, '2016')")
# c.execute("INSERT INTO questions VALUES (47,'What body is the policy making body for national FBLA-PBL Inc.?',1,0,0,0, 'National Board of Directors')")
# c.execute("INSERT INTO questions VALUES (48,'What do the initials NBEA stand for?',1,0,0,0, 'National Business Education Association')")
# c.execute("INSERT INTO questions VALUES (49,'What do the initials USDE stand for?',1,0,0,0, 'United States Department of Education')")
# c.execute("INSERT INTO questions VALUES (50,'What was the first state to have a FBLA state chapter?',1,0,0,0, 'Iowa')")

# conn.commit() # saves the changes made to the database

# c.execute("DROP TABLE questions") # SQL command that drops/gets rid of the table named questions
# conn.commit() # saves the changes made to the database

# Creates the main/landing Toplevel page
root = Tk()
root.geometry("1000x1000")

# The next 2 lines are good to run when wanting to verify that the functions are calling and reading the right attributes. (Great for debugging)
# c.execute("SELECT * FROM questions") # SQL command to get all of the values in the questions database
# print(c.fetchall()) # prints out all the question's information in the database to the console/terminal

def open_help_nav():
    """
        This function generates a message box to display the help/navigation information to the user.
    """
    msg = """Help/Navigation Information:
    
    - Click on the button that says 'Generate Random 5 Question Quiz' if you would like to have a 5 randomly generated question quiz on FBLA.
    
    - Click on the button that says 'See Question Bank with Answers' to have a new window pop up with a list of all the FBLA questions available in this program.
    """
    messagebox.showinfo("Help/Navigation", msg) # creates a messagebox that appears on top of the screen

def open_help_nav_quiz():
    """
        This function generates a message box to display the help/navigation information to the user on the quiz window.
    """
    msg = """Help/Navigation Information:
    
    - This window has your 5 question, randomly generated quiz.

    - Once you click submit, your results will appear on the screen.

    - If you would like to take another quiz, close this window by clicking on the X in the top left of your window and then cliick on the 'Generate Random 5 Question Quiz' button found on the landing page. A new window will appear with a new randomly generated quiz.
    """
    messagebox.showinfo("Help/Navigation", msg) # creates a messagebox that appears on top of the screen

def open_help_nav_all():
    """
        This function generates a message box to display the help/navigation information to the user on the window showing the user all of the questions in the database.
    """
    msg = """Help/Navigation Information:
    
    - On this page is a list of all the questions in the database associated with this program.

    - Scroll to see all of the 50+ questions.
    
    - Click on the X at the top left corner of your screen to close this window and return to the main window.
    """
    messagebox.showinfo("Help/Navigation", msg) # creates a messagebox that appears on top of the screen

def get_random_question(index):
    """
        This function returns a question's information based on the given parameter.
        Parameters:
            index (int): The index of the question to get from the database.
        Returns:
            (list): The string that has the question's information is split by ', ' and it's values are stored in this list.
    """
    c.execute("SELECT * FROM questions WHERE index_num=:index_num", {'index_num': index}) # SQL command to access the question in the database that has the given index
    return str(c.fetchone())[1:-1].split(', ') 

def add_question_to_window(window, question):
    """
        This function adds a question's information to the window given through the parameters.
        Parameters:
            window (Tkinter.Toplevel object): The Toplevel that the questions will be added to.
            question (list): Contains all of the question's information.
        Returns:
            (int or str, Tkinter.Toplevel.entry object or int or str): The first value is the correct answer to the question. The second value is the variable or widget where the answer the user gave can be accessed.
    """
    title1 = Label(window, text=question[1].strip("'"))
    title1.pack()

    # this conditional adds the question's information and associated widgets based on the values from question (the parameter passed)
    if question[2] == '1':
        # fillInBlank
        entry = Entry(window)
        entry.pack()
        return (question[6].strip("'").strip('"'), entry)
    elif question[3] == '1':
        # multipleChoice
        var1 = IntVar()
        Radiobutton(window, text=question[6].strip("'").strip('"'), variable=var1, value=1).pack()
        Radiobutton(window, text=question[7].strip("'").strip('"'), variable=var1, value=2).pack()
        Radiobutton(window, text=question[8].strip("'").strip('"'), variable=var1, value=3).pack()
        Radiobutton(window, text=question[9].strip("'").strip('"'), variable=var1, value=4).pack()
        return (1, var1)
    elif question[4] == '1':
        # tf
        var2 = IntVar()
        Radiobutton(window, text="True", variable=var2, value=1).pack()
        Radiobutton(window, text="False", variable=var2, value=2).pack()
        if question[-1].strip("'").strip('"') == 'True':
            return (1, var2)
        else:
            return (2, var2)
    else:
        # dropdown
        var3 = StringVar(window)
        var3.set("Click Here to See Options")
        dd = OptionMenu(window, var3, question[6].strip("'").strip('"'), question[7].strip("'").strip('"'), question[8].strip("'").strip('"'), question[9].strip("'").strip('"'))
        dd.pack()
        return (question[6].strip("'").strip('"'), var3)

def open_quiz():
    """
        This function creates a new Toplevel and gets the 5 random questions from the databse populated onto the window.
    """
    window = Toplevel()
    window.geometry("1000x1000")
    window.title('FBLA 5 Random Question Quiz')
    title1 = Label(window, text='FBLA 5 Random Question Quiz')
    title1.pack()

    Button(window, text='Help/Navigation', fg="blue", command=open_help_nav_quiz).place(relx=.02, rely=.02, anchor = NW)

    questions_answers = []
    indexes_left = list(range(51))
    # Randomly generates 5 indexes and updates indexes_left accordingly so that there are no repeated questions
    for x in range(5):
        index = random.randint(0,len(indexes_left)-1)
        questions_answers.append(add_question_to_window(window, get_random_question(indexes_left[index])))
        print(indexes_left[index])
        indexes_left.pop(index)
        
    indexes_left = list(range(51))

    def get_results():
        """
        This function checks to see if the user answered the questions correctly and prints the results to the quiz window.
        """
        score = 0
        index = 0
        alert = False
        results_to_print = ['1. ', '2. ', '3. ', '4. ', '5. ']
        print(questions_answers)
        for x in questions_answers:
            print(x[1].get())
            if str(x[0]).lower() == str(x[1].get()).lower():
                results_to_print[index] = results_to_print[index] + 'Correct'
                score += 1
                index += 1
            else:
                results_to_print[index] = results_to_print[index] + 'Incorrect'
                index += 1
            if str(x[1].get()).lower() == '' or str(x[1].get()).lower() == ' ' or str(x[1].get()).lower() == '0' or str(x[1].get()) == 'Click Here to See Options':
                alert = True
        if alert:
            # alerts the user if they did not answer all of the 5 questions
            messagebox.showinfo("Missing Answer", """You have not answered all of the questions. There is at least one missing field. Please fill in all fields next time.""")
        for i in results_to_print:
            title = Label(window, text=i)
            title.pack()
        title1 = Label(window, text='Your Score: '+str(score))
        title1.pack()

    button1 = Button(window, text='Submit Quiz and See Results', fg="blue", command=get_results)
    button1.pack()

def open_see_all_questions():
    """
        This function creates a new Toplevel and places a Treeview on the window with all of the questions from the database.
    """
    window = Toplevel()
    window.geometry("1000x1000")
    window.title('Program Question Bank with Answers')
    title1 = Label(window, text='Program Question Bank with Answers')
    title1.pack()

    tree = ttk.Treeview(window)
    # the line of code below hides the first column from the tree view
    tree['show'] = 'headings'
    tree["columns"] = ("1", "2", "3")
    tree.column("1", width=595)
    tree.column("2", width=255)
    tree.column("3", width=105)
    tree.heading("1", text="Question")
    tree.heading("2", text="Answer")
    tree.heading("3", text="Question Type")

    # populates the Treeview widget with the information from the quiz database
    c.execute("SELECT * FROM questions")
    objs = c.fetchall()
    q_type = ''
    for obj in objs:
        str(obj)[1:-1].split(', ')
        if int(obj[2]) == 1:
            q_type = 'Fill in the Blank'
        elif int(obj[3]) == 1:
            q_type = 'Multiple Choice'
        elif int(obj[4]) == 1:
            q_type = 'True or False'
        else:
            q_type = 'Drop Down'

        answer = (obj[6]).split(', ')[0]
        tree.insert("", 0, text="Line 1", values=(obj[1], answer, q_type))
    
    tree.pack()
    button = Button(window, text='Help/Navigation', fg="blue", command=open_help_nav_all)
    button.pack()


root.title('FBLA Quiz Generator')
title = Label(root, text='FBLA Quiz Generator')
title.pack()

# fbla logo added on home/landing page
photo = PhotoImage(file="FBLA_logo.png")
panel = Label(root, image=photo)
panel.pack()

info = Label(root, text="This application has access to a database with over 50 questions about FBLA.\n It can generate 5 question quizzes by randomly choosing questions from the database,\ninform the user which questions they got correct and generate a report based on the quiz results.")
info.pack()
button1 = Button(root, text='Generate Random 5 Question Quiz', fg="blue", command=open_quiz)
button1.pack()
button2 = Button(root, text='See Question Bank with Answers', fg="blue", command=open_see_all_questions)
button2.pack()
button3 = Button(root, text='Help/Navigation', fg="blue", command=open_help_nav)
button3.pack()

root.mainloop()

# good practice to close the database once finished
conn.close()
