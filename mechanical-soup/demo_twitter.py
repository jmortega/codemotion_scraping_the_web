import mechanicalsoup
import getpass

if __name__ == "__main__":

    URL = "https://twitter.com/login"
    
    username = raw_input ("Username: ")
    password = getpass.getpass()

    # Create a browser object
    browser = mechanicalsoup.Browser()

    # request Twitter login page
    login_page = browser.get(URL)

    # we grab the login form
    login_form = login_page.soup.find("form", {"class":"signin"})

    # find login and password inputs
    login_form.find("input", {"name": "session[username_or_email]"})["value"] = username
    login_form.find("input", {"name": "session[password]"})["value"] = password

    # submit form
    response = browser.submit(login_form, login_page.url)
	
	
    # verify we are now logged in ( get username in webpage )
    user = response.soup.find("span", { "class" : "u-linkComplex-target" }).string

    if username in user:
        print("You are connected as " + username)
    else:
        print("Not connected")