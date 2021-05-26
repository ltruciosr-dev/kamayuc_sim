from os import system
import yaml


def setCredentials(username, password):
    repos = None
    #Read SSH File
    with open('kamayuc-erc-ssh.repos','r') as file:
        repos = yaml.load(file, Loader=yaml.FullLoader)
        for key, value in repos['repositories'].items():
            url = "@gitlab.com/"+value['url'].split(':')[1]
            value['url'] = "https://" + username + ":" + password + url
            print(value['url'])
    
    #Write HTTPS File
    with open('kamayuc-erc.repos','w') as file:
        yaml.dump(repos,file,default_flow_style=False)


while True:
    # Clear terminal
    system('clear')

    # Get username
    print("Insert your Gitlab Username:")
    username = input()

    # Get password
    print("Insert your password:")
    password = input()
    
    system('clear')
    # Verify credentials
    print("Check your credentials:")
    print("Username:" + username)
    print("Password:" + password)
    print("Please be sure , this could affect your docker installation")
    print("These are your credentials? Write[yes/no/cancel]")
    answer = input()

    if(answer == "yes"):
        setCredentials(username, password)
        break
    elif(answer == "no"):
        continue
    elif(answer == "cancel"):
        break
