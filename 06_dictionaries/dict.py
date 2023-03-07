favorite_languages = {
                        'jen': 'python',
                        'sarah': 'c',
                        'edward': 'ruby',
                        'phil': 'python',
                    }
friends = ['phil', 'sarah']

for name in favorite_languages:
    print( name.title()  )
    print()
    if name in friends:
        print( "Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!" )
        print()




alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# list of dictionaries
aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)



favorite_languages = {
                        'jen': ['python', 'ruby'],
                        'sarah': [],
                        'edward': ['ruby', 'go'],
                        'phil': ['python', 'haskell'],
                        'juampa': ['php','python','java','c#', 'c++']
                    }

for name, languages in favorite_languages.items():
    if len(languages) == 0:
        print( name.title() + " dont have favorite language" )
    elif len(languages) > 4:
        print( name.title() + " have a lot of favorites languages..." )
    else:
        print( name.title() + "'s favorite languages are:" )
        for language in languages:
            print( "\t" + language.title() )
    print()
