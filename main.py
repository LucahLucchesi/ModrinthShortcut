import requests

modrinth_url = 'https://api.modrinth.com/v2/project/'

# all mods listed are client-side and do not impact the vanilla experience
mod_list = {
    'fabric_api': 'P7dR8mSH',
    'mod_menu': 'NNAgCjsB',
    'sodium': 'AANobbMI', # general optimization
    'sodium_extra': 'PtjYWJkn', # extra sodium options
    'lithium': 'gvQqBUqZ', # tick optimization
    'ferrite_core': 'uXXizFIs', # memory optimization
    'entity_culling': 'NNAgCjsB', # entity rendering optimization
    'iris': 'YL57xq9U', # shaders
}

def main():
    # gets the version list for each mod and prints the download link for latest version
    for mod in mod_list:
        try:
            versions = requests.get(modrinth_url + mod_list[mod] + '/version').json()
            latest_ver = versions[0]
            print(mod + ": " + latest_ver['files'][0]['url'])
        except:
            print("Error: " + mod + " not found.")


if __name__ == "__main__":
    main()