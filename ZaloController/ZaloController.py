from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
import chromedriver_autoinstaller
import undetected_chromedriver as uc
import os
import sys
import time
import re
sys.path.append(os.getcwd())
from SqliteHelper.SqliteHelper import *
from ZaloController.ElementZalo import *
from utils import *
PATH = os.getcwd()

version_main = int(chromedriver_autoinstaller.get_chrome_version().split(".")[0])

class AutoZalo:
    def __init__(self, time_open):
        self.time_open = time_open

    # def open_profile(self):
    #     chrome_options = Options()
    #     chrome_options.add_argument(
    #         "user-data-dir=C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data")
    #     chrome_options.add_argument("disable-infobars")
    #     chrome_options.add_argument("--headless")
    #     chrome_options.add_argument("--profile-directory=" + "Profile zalo")
    #     self.driver = webdriver.Chrome(chrome_options=chrome_options)
    #     self.driver.maximize_window()
    #     self.driver.get("https://chat.zalo.me/")
    #     time.sleep(self.time_open)
    def open_profile(self):
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("user-data-dir=C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data")
        chrome_options.add_argument("--profile-directory=" + "Profile zalo")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        self.driver = uc.Chrome(options=chrome_options, 
                                use_subprocess=True, 
                                headless=False,
                                version_main=version_main)
        self.driver.maximize_window()
        self.driver.get("https://chat.zalo.me/")
        self.driver.get_screenshot_as_file("screenshot.png")
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        time.sleep(self.time_open)
        
    def add2group(self, phone_number):
        self.driver.get("https://chat.zalo.me/")
        sleep_short()
        WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(CONTACT_SEARCH_INPUT)).send_keys("CHỊ EM SĂN ĐỒ RẺ CHẤT LƯỢNG")
        sleep_short()
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep_short()
        WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(ADD_MEMBER)).click()
        sleep_short()
        self.driver.switch_to.active_element.send_keys(phone_number)
        sleep_short()
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep_short()
        
        if ERR0R_NOTFOUND_ADDMEMBER in self.driver.page_source:
            print("Không mời được")
            return 0
        else:
            try:
                WebDriverWait(self.driver,  30).until(
                        EC.presence_of_element_located(CHOICE_PEOPLE)).click()
                sleep_short()
                WebDriverWait(self.driver,  30).until(
                        EC.presence_of_element_located(ADD_MEMBER_BUTTON)).click()
                sleep_short()
                return 1
            except:
                print("Không mời được")
                return 0
    
    def switch_to_groups(self):
        try:
            # self.driver.find_element(By.XPATH, '//div[@title="Danh bạ"]').click()
            WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@title="Danh bạ"]'))).click()
            # WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(
            #          (By.XPATH, '//div[@icon="icon-solid-left"]'))).click()
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[contains(text(), "Danh sách nhóm")]'))).click()
        except:
            self.driver.get("https://chat.zalo.me/")
            WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@title="Danh bạ"]'))).click()
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[contains(text(), "Danh sách nhóm")]'))).click()
    def scan_member(self):
        #connect SQL
        conn = create_connection(PATH+ "/database/database_Nhom.db")
        delete_table(conn=conn, table="Nhom")
        query = f"""CREATE TABLE IF NOT EXISTS Nhom (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    group_name text NOT NULL,
                                    member_name text,
                                    status text,
                                    state text
                                );"""
        create_table(conn=conn, query=query)
        # find element 'Danh bạ'
        self.switch_to_groups()
        number_groups = WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located((By.XPATH, '//span[@data-translate-inner="STR_GROUP_LIST_COUNTER"]'))).text
        number_groups = int(re.search('Nhóm (.*)', number_groups).group(1)[1:-1])
        print("Số lượng nhóm: ",number_groups)
        groups = []
        while len(groups) < number_groups:
            elements = WebDriverWait(self.driver, timeout=2).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="detail-info"]')))
            print(len(elements))
            for element in elements:
                group_name = element.find_element(By.XPATH, './/span[@class="name"]').text
                print(group_name)
                if group_name not in groups:
                    groups.append(group_name)
                    try:
                        try: 
                            element.find_element(By.XPATH, './/a[@class="description left members"]').click()
                        except:
                            ActionChains(self.driver).move_to_element(elements[-1]).perform()
                            element.find_element(By.XPATH, './/a[@class="description left members"]').click()
                        time.sleep(2)
                        members = WebDriverWait(self.driver, timeout=2).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="chat-box-member__info v2"]')))
                        for member in members:
                            members_name = member.get_attribute("title")
                            insert_table(conn=conn, table='Nhom',
                                        columns=['group_name', 'member_name', 'state'],
                                        values=[group_name, members_name, 'unknow'],
                                        realtime = False)
                        conn.commit()   
                        groups.append(group_name)
                        self.driver.find_element(By.XPATH, '//i[@class="fa fa-close f16 pre"]').click()
                    except:
                        pass
    def add_friend_from_members(self, ID):
        # connect SQL
        conn = create_connection(PATH+ "/database/database_Nhom.db")
        keys = random.choice(open_txt(PATH + '/settings/ListMessSpam.txt'))
        group_name, member_name =  select_get_value(conn=conn,
                                                    table= "Nhom",
                                                    id= int(ID),
                                                    column="group_name, member_name")
        if (member_name == None) | (member_name == ''):
            return "Không tìm ra"
        elif  (member_name == 'Tài khoản bị khóa') | (member_name == 'Account Banned'):
            return "Tài khoản bị khóa"
        # switch to list groups
        self.switch_to_groups()
        # find group by group_name
        try:
            WebDriverWait(self.driver, timeout=1).until(EC.presence_of_element_located(
                    (By.XPATH, '//i[@class="fa fa-filter-icon-clear zl-group-input__search__icon-clear zl-group-input__affix-wrapper__suffix-icon"]'))).click()
        except:
            pass
        WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located(
                (By.XPATH, f'//input[@placeholder="Tìm nhóm"]'))).send_keys(group_name)
        time.sleep(0.5)
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(
                (By.XPATH, '//a[@class="description left members"]'))).click()
        # find group by group_name
        try:
            WebDriverWait(self.driver, timeout=1).until(EC.presence_of_element_located(
                    (By.XPATH, '//i[@class="fa fa-filter-icon-clear zl-group-input__search__icon-clear zl-group-input__affix-wrapper__suffix-icon"]'))).click()
        except:
            pass
        WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located(
                (By.XPATH, f'//input[@placeholder="Tìm nhóm"]'))).send_keys(group_name)
        time.sleep(0.5)
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(
                (By.XPATH, '//a[@class="description left members"]'))).click()
        # find member and send text
        try:
            try:
                WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located((By.XPATH, f'//div[@title="{member_name}"]'))).click()
            except:
                element = WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located((By.XPATH, f'//div[@title="{member_name}"]')))
                ActionChains(self.driver).move_to_element(element).perform()
                WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located((By.XPATH, f'//div[@title="{member_name}"]'))).click()
                
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-id="btn_UserProfile_SendMsg"]'))).click()
            # for i in keys:
            self.driver.switch_to.active_element.send_keys(keys)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            try:
                try:
                    self.driver.find_element(By.XPATH, f'//div[@data-id="div_LastReceivedMsg_Text"]')
                    output = "Chưa thể nhắn tin"
                except:
                    error3 = self.driver.find_element(By.XPATH, f'//div[@class="chat-message__actionholder  me  last-msg has-status "]/ancestor::div[@class="card  me  last-msg has-status  card--text"]')
                    error3.find_element(By.XPATH, './/*[contains(text(), "Gửi lỗi")]')
                    output = "Bị chặn spam tạm thời"
            except:
                output = "Nhắn tin thành công"
        except:
            self.driver.find_element(By.XPATH, '//i[@class="fa fa-close f16 pre"]').click()
            output = "Nhắn tin không thành công"
            pass
        # add friend
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(ADD_MEMBER)).click()
            output = "Gửi kết bạn thành công," + output
        except:
            status = "Đã kết bạn"
            
        update_table(conn= conn,
                    table= "Nhom",
                    columns=["status","state"],
                    values= [status, output],
                    column_where= "id",
                    value_where= int(ID))
        return output
    
    def send_mess_to_members(self, ID):
        # connect SQL
        conn = create_connection(PATH+ "/database/database_Nhom.db")
        keys = random.choice(open_txt(PATH + '/settings/ListMessSpam.txt'))
        group_name, member_name =  select_get_value(conn=conn,
                                                    table= "Nhom",
                                                    id= int(ID),
                                                    column="group_name, member_name")
        if (member_name == None) | (member_name == ''):
            return "Không tìm ra"
        elif  (member_name == 'Tài khoản bị khóa') | (member_name == 'Account Banned'):
            return "Tài khoản bị khóa"
        
        # switch to list groups
        self.switch_to_groups()
        # find group by group_name
        try:
            WebDriverWait(self.driver, timeout=1).until(EC.presence_of_element_located(
                    (By.XPATH, '//i[@class="fa fa-filter-icon-clear zl-group-input__search__icon-clear zl-group-input__affix-wrapper__suffix-icon"]'))).click()
        except:
            pass
        WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located(
                (By.XPATH, f'//input[@placeholder="Tìm nhóm"]'))).send_keys(group_name)
        time.sleep(0.5)
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(
                (By.XPATH, '//a[@class="description left members"]'))).click()
        # find member
        try:
            try:
                WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located((By.XPATH, f'//div[@title="{member_name}"]'))).click()
            except:
                element = WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located((By.XPATH, f'//div[@title="{member_name}"]')))
                ActionChains(self.driver).move_to_element(element).perform()
                WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located((By.XPATH, f'//div[@title="{member_name}"]'))).click()
                
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-id="btn_UserProfile_SendMsg"]'))).click()
            # for i in keys:
            self.driver.switch_to.active_element.send_keys(keys)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            try:
                try:
                    self.driver.find_element(By.XPATH, f'//div[@data-id="div_LastReceivedMsg_Text"]')
                    output = "Chưa thể nhắn tin"
                except:
                    error3 = self.driver.find_element(By.XPATH, f'//div[@class="chat-message__actionholder  me  last-msg has-status "]/ancestor::div[@class="card  me  last-msg has-status  card--text"]')
                    error3.find_element(By.XPATH, './/*[contains(text(), "Gửi lỗi")]')
                    output = "Bị chặn spam tạm thời"
            except:
                output = "Nhắn tin thành công"
        except:
            self.driver.find_element(By.XPATH, '//i[@class="fa fa-close f16 pre"]').click()
            output = "Nhắn tin không thành công"
            pass
        update_table(conn= conn,
                    table= "Nhom",
                    columns=["state"],
                    values= [output],
                    column_where= "id",
                    value_where= int(ID))
        return output
        
    def find_phonenumber(self, phone_number):
        WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(CONTACT_SEARCH_INPUT)).send_keys(phone_number)
        sleep_short()
        if ERR0R_NOTFOUND in self.driver.page_source:
            return "Số điện thoại không dùng zalo"
        elif ERROR_MAXIMUM_SEARCH in self.driver.page_source:
            return "Quá số lần tìm kiếm"
        else:
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            # Add friends
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            return "HAD-FOUND"
    
    def add_friend_from_phonenumbers(self,  ID):
        # connect SQL
        conn = create_connection(PATH+ "/database/database_SDT.db")
        keys = random.choice(open_txt(PATH + '/settings/ListMessSpam.txt'))
        phonenumber =  select_get_value(conn=conn,
                                        table= "SDT",
                                        id= int(ID),
                                        column="phone_or_url")
        
        # find phone number
        out = self.find_phonenumber(phonenumber)
        print(out)
        if out == "HAD-FOUND":
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(CHAT_INPUT)).click()
            self.driver.switch_to.active_element.send_keys(keys)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            try:
                try:
                    self.driver.find_element(By.XPATH, f'//div[@data-id="div_LastReceivedMsg_Text"]')
                    output = "Chưa thể nhắn tin"
                except:
                    error3 = self.driver.find_element(By.XPATH, f'//div[@class="chat-message__actionholder  me  last-msg has-status "]/ancestor::div[@class="card  me  last-msg has-status  card--text"]')
                    error3.find_element(By.XPATH, './/*[contains(text(), "Gửi lỗi")]')
                    output = "Bị chặn spam tạm thời"
            except:
                output = "Nhắn tin thành công"
            # add friend
            try:
                WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(ADD_MEMBER)).click()
                output = "Gửi kết bạn thành công," + output
            except:
                status = "Đã kết bạn"
        else:
            output = out
        try:
            self.driver.find_element(By.XPATH, '//i[@class="fa fa-textbox-icon-clear btn clickable close-spinner"]').click()
        except:
            pass
        update_table(conn= conn,
                    table= "SDT",
                    columns=["status","state"],
                    values= [status, output],
                    column_where= "id",
                    value_where= int(ID))
        
    def send_mess_to_phonenumbers(self, ID):
        # connect SQL
        conn = create_connection(PATH+ "/database/database_SDT.db")
        keys = random.choice(open_txt(PATH + '/settings/ListMessSpam.txt'))
        phonenumber =  select_get_value(conn=conn,
                                        table= "SDT",
                                        id= int(ID),
                                        column="phone_or_url")
        
        # find phone number
        out = self.find_phonenumber(phonenumber)
        print(out)
        if out == "HAD-FOUND":
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(CHAT_INPUT)).click()
            self.driver.switch_to.active_element.send_keys(keys)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            try:
                try:
                    self.driver.find_element(By.XPATH, f'//div[@data-id="div_LastReceivedMsg_Text"]')
                    output = "Chưa thể nhắn tin"
                except:
                    error3 = self.driver.find_element(By.XPATH, f'//div[@class="chat-message__actionholder  me  last-msg has-status "]/ancestor::div[@class="card  me  last-msg has-status  card--text"]')
                    error3.find_element(By.XPATH, './/*[contains(text(), "Gửi lỗi")]')
                    output = "Bị chặn spam tạm thời"
            except:
                output = "Nhắn tin thành công"
        else:
            output = out
        try:
            self.driver.find_element(By.XPATH, '//i[@class="fa fa-textbox-icon-clear btn clickable close-spinner"]').click()
        except:
            pass
        update_table(conn= conn,
                    table= "SDT",
                    columns=["state"],
                    values= [output],
                    column_where= "id",
                    value_where= int(ID))
        return output
        
        
        

        