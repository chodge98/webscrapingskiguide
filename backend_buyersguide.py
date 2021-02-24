# Colin Hodge & Owein LaBarr
# CS021 - Final project
# Back end program that gathers information from evo.com on skis using selenium.
# Utilizes the predictability of the links on the website to create a link for each individual ski pair
##
# -----------------------------------------------
# final_ski_back_end.py was built by Colin Hodge 
# -----------------------------------------------
#
# Importing libraries
import urllib3
# Importing selenium libraries to open and scrape through a chrome web page
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

## Defining constants
# The start and end URL for every single link on the page we are using
BASE_URL = 'https://www.evo.com/shop/ski/skis/'
URL_ENDING = '/skis_no-bindings'
# All of the criteria required in a list
GENDERS = ['Male', 'Female']
ABILITY = ['Beginner-Intermediate', 'Intermediate-Advanced','Advanced-Expert']
TYPE = ['All Mountain', 'Park & Pipe', 'Powder', 'Alpine Touring']
PROFILE = ['Camber', 'Rocker', 'Rocker/Camber', 'Rocker/Camber/Rocker']

def main():
    'Calls to print gather_data()'
    print(gather_data())


def make_URL(gender, ability_level, ski_type, ski_profile):
    'Creates a URL based on the above conditons of a skier and what type of ski they are looking for'
    # Creating blank strings to iterate through
    gender_string = ''
    ability_string = ''
    type_string = ''
    profile_string = ''

    # If statement to add to the string based on the URL
    # For gender
    if gender == 'Male':
        gender_string = 'mens'
    elif gender == 'Female':
        gender_string = 'womens'
    else:
        print('GENDER ERROR')

    
    # For ability level
    if ability_level == 'Beginner-Intermediate':
        ability_string = 'ability_beginner-intermediate'
    elif ability_level == 'Intermediate-Advanced':
        ability_string = 'ability_intermediate-advanced'
    elif ability_level == 'Advanced-Expert':
        ability_string = 'ability_advanced-expert'
    else:
        print('ABILITY ERROR')

    # For ski type
    if ski_type == 'All Mountain':
        type_string = 'all-mountain'
    elif ski_type == 'Park & Pipe':
        type_string = 'park-pipe'
    elif ski_type == 'Powder':
        type_string = 'powder'
    elif ski_type == 'Alpine Touring':
        type_string = 'alpine-touring-2'
    else:
        print('TYPE ERROR')

    # For ski profile
    if ski_profile == 'Camber':
        profile_string = 'rocker_camber'
    elif ski_profile == 'Rocker':
        profile_string = 'rocker_rocker'
    elif ski_profile == 'Rocker/Camber':
        profile_string = 'rocker_rocker-camber'
    elif ski_profile == 'Rocker/Camber/Rocker':
        profile_string = 'rocker_rocker-camber-rocker'
    else:
        print('PROFILE ERROR')

        
    # Defining the final URL to be scraped from
    final_URL = BASE_URL + type_string + '/' + gender_string + '/' + ability_string + '/' + profile_string + URL_ENDING

    return final_URL



def ski_scraper(URL):
    'Using a previously built URL will scrape through evo.com and pair create a list of ski names paired with the link to it'
    chrome = webdriver.Chrome()
    chrome.get(URL)

    # Finding the requested items on the link by class name
    links = chrome.find_elements_by_class_name('product-thumb-link')
    ski_link_list = []

    # Adding found links to the list
    for i in links:
        ski_link_list.append(i.get_attribute('href'))

    # Finding specific ski names by class name
    ski_names = chrome.find_elements_by_class_name('product-thumb-title')
    ski_names_list = []

    # Adding the found names to the list
    for x in range(len(ski_names)):
        if ski_names[x].text != '':
            ski_names_list.append(ski_names[x].text)

    # Zipping the list of names and links together
    paired_list = list(zip(ski_names_list, ski_link_list))

    # Closing chrome after each iteration so that my computer doesn't explode with 100000 chrome tabs
    chrome.quit()

    return paired_list


def gather_data():
    'Creating a dynamic dictionary for every possible answer to the front end quiz'

    # Imbedded for loops to create dictionaries of the criteria 
    gender_dic = {}
    for g in GENDERS:

        ability_dic = {}
        for a in ABILITY:

            type_dic = {}
            for t in TYPE:

                profile_dic = {}
                for p in PROFILE:
                    # Building URLs for each of the criteria
                    url = make_URL(g, a, t, p)
                    list_of_skis = ski_scraper(url)
                    profile_dic[p] = list_of_skis
                    
                type_dic[t] = profile_dic
                
            ability_dic[a] = type_dic
            
        gender_dic[g] = ability_dic


    return gender_dic


# Running main()
main()       



  
        












    
    
