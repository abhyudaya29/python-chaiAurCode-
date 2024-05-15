import requests
def fetch_random_user_free_api():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()
    print(data,"Fetched data")
    if data["success"] and "data" in data:
        user_data=data["data"]
        userName=user_data["login"]["username"]
        return userName
    else:
        raise Exception("Failed to fetch user data")
def main():
    try:
        userName=fetch_random_user_free_api()
        print(userName,">>username")
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()

