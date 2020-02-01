from time import sleep
from secrets import pw

class Instabot_Youtube:
    #Initializing method
    def __init__(self, username, password):
        self.webDriver = webDriver.Chrome()
        #using wbedriver to contact DNS
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\.click()
        sleep(2)
        #Relation to keys "username" and "password"
        self.driver.find_element_by_xpath("//input[@name =\"username\"]")\.send_keys(username)
        self.driver.find_element_by_xpath("//input[@name =\"password\"]")\.send_keys(pw)
        seld.driver.find_element_by_xpath('//button[@type="submit"]')\.click()
        sleep(4)
        seld.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\.click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_bu_xpath("//a[contains(@href, '/{}')]".format(self.username))\.click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]")\.click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]")\.click()
        followers = self._get_names()
        #checks for names in following that are not in followers
        not_following_back = [user for user in following if user not in followers]

    def _get_names(self)
    #scrapes names from instagram website
        sleep(2)
        sugs = self.driver.find_element_bu_xpath('//h4[contains(test(), Suggestions)]')
        self.driver.execture_script('arguements[0].scrollInto()', sugs)
        sleep(2)
        scroll_box = self.driver.find_element_bu_xpath("/html/body/div[3]/div/div[2]")
        last_height, height = 0, 1
        while last_height != height:
            last_height = height
            sleep(1)
            height = self.driver.execute_script("""arguements[0].scrollTo(0, arguements[0].scrollHeight);
            return arguements[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        #to close
        self.driver.find_element_bu_xpath("/html/body/div[3]/div[1]/div/div[2]/button")\.click()
        return names

unFollowers = Instabot_Youtube('dhruv4102', password )
unFollowers.get_unfollowers()



#Credits to CodeDrip on Youtube
#Created for the purpose of learning about the selenium module & because relevancy of social media
