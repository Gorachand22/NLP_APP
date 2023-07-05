from tkinter import *
from tkinter import messagebox
from myapi import API
from mydb import Database

class NLPApp:
    def __init__(self):
        # Create db object
        self.dob=Database()

        self.apio = API()


        # login ka gui load karna
        self.root = Tk() 
        self.root.title('NLPApp') # title for the Website
        self.root.iconbitmap('resources/favicon.ico') # icon for the website
        self.root.geometry('350x600') # size (width x Height) of the website
        self.root.configure(bg = '#1C2833') # background color for the website

        self.login_gui()
        self.root.mainloop() # visualize the website as much you want
    
    def login_gui(self):
        self.clear()
        
        heading = Label(self.root, text = 'NLPApp', bg = '#1C2833', fg = 'white') # display software name with Label class
        heading.pack(pady=(30,30)) # geometry manager, put your heading components on  the ui (Like Gauri Khan)
        heading.configure(font = ('verdana', 24, 'bold')) # font size set
#-------------------------------------------------------------------------------------------------------------------------------- 
        label1 = Label(self.root, text = 'Enter Email')
        label1.pack(pady=(10,10))
        label1.configure(font = ('verdana', 10)) # font size set
#-------------------------------------------------------------------------------------------------------------------------------- 
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10), ipady = 4) #ipady use for set height
#--------------------------------------------------------------------------------------------------------------------------------         
        label2 = Label(self.root, text = 'Enter Password')
        label2.pack(pady=(10,10))
        label2.configure(font = ('verdana', 10)) # font size set

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5,10), ipady = 4) #ipady use for set height
#-------------------------------------------------------------------------------------------------------------------------------- 
        login_btn = Button(self.root, text = "Login", width = 30, height= 2, command= self.perform_login) # Button class for login click
        login_btn.pack(pady=(5,10))
        login_btn.configure(font = ('verdana', 10))
#-------------------------------------------------------------------------------------------------------------------------------- 

        label3 = Label(self.root, text = 'Not a member?', bg = '#1C2833',fg = '#2980B9')
        label3.pack(pady=(3,10))
        label3.configure(font=('verdana',10, 'bold'))

        register_btn = Button(self.root, text = 'Register Now', command=self.register_gui)
        register_btn.pack(pady=(3,10))
        register_btn.configure(font=('verdana',10))
#-------------------------------------------------------------------------------------------------------------------------------- 


    def register_gui(self):
        self.clear()

        heading = Label(self.root, text = 'NLPApp', bg = '#1C2833', fg = 'white') # display software name with Label class
        heading.pack(pady=(30,30)) # geometry manager, put your heading components on  the ui (Like Gauri Khan)
        heading.configure(font = ('verdana', 24, 'bold')) # font size set
#--------------------------------------------------------------------------------------------------------------------------------        
        label0 = Label(self.root, text = 'Enter Name')
        label0.pack(pady=(10,10))
        label0.configure(font = ('verdana', 10)) # font size set

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5,10), ipady = 4) #ipady use for set height
        
#--------------------------------------------------------------------------------------------------------------------------------        
        label1 = Label(self.root, text = 'Enter Email')
        label1.pack(pady=(10,10))
        label1.configure(font = ('verdana', 10)) # font size set

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10), ipady = 4) #ipady use for set height
#--------------------------------------------------------------------------------------------------------------------------------                
        label2 = Label(self.root, text = 'Enter Password')
        label2.pack(pady=(10,10))
        label2.configure(font = ('verdana', 10)) # font size set

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5,10), ipady = 4) #ipady use for set height
#--------------------------------------------------------------------------------------------------------------------------------        
        Register_btn = Button(self.root, text = "Register", width = 30, height= 2, command=self.perform_registration) # Button class for Register click
        Register_btn.pack(pady=(5,10))
        Register_btn.configure(font = ('verdana', 10))

