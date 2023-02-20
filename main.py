from random import randint
import json
import os
import stat
count = input("enter number of students\n")

def write_file(count):      #method 1 for save data
    names = []
    family = []
    ages = []
    avg = []
    for i in range(int(count)):
        name = input(f"name student {i} \n")
        names.append(name)
        famil = input(f"inter family student {i}\n")
        family.append(famil)
        ag = randint(10, 16)#input(f"inter age student {i}\n")
        ages.append(ag)
        av = randint(15, 19)#input(f"inter average student {i}\n")
        avg.append(av)
    all = {'name': names,
           'family': family,
           'ages': ages,
           'average': avg
           }
    with open('data.txt', 'w') as f:
        f.write(json.dumps(all))


def write_data2(count):
    for i in range(int(count)):
        name = input(f"enter name student: {i}\n")
        family = input(f"inter family student: {i}\n")
        avg = input(f"inter average student: {i}\n")
        alls= [name, family, avg]
        all = {
            f'student {i}': f'{alls}\n'
        }
        with open('data.txt', 'a') as s:
            s.write(json.dumps(all))


def read_file():
    with open('data.txt', 'r') as f:
        datas = f.read()

def search():
    inp = input("input search value\n")
    with open('data.txt','r') as f:
        if inp in f.read():
            print(f"{inp} found")
        else:
            print("not found")


def os_commands():  # permission error
    string = '#       ::2             localhostttttttttt'
    with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+') as h:
        hosts = h.write(string)

        #print(oct(os.stat(r'C:\Windows\System32\drivers\etc\hosts').st_mode))


if __name__ == '__main__':
    try:
        write_data2(count)
        print("#"*30)
        search()
    except Exception as e:
        print(e)