import requests


def main():
    search_text = input('Enter movie to search: ')
    apikey = 'aa9e49f'
    url = f'https://omdbapi.com/?s={search_text}&apikey={apikey}'
    resp = requests.get(url)

    if resp.status_code != 200:
        print('something went wrong')
        print(resp.text)
        exit(1)

    data = resp.json()
    print(f'Total {data['totalResults']} movies found')
    movies = data['Search']

    for each_movie in movies:
        print(each_movie['Title'])



if __name__ == '__main__':
    main()

