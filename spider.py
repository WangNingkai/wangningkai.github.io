from requests import get


def updateGitfolio():
    api_url ='https://gitfolio.ningkai.wang'
    data = get(api_url).content
    print(data)
    open('index.html', 'wb').write(data)


if __name__ == "__main__":
    updateGitfolio()
