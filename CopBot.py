from tkinter import *
import os
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
from tkinter import ttk
from webdriver_manager.chrome import ChromeDriverManager          
from win10toast import ToastNotifier
import webbrowser
from selenium.webdriver.chrome.service import Service

class CopBot_app():

    def session(self):
        self.Session_screen = Toplevel(self.Main_screen)
        self.Session_screen.geometry("300x840")
        self.clock_thread = threading.Thread(target=self.Clock)
        self.clock2_thread = threading.Thread(target=self.Clock2)
        Tabs = ttk.Notebook(self.Session_screen)
        self.Tab1 = ttk.Frame(Tabs)
        Tabs.add(self.Tab1, text="Billing")
        self.Tab2 = ttk.Frame(Tabs)
        Tabs.add(self.Tab2, text="Product")
        self.Tab3 = ttk.Frame(Tabs)
        Tabs.add(self.Tab3, text="Instructions")
        self.Tab4 = ttk.Frame(Tabs)
        Tabs.add(self.Tab4, text="Account")
        Tabs.pack(expan = 1, fill = "both")
    
        self.time_tab1 = Label(self.Tab1, text="", bg="grey")
        self.time_tab1.pack(side=TOP, anchor=NE)
        self.time_tab2 = Label(self.Tab2, text="", bg="grey")
        self.time_tab2.pack(side=TOP, anchor=NE)
        self.clock_thread.start()
        self.clock2_thread.start()
        self.Delete_account = ttk.Button(self.Tab4, text= "Delete Account", width = 20, command= self.Sure_to_delete)
        self.Logout_account = ttk.Button(self.Tab4, text= "Log Out", width = 10, command= self.Sure_to_logout)
        self.Session_screen.bind("<Return>", self.Session_Enter)

        self.username1 = self.username_verify.get().upper()

        list_of_files = os.listdir()

        if self.username1 not in list_of_files:
            with open(self.username1, "w") as file:   
                file.write(self.username_verify.get()+"\n"+self.password_verify.get()+("\n " * 12).strip())
            with open(self.username1) as f:
                lines = f.read().splitlines()

            self.Read_FirstName = lines[2]
            self.Read_LastName = lines[3]
            self.Read_Email = lines[4]
            self.Read_Phone = lines[5]
            self.Read_Street = lines[6]
            self.Read_Apt = lines[7]
            self.Read_Zip = lines[8]
            self.Read_City = lines[9]
            self.Read_State = lines[10]
            self.Read_Number = lines[11]
            self.Read_Cvv = lines[12]
            self.Read_extra = lines[13]

        else:
            with open(self.username1) as f:
                lines = f.read().splitlines()

            try:
                self.Read_FirstName = lines[2]
                self.Read_LastName = lines[3]
                self.Read_Email = lines[4]
                self.Read_Phone = lines[5]
                self.Read_Street = lines[6]
                self.Read_Apt = lines[7]
                self.Read_Zip = lines[8]
                self.Read_City = lines[9]
                self.Read_State = lines[10]
                self.Read_Number = lines[11]
                self.Read_Cvv = lines[12]
                self.Read_extra = lines[13]
            except IndexError:
                self.Read_FirstName = ""
                self.Read_LastName = ""
                self.Read_Email = ""
                self.Read_Phone = ""
                self.Read_Street = ""
                self.Read_Apt = ""
                self.Read_Zip = ""
                self.Read_City = ""
                self.Read_State = ""
                self.Read_Number = ""
                self.Read_Cvv = ""
                self.Read_extra = ""

    #FIRST NAME
        Label(self.Tab1, text="First Name").pack()
        self.First_Name = StringVar()
        self.FirstName_Entry = ttk.Entry(self.Tab1, textvariable=self.First_Name)
        self.FirstName_Entry.insert(0, self.Read_FirstName)
        self.FirstName_Entry.pack()
        self.FirstName_Entry.focus_set()

    #LAST NAME
        Label(self.Tab1, text="Last Name").pack()
        self.Last_Name = StringVar()
        self.LastName_Entry = ttk.Entry(self.Tab1, textvariable=self.Last_Name)
        self.LastName_Entry.insert(0, self.Read_LastName)
        self.LastName_Entry.pack()

    #EMAIL
        Label(self.Tab1, text="Email").pack()
        self.Email = StringVar()
        self.Email_Entry = ttk.Entry(self.Tab1, textvariable=self.Email)
        self.Email_Entry.insert(0, self.Read_Email)
        self.Email_Entry.pack()

    #PHONE NUMBER
        Label(self.Tab1, text="Phone Number").pack()
        self.Phone = StringVar()
        self.Phone_Entry = ttk.Entry(self.Tab1, validate="key",textvariable=self.Phone)
        self.Phone_Entry.insert(0, self.Read_Phone)
        self.Phone_Entry['validatecommand'] = (self.Phone_Entry.register(self.testVal),'%P','%d')
        self.Phone_Entry.pack()

    #STREET
        Label(self.Tab1, text="Street Address").pack()
        self.Street = StringVar()
        self.Street_Entry = ttk.Entry(self.Tab1, textvariable=self.Street)
        self.Street_Entry.insert(0, self.Read_Street)
        self.Street_Entry.pack()

    #APT
        Label(self.Tab1, text="Apartment number").pack()
        self.Apt = StringVar()
        self.Apt_Entry = ttk.Entry(self.Tab1, textvariable=self.Apt)
        self.Apt_Entry.insert(0, self.Read_Apt)
        self.Apt_Entry.pack()

    #ZIP
        Label(self.Tab1, text="Zip/Postal Code").pack()
        self.Zip = StringVar()
        self.Zip_Entry = ttk.Entry(self.Tab1, textvariable=self.Zip)
        self.Zip_Entry.insert(0, self.Read_Zip)
        self.Zip_Entry.pack()

    #CITY
        Label(self.Tab1, text="City").pack()
        self.City = StringVar()
        self.City_Entry = ttk.Entry(self.Tab1, textvariable=self.City)
        self.City_Entry.insert(0, self.Read_City)
        self.City_Entry.pack()

    #STATE OR PROVINCE
        Label(self.Tab1, text="State or Province Acronym").pack()
        self.State =StringVar()
        self.State_Entry = ttk.Entry(self.Tab1, textvariable=self.State)
        self.State_Entry.insert(0, self.Read_State)
        self.State_Entry.pack()

    #COUNTRY
        Countries = [
            "USA",
            "CANADA",
            "MEXICO",
            "GERMANY",
            "UK",
            "FRANCE",
            "JAPAN"
        ]
        Label(self.Tab1, text="Country").pack()
        self.Country = StringVar()
        self.Country_Entry = ttk.OptionMenu(self.Tab1, self.Country, Countries[0], *Countries)
        self.Country_Entry.pack()

    #NUMBER
        Label(self.Tab1, text="Card Number").pack()
        self.Number = StringVar()
        self.Number_Entry = ttk.Entry(self.Tab1, validate='key', textvariable=self.Number)
        self.Number_Entry.insert(0, self.Read_Number)
        self.Number_Entry['validatecommand'] = (self.Number_Entry.register(self.testVal),'%P','%d')
        self.Number_Entry.pack()
        
    #CARD MONTH
        months = [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ]
        Label(self.Tab1, text="Card Month").pack()
        self.Month = StringVar()
        self.Month_Entry = ttk.OptionMenu(self.Tab1, self.Month, months[0], *months)
        self.Month_Entry.pack()

    #CARD YEAR
        years = [
            "2020",
            "2021",
            "2022",
            "2023",
            "2024",
            "2025",
            "2026",
            "2027",
            "2028",
            "2029",
            "2030",
        ]
        Label(self.Tab1, text="Card Year").pack()
        self.Year = StringVar()
        self.Year_Entry= ttk.OptionMenu(self.Tab1, self.Year, years[0], *years)
        self.Year_Entry.pack()

    #CVV AND READ SAVE THINGS
        Label(self.Tab1, text="Card Cvv").pack()
        self.Cvv = StringVar()
        self.Cvv_Entry = ttk.Entry(self.Tab1, validate='key', textvariable=self.Cvv)
        self.Cvv_Entry.insert(0, self.Read_Cvv)
        self.Cvv_Entry['validatecommand'] = (self.Cvv_Entry.register(self.testVal),'%P','%d')
        self.Cvv_Entry.pack()

        self.Save_text = Label(self.Tab1, text="")
        self.Save_text.pack()

        self.extra = StringVar()
        self.extra_entry = ttk.Entry(self.Tab1, textvariable=self.extra)
        self.extra_entry.insert(0, self.Read_extra)    

        if self.Read_FirstName == " ":
            self.FirstName_Entry.delete(0, END)
        if self.Read_LastName == " ":
            self.LastName_Entry.delete(0, END)
        if self.Read_Email == " ":
            self.Email_Entry.delete(0, END)
        if self.Read_Phone == " ":
            self.Phone_Entry.delete(0, END)
        if self.Read_Street == " ":
            self.Street_Entry.delete(0, END)
        if self.Read_City == " ":    
            self.City_Entry.delete(0, END)
        if self.Read_Zip == " ":    
            self.Zip_Entry.delete(0, END)
        if self.Read_Cvv == " ":    
            self.Cvv_Entry.delete(0, END)
        if self.Read_Number == " ":    
            self.Number_Entry.delete(0, END)
        if self.Read_Apt == " ":    
            self.Apt_Entry.delete(0, END)
        if self.Read_State == " ":    
            self.State_Entry.delete(0, END)    

        self.Session_screen.protocol('WM_DELETE_WINDOW', self.Main_screen.quit)
        
    #PRODUCT NAME
        Label(self.Tab2, text="Product Key Words").pack()
        self.Product_name = StringVar()
        self.Product_nameEntry= ttk.Entry(self.Tab2, textvariable=self.Product_name)
        self.Product_nameEntry.pack()
        Label(self.Tab2, text="").pack()
        self.Product_nameEntry.focus_set()

    #PRODUCT SIZE
        Label(self.Tab2, text="Product Size").pack()
        self.Product_size = StringVar()
        self.Product_sizeEntry= ttk.Entry(self.Tab2, textvariable=self.Product_size)
        self.Product_sizeEntry.pack()
        Label(self.Tab2, text="").pack()

    #PRODUCT QUANTITY
        pr_qty = [
            "",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"
        ]
        Label(self.Tab2, text="Product Quantity").pack()
        self.Product_quantity = StringVar()
        self.Product_quantityEntry = ttk.OptionMenu(self.Tab2, self.Product_quantity, pr_qty[0], *pr_qty)
        self.Product_quantityEntry.pack()
        self.Product_quantity.set(pr_qty[0])
        Label(self.Tab2, text="").pack()

    #PAGE AND SAVE DEFS
        Label(self.Tab2, text="Page Link").pack()
        self.Product_page = StringVar()
        self.Product_pageEntry= ttk.Entry(self.Tab2, textvariable=self.Product_page, width=40)
        self.Product_pageEntry.insert(0, "https://www.supremenewyork.com/shop/all/")
        self.Product_pageEntry.pack()
        Label(self.Tab2, text="").pack()

    #SAVE BUTTONS
        self.Save_button = ttk.Button(self.Tab1, width = 10, text= "Save", command=lambda:[self.Save(),self.Write_settings()])
        self.Save_button.pack()
        self.Run_button = ttk.Button(self.Tab2, width = 10, text="Run", command=lambda:[self.Save2(),self.Save(),self.Run()])
        self.Run_button.pack()
        self.Run_text = Label(self.Tab2, text="", fg="red")
        self.Run_text.pack()

    #LOGOUT AND DELETE ACCOUNT BUTTONS

        Label(self.Tab4, text="").pack()
        self.Logout_account.pack()
        Label(self.Tab4, text="").pack()
        self.Delete_account.pack()

    def Save(self):

        self.Sel_FirstName = self.First_Name.get()
        self.Sel_LastName = self.Last_Name.get()
        self.Sel_Email = self.Email.get()
        self.Sel_Phone = self.Phone.get()
        self.Sel_Street = self.Street.get()
        self.Sel_Apt = self.Apt.get()
        self.Sel_Zip = self.Zip.get()
        self.Sel_City = self.City.get()
        self.Sel_State = self.State.get()
        self.Sel_Country = self.Country.get()
        self.Sel_Number = self.Number.get()
        self.Sel_Card_Month = self.Month.get()
        self.Sel_Card_Year = self.Year.get()
        self.Sel_Cvv = self.Cvv.get()

    def Save2(self):
    
        self.Sel_Product = self.Product_name.get()
        self.Sel_ProductSize = self.Product_size.get()
        self.Sel_Page = self.Product_page.get()
        self.Sel_ProductQuantity = self.Product_quantity.get()

    def Sure_to_delete(self):
        
        self.Delete_screen = Toplevel(self.Main_screen)
        self.Delete_screen.title("Delete?")
        self.Delete_screen.geometry("300x110")
        self.Delete_screen.resizable(False, False)
        self.Delete_screen.grab_set()

        self.want_to_delete = Label(self.Delete_screen, text="Are you sure you want to delete your account?")
        self.want_to_delete.pack()
        self.delete_button = ttk.Button(self.Delete_screen, text="Yes", width=8, command=self.remove)
        self.delete_button.pack()
        Label(self.Delete_screen, text="").pack()
        self.dont_delete_button = ttk.Button(self.Delete_screen, width=8, text="No", command=self.close)
        self.dont_delete_button.pack()
        self.dont_delete_button.focus_set()
        self.Delete_screen.bind("<Return>", self.Delete_enter)

    def dont_logout(self):

        self.Logout_screen.withdraw()
        self.Logout_screen.grab_release()

    def logout(self):

        self.Logout_screen.withdraw()
        self.Main_screen.deiconify()
        self.Session_screen.withdraw()
        self.Logout_screen.grab_release()

    def Sure_to_logout(self):

        self.Logout_screen = Toplevel(self.Main_screen)
        self.Logout_screen.title("Log out?")
        self.Logout_screen.geometry("300x110")
        self.Logout_screen.resizable(False, False)
        self.Logout_screen.grab_set()

        self.want_to_logout = Label(self.Logout_screen, text="Are you sure you want to log out?")
        self.want_to_logout.pack()
        self.logout_button = ttk.Button(self.Logout_screen, text="Yes", width=8, command=self.logout)
        self.logout_button.pack()
        Label(self.Logout_screen, text="").pack()
        self.dont_logout_button = ttk.Button(self.Logout_screen, width=8, text="No", command=self.dont_logout)
        self.dont_logout_button.pack()
        self.logout_button.focus_set()
        self.Logout_screen.bind("<Return>", self.Log_out_enter)

    def testVal(self,inStr,acttyp):
        if acttyp == '1': #insert
            if not inStr.isdigit():
                return False
        return True

    def Back(self):

        self.Main_screen.deiconify()
        self.Session_screen.withdraw()

    def order(self):
        while True:
            self.options = Options()
            self.options.add_argument('--disable-gpu') 
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.get(self.Sel_Page)
            print(ChromeDriverManager().install())
            
            self.products = self.driver.find_elements(By.CLASS_NAME, 'collection-ul')
            
            self.search = self.Sel_Product
            
            self.search_words = self.search.split()
            self.found_product = False
                
            # Search for a match by text inside product WebElements
            for p in self.products:
                if all(search_word in p.text for search_word in self.search_words):
                    self.found_product = p
            if not self.found_product: 
                self.driver.refresh()
            else: 
                pass 
            self.found_product.click() if self.found_product else print('No product found')
            break 
        
        # Size
        while True:
            if self.Sel_ProductSize == "":
                break
            else:
                try:
                    size = Select(self.driver.find_element(By.ID, 'size'))
                    size.select_by_visible_text(self.Sel_ProductSize)
                    break
                except (NoSuchElementException):
                    wait = WebDriverWait(self.driver, 10)
                    waitBis = wait.until(EC.presence_of_element_located((By.ID, 'time-zone-name')))
                    self.driver.refresh()

        # Quantity
        while True:
            if self.Sel_ProductQuantity == "":
                break
            else:
                try:
                    self.qty = Select(self.driver.find_element(By.ID, 'qty'))
                    self.qty.select_by_visible_text(self.Sel_ProductQuantity)
                    break
                except (NoSuchElementException):
                    wait = WebDriverWait(self.driver, 10)
                    waitBis = wait.until(EC.presence_of_element_located((By.ID, 'time-zone-name')))
                    self.driver.refresh()            
        
        # Waits for add to cart button to load then clicks it
        while True:
            try:
                self.driver.find_element(By.NAME, 'commit').click()
                break
            except (NoSuchElementException):     
                wait = WebDriverWait(self.driver, 10)
                waitBis = wait.until(EC.presence_of_element_located((By.ID, 'time-zone-name')))
                self.driver.refresh()

        # Wait for checkout button element to load
        wait = WebDriverWait(self.driver, 10)
        waitBis = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'checkout'))).click()

        # Fills out checkout screen fields

        # Fills out Name
        self.driver.find_element(By.XPATH, '//*[@id="order_billing_name"]').send_keys(self.Sel_FirstName)
        
        # Fills out Email
        self.driver.find_element(By.XPATH, '//*[@id="order_email"]').send_keys(self.Sel_Email)
        
        # Fills out Phone Number
        self.driver.find_element(By.XPATH, '//*[@id="order_tel"]').send_keys(self.Sel_Phone)
        
        # Fills out Address
        self.driver.find_element(By.XPATH, '//*[@id="order_billing_address"]').send_keys(self.Sel_Street)
        
        # Fills out apt, unit, etc
        self.driver.find_element(By.XPATH, '//*[@id="order_billing_address_2"]').send_keys(self.Sel_Apt)
        
        # Fills out Zip
        self.driver.find_element(By.XPATH, '//*[@id="order_billing_zip"]').send_keys(self.Sel_Zip)
        
        # Fills out City
        self.driver.find_element(By.XPATH, '//*[@id="order_billing_city"]').send_keys(self.Sel_City)
        
        # Fills out Card Number
        self.driver.find_element(By.XPATH, '//*[@id="credit_card_number"]').send_keys(self.Sel_Number)
        
        # Fills out Card Cvv
        self.driver.find_element(By.XPATH, '//*[@id="credit_card_verification_value"]').send_keys(self.Sel_Cvv)
        
        # Selects Country
        self.country = Select(self.driver.find_element(By.NAME, 'order[billing_country]'))
        self.country.select_by_value(self.Sel_Country.upper())
        
        # Selects State/Province
        self.state = Select(self.driver.find_element(By.NAME, 'order[billing_state]'))  
        self.state.select_by_value(self.Sel_State.upper())
        
        # Selects Card Month
        self.month = Select(self.driver.find_element(By.NAME, 'credit_card[month]'))
        self.month.select_by_value(self.Sel_Card_Month)
        
        # Selects Card Year
        self.year = Select(self.driver.find_element(By.NAME, 'credit_card[year]'))
        self.year.select_by_value(self.Sel_Card_Year)
        
        # Checks agreement box
        self.driver.find_element(By.XPATH, '//*[@id="terms-checkbox"]/label/div/ins').click()
        
        # Clicks process payment button
        self.process_payment = self.driver.find_element(By.XPATH, '//*[@id="pay"]/input')
        self.process_payment.click()
        
        # Sends a Windows notification
        self.Notification = ToastNotifier()
        self.Notification.show_toast("Do Captcha", "Do the captcha to buy the " + self.Sel_Product, threaded=True)

            
    def Run(self):

        white_product = self.Sel_Product.isspace()
        thread = threading.Thread(target=self.order)

        if self.Sel_Product == "" or white_product:
            self.Run_text.config(text="Please type a keyword for product")
            self.Session_screen.after(2000, self.Run_text_delete)
        else:
            thread.start()

    def Clock(self):

        self.Time_date = time.strftime("%I:%M:%S %A")

        self.time_tab1.config(text= self.Time_date)   
        self.time_tab1.after(1000, self.Clock)

    def Clock2(self):

        self.time_tab2.config(text= self.Time_date)    
        self.time_tab2.after(1000, self.Clock2)

    def Run_text_delete(self):

        self.Run_text.config(text="")

    def Write_settings(self):

        with open(self.username_verify.get(), "w") as file:   
            file.write(self.username_verify.get()+"\n"+self.password_verify.get()+"\n"+self.Sel_FirstName+"\n"+self.Sel_LastName+"\n"+self.Sel_Email+"\n"+self.Sel_Phone+"\n"+self.Sel_Street+"\n"+self.Sel_Apt+"\n"+self.Sel_Zip+"\n"+self.Sel_City+"\n"+self.Sel_State+"\n"+self.Sel_Number+"\n"+self.Sel_Cvv+"\n"+" ")
        
        self.Save_text.config(text="Saved!", fg="green")
        self.Session_screen.after(1500, self.Save_text_delete)

    def Save_text_delete(self):

        self.Save_text.config(text="")

    def close(self):

        self.Delete_screen.withdraw()
        self.Session_screen.deiconify()
        self.Delete_screen.grab_release()

    def ok_close(self):

        self.Delete_screen.withdraw()
        self.Session_screen.withdraw()
        self.Main_screen.deiconify()
        self.Delete_screen.grab_release()

    def remove(self):
        
        os.remove(self.username_verify.get())
        list_of_files = os.listdir()

        if "r" in list_of_files:
            with open("r", "r") as file3:
                verify = file3.read().splitlines()
                verify1 = verify[0]
            if verify1 == self.username_verify.get():
                with open("r", "w") as file4:
                    file4.write("" + "\n" + "")
        
        self.Delete_screen.protocol("WM_DELETE_WINDOW", self.nothing)
        self.Delete_screen.title("Successfuly removed")
        self.want_to_delete.config(text="Account successfuly removed")
        self.delete_button.destroy()
        self.dont_delete_button.destroy()
        self.ok_button = ttk.Button(self.Delete_screen, text="Ok", width=8, command=self.ok_close)
        self.ok_button.pack()
        self.ok_button.focus_set()

    def nothing(self):
        
        pass

    def login_verify(self):

        list_of_files = os.listdir()
        self.username1 = self.username_verify.get().upper()
        self.password1 = self.password_verify.get()

        user_white = self.username1.isspace()
        pass_white = self.password1.isspace()


        if self.username1 in list_of_files:

            with open(self.username1) as f:
                lines = f.read().splitlines()

            if self.password1 == lines[1]:
                if self.checkbox.get() == "On":
                    with open("r", "w") as f:
                        f.write(f"{self.username_verify.get()}\n{self.password_verify.get()}")
                else:
                    pass
                self.session()
                self.Main_screen.withdraw()
                self.Login_screen.withdraw()
                self.Login_screen.grab_release()
            elif self.password_verify.get() == "" or pass_white:
                self.message_login.config(text="Please fill in all the boxes", fg="red")
                self.Login_screen.after(1500, self.login_message_delete)
            else:
                self.message_login.config(text="Wrong Password", fg="red")
                self.Login_screen.after(1500, self.login_message_delete)
        elif self.username_verify.get() == "" or user_white:
            self.message_login.config(text="Please fill in all the boxes", fg="red")
            self.Login_screen.after(1500, self.login_message_delete)
        elif self.password_verify.get() == "" or pass_white:
            self.message_login.config(text="Please fill in all the boxes", fg="red")
            self.Login_screen.after(1500, self.login_message_delete)
        elif self.username1 not in list_of_files:
            self.message_login.config(text="User Not Found", fg="red")
            self.Login_screen.after(1500, self.login_message_delete)

    def login_message_delete(self):
        self.message_login.config(text= "")

    def callback(self,url):
        webbrowser.open_new(url)

    def login(self):
        
        self.Login_screen = Toplevel(self.Main_screen)
        self.Login_screen.title("Login")
        self.Login_screen.geometry("300x300")
        self.Login_screen.resizable(False, False)
        Label(self.Login_screen, text= "Please Login").pack()
        self.Login_screen.grab_set()

        self.username_verify = StringVar()
        self.password_verify = StringVar()
      
        self.checkbox = StringVar()

        Label(self.Login_screen, text= "").pack()
        Label(self.Login_screen, text= "Username ").pack()
        self.username_entry1 = ttk.Entry(self.Login_screen, text = self.username_verify)
        self.username_entry1.pack()
        self.username_entry1.focus_set()
        Label(self.Login_screen, text= "").pack()
        Label(self.Login_screen, text= "Password ").pack()
        self.password_entry1 = ttk.Entry(self.Login_screen, show="•", text = self.password_verify)
        self.password_entry1.pack()
        self.Remember_me = ttk.Checkbutton(self.Login_screen, text="Remember me", variable=self.checkbox, onvalue="On", offvalue="Off")
        self.Remember_me.pack()
        ttk.Button(self.Login_screen, text = "Login",  width = 15,  command = self.login_verify).pack()
        self.message_login = Label(self.Login_screen, text="")
        self.message_login.pack()
        self.Login_screen.bind("<Return>", self.login_verify_event)

        with open("r", "r") as self.read_remember:
            check = self.read_remember.read().splitlines() 
        self.remember_read_name = check[0]
        self.remember_read_pass = check[1]
        self.username_entry1.insert(0, self.remember_read_name)
        self.password_entry1.insert(0, self.remember_read_pass)

    def Delete_enter(self, event):

        focused_button = self.Delete_screen.focus_get()
        if focused_button != self.Delete_screen:
            focused_button.invoke()

    def login_verify_event(self, event):

        self.login_verify()

    def Session_Enter(self, event):

        focused_button =self.Session_screen.focus_get()
        if focused_button != self.Session_screen:
            focused_button.invoke()

    def Log_out_enter(self, event):

        focused_button = self.Logout_screen.focus_get()
        if focused_button != self.Logout_screen:
            focused_button.invoke()

    def Click(self, event):

        focused_button = self.Main_screen.focus_get()
        if focused_button != self.Main_screen:
            focused_button.invoke()

    def main_screen(self):
        self.Main_screen = Tk()
        self.Main_screen.geometry("450x450")
        self.Main_screen.title("CopBot")
        Label(text= "CopBot", bg = "grey", width = "300").pack()
        Label(text= "").pack()
        self.Login_button = ttk.Button(text = "Login", width = 25, command = self.login)
        self.Login_button.pack()
        Label(text= "").pack()
        ttk.Button(text = "Exit", width = 25, command = self.Main_screen.quit).pack()
        Label(text= "").pack()
        self.Main_screen.protocol('WM_DELETE_WINDOW', self.Main_screen.quit)
        self.Main_screen.bind("<Return>", self.Click)
        self.Main_screen.mainloop()
        
if __name__ == "__main__":
    app = CopBot_app()
    app.main_screen()