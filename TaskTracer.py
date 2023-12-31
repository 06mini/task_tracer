import json
import datetime

def selection():

        i = int(input("\n\nselect number |record today[1]| result today[2]|: "))
        if i ==1:
            return excecute_main(write)
        
        elif i == 2:
            return computing(read)
        
        else:
            print("try again\n")
            return selection()

def excecute_main(write_data):
        data = read_json(file_path)
        if not data:
            data = {}
        if now not in data:
            data[now] = {"rate": [], "tasks": []}
            
        for i in range(7,21+1):
            if i > 12 :
                i-=12
                performed_tasks = input(f"\nwhat did you do until {i} AM?: ").strip().split(",")
                write_data[now]["rate"].extend(performed_tasks)

            rate = input("\nrate[1~10]: ")
            write_data[now]["tasks"].extend(int(rate))    
        else:
            performed_tasks = input(f"\nwhat did you do until {i}?: ").strip().split(",")
            write_data[now]["rate"].extend(performed_tasks)

            rate = input("\nrate[1~10]: ")
            write_data[now]["tasks"].extend(rate)

    

def computing(read_data):
    sum = 0
    try:
        for i in read_data[now]["rate"]:
            sum +=i
        average = sum / 14

        print(f"average rate is {average}")
    
    except:
        print("there is no connected data")
      
def read_json(file_path):
    try:
        with open(file_path, "r") as file:
            json_file = json.load(file)
            return json_file
        
    except FileExistsError:
        print("check your json file matherfuker.")
 
    except FileNotFoundError:
        print("your file was not detected asshole. fix it")

    except ValueError:
        print("I don't know what is wrong, but you need to fix it")

def write_json(file_path,data):
    try:
        with open(file_path, "w") as file:
            json.dump(data,file)

        
    except FileExistsError:
        print("check your json file matherfuker.")
 
    except FileNotFoundError:
        print("your file was not detected asshole. fix it")

    except ValueError:
        print("I don't know what is wrong, but you need to fix it")



    





file_path = "history.json"
now = datetime.datetime.now().strftime("%Y-%m-%d")

write = write_json(file_path,now)
read = read_json(file_path)

selection()