#--------------------------------------------------------------------------------------------------------------------------------        

        label3 = Label(self.root, text = 'Already a member?', bg = '#1C2833',fg = '#2980B9')
        label3.pack(pady=(3,10))
        label3.configure(font=('verdana',10, 'bold'))

        login_btn = Button(self.root, text = 'login Now', command=self.login_gui)
        login_btn.pack(pady=(3,10))
        login_btn.configure(font=('verdana',10))
#--------------------------------------------------------------------------------------------------------------------------------        

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
 #--------------------------------------------------------------------------------------------------------------------------------    
    def perform_registration(self):
        name = self.name_input.get()  
        email = self.email_input.get()  
        password = self.password_input.get()  

        response = self.dob.add_data(name, email, password)

        if response == 1:
            messagebox.showinfo('Success', 'Registration successful. You can login now')
        else:
            messagebox.showerror('error', 'Emailo already exist')
#--------------------------------------------------------------------------------------------------------------------------------     
    def perform_login(self):
        email = self.email_input.get()  
        password = self.password_input.get()  

        response = self.dob.search(email, password)

        if response == 1:
            messagebox.showinfo('Sucess', 'successfully login!!!')
            self.home_gui()

        else:
            messagebox.showerror('Error', 'Login failed')
            self.login_gui()
#--------------------------------------------------------------------------------------------------------------------------------     
    def home_gui(self):

        self.clear()

        heading = Label(self.root, text = 'NLPApp',bg = '#1C2833' , fg = 'white' )
        heading.pack(pady=(10,10))
        heading.configure(font = ('Verdana',24, 'bold'))
#-------------------------------------------------------------------------------------------------------------------------------- 
        sentiment_btn = Button(self.root, text = "Sentiment Analysis", width = 30, height = 4, command = self.sentiment_gui)
        sentiment_btn.pack(pady= (10,10))
        sentiment_btn.configure(font = ('verdana', 10))
#-------------------------------------------------------------------------------------------------------------------------------- 
        ner_btn = Button(self.root, text = "Name Entity Recognition", width = 30, height = 4, command = self.ner_gui)
        ner_btn.pack(pady= (10,10))
        ner_btn.configure(font = ('verdana', 10))
#-------------------------------------------------------------------------------------------------------------------------------- 
        emotion_btn = Button(self.root, text = "Emotion Prediction", width = 30, height = 4, command = self.emp_gui)
        emotion_btn.pack(pady= (10,10))
        emotion_btn.configure(font = ('verdana', 10))
#-------------------------------------------------------------------------------------------------------------------------------- 
        logout_btn = Button(self.root, text = "logout", width = 30, height = 4, command = self.login_gui)
        logout_btn.pack(pady= (3,10))
        logout_btn.configure(font = ('verdana', 10))

#-------------------------------------------------------------------------------------------------------------------------------- 
    def sentiment_gui(self):
        self.clear()
        
        heading = Label(self.root, text = 'NLPApp',bg = '#1C2833' , fg = 'white' )
        heading.pack(pady=(10,10))
        heading.configure(font = ('Verdana',24, 'bold'))
        
        heading2 = Label(self.root, text = 'NER Analysis',bg = '#1C2833' , fg = 'white' )
        heading2.pack(pady=(8,8))
        heading2.configure(font = ('Verdana',20))
#--------------------------------------------------------------------------------------------------------------------------------
        label1 = Label(self.root, text = 'Enter the text',bg = '#1C2833' , fg = 'red')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',15))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5,10), ipady = 5)
        
        ner_btn = Button(self.root, text = "Analyize NER", command = self.do_ner_analysis)
        ner_btn.pack(pady = (10,10))

        self.sentiment_result = Button(self.root, text = '', bg = '#1C2833', fg = 'green')
        self.sentiment_result.pack(pady= (10,10))
        self.sentiment_result.configure(font = ('verdana', 16))
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------        
        goback_btn = Button(self.root, text = "Back", command = self.home_gui)
        goback_btn.pack(pady= (10,10))
        goback_btn.configure(font = ('verdana', 10))
