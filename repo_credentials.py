from os import system
from colorama import Fore,Style
import yaml


def setCredentials(username, password):
    repos = None
    #Read SSH File
    with open('kamayuc-erc-ssh.repos','r') as file:
        repos = yaml.load(file, Loader=yaml.FullLoader)
        for key, value in repos['repositories'].items():
            url = "@"+value['url'].split('@')[1]
            value['url'] = "https://" +username + ":" + password + url
            print(value['url'])
    
    #Write HTTPS File
    with open('kamayuc-erc.repos','w') as file:
        yaml.dump(repos,file,default_flow_style=False)


        


while True:
    
    # Clear terminal
    system('clear')

    # Get username
    print(f"{Fore.BLUE}Insert your Gitlab Username:{Style.RESET_ALL}")
    username = input()

    # Get password
    print(f"{Fore.BLUE}Insert your password:{Style.RESET_ALL}")
    password = input()
    
    system('clear')
    # Verify credentials
    print(f"{Fore.MAGENTA}Check your credentials:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Username:{Style.RESET_ALL} " + username)
    print(f"{Fore.CYAN}Password:{Style.RESET_ALL} " + password)
    print(f"{Fore.YELLOW}Please be sure , this could affect your docker installation{Style.RESET_ALL}")
    print(f"These are your credentials? Write{Fore.CYAN}[yes/no/cancel]{Style.RESET_ALL}")
    answer = input()

    if(answer == "yes"):
        setCredentials(username, password)
        break
    elif(answer == "no"):
        continue
    elif(answer == "cancel"):
        break
