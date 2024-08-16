import requests

modrinth_url = 'https://api.modrinth.com/v2/project/'

# dictionary of mod id's
mod_list = {
    'fabric_api': 'P7dR8mSH',
    'sodium': 'AANobbMI'
}

def main():
    # gets the version list for each mod and prints the download link for latest version
    for mod in mod_list:
        versions = requests.get(modrinth_url + mod_list[mod] + '/version').json()
        latest_ver = versions[0]
        print(mod + ": " + latest_ver['files'][0]['url'])

if __name__ == "__main__":
    main()