import requests
import json

def get_request(url:str = "https://127.0.0.1:8000"):
    response = requests.get(url = url)
    print(response.json())

def post_request(data: dict, url:str = "https://127.0.0.1:8000"):
    response = requests.post(url = url, json=data)
    print(response.json())
    
def put_request(data: dict, url:str = "https://127.0.0.1:8000"):
    response = requests.put(url = url, json = data) 
    print(response.json())
    
def delete_request(data: dict, url:str = "https://127.0.0.1:8000"):
    response = requests.delete(url = url, json = data)
    print(response.json())
    

def main():
    url = "http://127.0.0.1:8000" 
    while True:

        user_input = input("Request: ")
        if user_input == "q":
            break

        user_input = user_input.split()
       
        if user_input[0].upper() not in ["GET", "POST", "PUT", "DELETE"]:
            print("Invalid request! Please try again")
            continue
        request_type = user_input[0].upper()
        try:
            if not user_input[1].startswith("/"):
                print("Invalid request path! Please try again")
                continue
            request_path = user_input[1]
            url_with_path = url + request_path
        except:
            print("Invalid request path! Please try again")
            continue
        if len(user_input) > 2:
            try: 
                user_input[2] = " ".join(user_input[2:])
                body = user_input[2]
                id = int(body.split()[0])
            except:
                print("Invalid id! Please try again")
            try:
                activity = body.split()[1:]
                activity = " ".join(activity)
                data = {"id": id, "activity": activity}
            except:
                activity = None
        else:
            activity = None 
        
        if request_type == "GET":
            get_request(url_with_path)
            continue
        
        elif request_type == "POST":
            if activity is None:
                print("Activity missing! Please try again")
                continue
            if activity == "":
                print("Activity missing! Please try again")
                continue
            post_request(data = data, url = url_with_path)
            continue
        
        elif request_type == "PUT":
            if activity == None:
                print("Activity missing! Please try again")
                continue
            if activity == "":
                print("Activity missing! Please try again")
                continue
            put_request(data = data, url=url_with_path)
            continue
        
        elif request_type == "DELETE":
            delete_request(data = data, url=url_with_path)
            continue
        

        
    

if __name__ == "__main__":
    main()