#--------------------------------------------------------------------------------------------------------------------------------
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result= self.apio.sentiment_analysis(text)
        l = []
        for i in result['sentiment']:
                l.append(result['sentiment'][i])
        m=max(l)

        for i in result['sentiment']:
                if result['sentiment'][i] ==m:
                        self.sentiment_result['text'] = i

#-------------------------------------------------------------------------------------------------------------------------------- 
    def ner_gui(self):
        self.clear()
        
        heading = Label(self.root, text = 'NLPApp',bg = '#1C2833' , fg = 'white' )
        heading.pack(pady=(10,10))
        heading.configure(font = ('Verdana',24, 'bold'))
        
        heading2 = Label(self.root, text = 'Sentiment Analysis',bg = '#1C2833' , fg = 'white' )
        heading2.pack(pady=(8,8))
        heading2.configure(font = ('Verdana',20))
#--------------------------------------------------------------------------------------------------------------------------------
        label1 = Label(self.root, text = 'Enter the text',bg = '#1C2833' , fg = 'red')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',15))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5,10), ipady = 4)
        
        ner_btn = Button(self.root, text = "Analyize NER", command = self.do_ner_analysis)
        ner_btn.pack(pady = (10,10))

        self.ner_result = Button(self.root, text = '', bg = '#1C2833', fg = 'white')
        self.ner_result.pack(pady= (10,10))
        self.ner_result.configure(font = ('verdana', 16))
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------        
        goback_btn = Button(self.root, text = "Back", command = self.home_gui)
        goback_btn.pack(pady= (10,10))
        goback_btn.configure(font = ('verdana', 10))
#--------------------------------------------------------------------------------------------------------------------------------
    def do_ner_analysis(self):
        text = self.ner_input.get()
        result= self.apio.ner_analysis(text)
        txt = ''
        for i in result['entities']:
                txt += "name : " + str(i['name']) + " --> " + "category : " + str(i['category']) + " --> " + "confidence_score : " + str(i['confidence_score']) + '\n'
        
        self.ner_result['text']=txt

        # try this example - Barack Obama was born in Hawaii on August 4, 1961


#-------------------------------------------------------------------------------------------------------------------------------- 
    def emp_gui(self):
        self.clear()
        
        heading = Label(self.root, text = 'NLPApp',bg = '#1C2833' , fg = 'white' )
        heading.pack(pady=(10,10))
        heading.configure(font = ('Verdana',24, 'bold'))
        
        heading2 = Label(self.root, text = 'Emotion Prediction',bg = '#1C2833' , fg = 'white' )
        heading2.pack(pady=(8,8))
        heading2.configure(font = ('Verdana',20))
#--------------------------------------------------------------------------------------------------------------------------------
        label1 = Label(self.root, text = 'Enter the text',bg = '#1C2833' , fg = 'red')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',15))

        self.emp_input = Entry(self.root, width=50)
        self.emp_input.pack(pady=(5,10), ipady = 4)
        
        emp_btn = Button(self.root, text = "Analyize EMP", command = self.do_emp_analysis)
        emp_btn.pack(pady = (10,10))

        self.emp_result = Button(self.root, text = '', bg = '#1C2833', fg = 'white')
        self.emp_result.pack(pady= (10,10))
        self.emp_result.configure(font = ('verdana', 16))
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------        
        goback_btn = Button(self.root, text = "Back", command = self.home_gui)
        goback_btn.pack(pady= (10,10))
        goback_btn.configure(font = ('verdana', 10))
#--------------------------------------------------------------------------------------------------------------------------------
    def do_emp_analysis(self):
        text = self.emp_input.get()
        result= self.apio.emp_analysis(text)
        
        txt=list(filter(lambda x: max(x),result['emotion']))
        self.emp_result['text']=txt[0]
        
        # try this example - tired people become frustrated and guilty people become ashamed.
                  



nlp = NLPApp()