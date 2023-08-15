from selenium.webdriver.common.by import By

CONTACT_SEARCH_INPUT = (By.XPATH, '//input[@id="contact-search-input"]')
ADD_FRIEND1 = (By.XPATH, '//div[@data-translate-inner="STR_FRIEND_REQ_SEND"]')
ADD_FRIEND2 = (By.XPATH, '//div[@data-translate-inner="STR_PROFILE_ADD_FRIEND"]')
CHAT_INPUT = (By.XPATH, '//div[@class="rich-input empty"]')
ADD_MEMBER = (By.XPATH, '//div[@data-id="btn_Grp_AddMem"]')
CHOICE_PEOPLE = (By.XPATH, '//div[@class="flx flx-col create-group__phone-info  single-state"]')
ADD_MEMBER_BUTTON = (By.XPATH, '//div[@data-id="btn_AddMem_Finish"]')
ERROR_INBOX1 = "Bạn chưa thể gửi tin nhắn đến người này vì người này chặn không nhận tin nhắn từ người lạ"
ERROR_INBOX2 = "Không thể nhận tin nhắn từ bạn"
ERROR_INBOX3 = "Gửi lỗi"
ERROR_MAXIMUM_SEARCH = "Bạn đã tìm kiếm quá số lần cho phép"
ERR0R_NOTFOUND1 = "Số điện thoại chưa đăng ký tài khoản hoặc không cho phép tìm kiếm"
ERR0R_NOTFOUND2 = "Không tìm thấy"
SEND_PHOTO = (By.XPATH, '//div[@icon="chatbar-photo"]')