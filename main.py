import requests


def looky():
    ac = open('admin.txt','r')
    print("\n\t    Domain giriniz. Not! http ve ya https yazmayin\n")
    link = input("> ")
    print("\nBasliyoruzz ..\n")

    while True:
        links = ac.readline()
        deneme = f'http://{link}/{links}'
        try:
            loky = requests.get(deneme)
            if loky.status_code == 200 or loky.status_code == 305:
                print(f"Giris paneli: {deneme}")
                break
        except requests.exceptions.ConnectionError:
            continue




def boom():
    print('''
 
                       $$$$$$$$$$$$$$$$$$$$$$$$$
                       $$$$$$$$$$$$$$$$$$$$$$$$$
                       $$$$$'`$$$$$$$$$$$$$'`$$$
                       $$$$$$  $$$$$$$$$$$  $$$$
                       $$$$$$$  '$/ `/ `$' .$$$$
                       $$$$$$$$. i  i  /! .$$$$$
                       $$$$$$$$$.--'--'   $$$$$$
                       $$^^$$$$$'        J$$$$$$
                       $$$   ~""   `.   .$$$$$$$
                       $$$$$e,      ;  .$$$$$$$$
                       $$$$$$$$$$$.'   $$$$$$$$$
                       $$$$$$$$$$$$.    $$$$$$$$
                       $$$$$$$$$$$$$     $$$$$$$
                       -------------------------
                           Admin Panel Finder
                           Coded by ghetto23
                          github.com/ghetto23
                       -------------------------
 ''')


if __name__ == '__main__':
    boom()
    looky() 



        
