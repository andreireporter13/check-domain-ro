#
#   Author: Andrei C. Cojocaru
#   LinkedIn profile: https://www.linkedin.com/in/andrei-cojocaru-985932204/
#   Site: https://webautomation.ro
#
# ### ### ### ### ### ### ### ### ### ### ### ### ###
# 
#   New automation script Powered by webautomation.ro; 
#
#
#   important library for this script is python-whois;
#
import whois
# 
#
#   import requests and bs4 for HTML elements; 
# 
import requests
from bs4 import BeautifulSoup
#
#
#
#   import another needed libraries; 
#
from time import sleep
#
#
#   import library for beautiful introduction screen; 
from termcolor import colored
from pyfiglet import Figlet
from pyfiglet import figlet_format
# 
#   
#
#   time to begin an application;
#
#
#   function with number_1 ---> gather data if domain available or not; 
#
def get_domain_data_from_registrar(domain_name):

    ''' Function Documentation: 

    This function return data about domain, return: 'valabil - poate fi cumparat si
        nevalabil - nu poate fi cumparat; 

    '''

    # this part of code open site cheker for availability, will check with python-whois;
    #
    flags = 0
    flags = flags | whois.NICClient.WHOIS_QUICK
    
    domain_info_registrar = whois.whois(domain_name, flags=flags)

    return domain_info_registrar.registrar

    

# function with number_2 ----> define a function for check creation date, if it need;
#
def get_domain_creation_date(domain_name):

    ''' Function Documentation: 

    This function return creation date for any .ro domain

    ''' 
    flags = 0
    flags = flags | whois.NICClient.WHOIS_QUICK
    
    domain_info_creation_date = whois.whois(domain_name, flags=flags)

    return f' Domeniul a fost creat la data de {domain_info_creation_date.creation_date}'


# function with number_3 ----> define expiration domain name;
#
def get_expiration_domain_date(domain_name):

    ''' Function Documentation: 

    This function return a expiration date for any .ro domain;

    ''' 

    flags = 0
    flags = flags | whois.NICClient.WHOIS_QUICK
        
    domain_info_expiration_date = whois.whois(domain_name, flags=flags)

    return f' Domeniul expira: {domain_info_expiration_date.expiration_date}'


# function with number_4 ----> get data from domain: status code, soup.title.text and more; 
#
def get_data_from_site(domain_name):

    ''' Function Documentation 

    This function return info from domain, if it available return status 200, 
        and soup.title.text and meta information; 

    ''' 
    response = requests.get('https://' + domain_name)
    soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code: 
        return f'Numele site-ului: >>>>> {soup.p.text} <<<<< - iar sloganul: >>>>> {soup.title.text} <<<<<'
    else: 
        return f'Domeniul {domain_name} nu are nicio interfata.'
                

# define main() function for logic of code; 
#
def main():

    ''' Function Documentation: 

    This function for logic of code. It is heart of my application; 

    ''' 

    introduction = Figlet(font = 'big')
    print(colored(introduction.renderText('Powered by:'), 'green'))
    print(figlet_format("webautomation.ro", font = "banner3", width = 600))

    print('1: By-default - Verifica daca domeniul este sau nu disponibil.')
    print('2: Verifica cand a fost creat domeniul, daca aceasta nu este disponibil.')
    print('3: Verifica cand expira domeniul, daca acesta nu este disponibil.')
    print('4: Vezi titlul si sloganul site-ului.')
    print('0: Exit.')
    print()


    input_from_user = input('Scrie un domeniu pentru verificare, fara "https://": ')
    print()

    # if 'https://' not in domain_input_from_user and domain_input_from_user.endswith('.ro'): 
    check_domain = get_domain_data_from_registrar(input_from_user)

    if check_domain != None: 
        print(f'Domeniul >>> {input_from_user} <<< este indisponibil!') 
        print()   

        while True: 

            new_user_input = int(input('Vezi si alte informatii, alegand cifra corespunzatoare: '))
            print()

            # this function is about the logic of user input;
            #
            if new_user_input == 0 or 1  < new_user_input < 5: 
            
                if new_user_input == 2: 
                    print(get_domain_creation_date(input_from_user))
                    print()
                    continue
                    
                elif new_user_input == 3: 
                    print(get_expiration_domain_date(input_from_user))
                    print()
                    continue 

                elif new_user_input == 4: 
                    print(get_data_from_site(input_from_user))
                    print()
                    continue 

                elif new_user_input == 0:
                    break

            else: 
                print('Ai introdus o cifra necorespunzatoare. Daca vrei sa iesi, introduci 0.')
                print()
        

    else: 
        print(f'Super! Domeniul >>> {input_from_user} <<< este disponibil. Cumpara-l mai repede!')
        print()
        

# if __name__ == '__main__' ---> run functions as an independent function; 
#
if __name__ == "__main__":
    main()

