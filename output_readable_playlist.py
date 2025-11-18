make_playlist=input('would you like to make a playlist? y/n: ')
if make_playlist!='y':
    print('okay, see you later then')
elif make_playlist=='y':
    while True:
        try:
            playlist_length=int(input('how many songs would you like in your playlist?\nplease only type an integer: '))
            break
        except ValueError:
            print('that is not an integer.')
    playlist_titles=[0]
    playlist_artists=[0]
    playlist_genres=[0]
    playlist_durations=[0]
    deleted_songs=[]
    total_time=0
    for songz in range(1,playlist_length+1):
        if len(playlist_titles)<2:
            title=input('what\'s your song called? ')
            while True:
                try:
                    if title=='':
                        raise ValueError('please type something:')
                except ValueError as err:
                    title=input(f'{err}\nwhat\'s your song called? ')
                else:
                    playlist_titles.append(title)
                    break
        else:
            title=input('what\'s your next song called? ')
            while True:
                try:
                    if title=='':
                        raise ValueError('please type something:')
                except ValueError as err:
                    title=input(f'{err}\nwhat\'s your next song called? ')
                else:
                    playlist_titles.append(title)
                    break        
        artist=input('who made your song? ')
        while True:
            try:
                if artist=='':
                    raise ValueError('please type something:')
            except ValueError as err:
                artist=input(f'{err}\nwho made your song? ')
            else:
                playlist_artists.append(artist)
                break
        genre=input('what\'s the genre of your song? ')
        while True:
            try:
                if genre=='':
                    raise ValueError('please type something.')
            except ValueError as err:
                genre=input(f'{err}\nwhat\'s the genre of your song? ')
            else:
                playlist_genres.append(genre)
                break
        while True:
            try:
                duration=int(input('about how many minutes long is the song?\nplease only type an integer: '))
                playlist_durations.append(duration)
                total_time+=(duration)
                break
            except ValueError:
                print('that is not an integer.')
    #print(playlist_titles)
    #print(playlist_artists)
    #print(playlist_genres)
    #print(playlist_durations)
    #print(total_time)
    playlist={}
    for music in range(1,int(playlist_length)+1):
        playlist.update({f'song{music}':{'title':playlist_titles[music],'artist':playlist_artists[music],'genre':playlist_genres[music],'duration':f'{playlist_durations[music]} minute(s) or about {round((playlist_durations[music]/60),2)} hour(s)'}})
    print('your playlist is currently:')
    for mu,sic in playlist.items():
        print(f'{mu}: {sic}')
    print(f'your total playlist length is: about {total_time} minutes or about {round((total_time/60),2)} hour(s)')
    done=input('will that be all for now? y/n ')
    if done=='y':
        print('have a great day!')
    else:
        while done!='y':
            add_or_remove=input('would you like to add or remove songs? ')
            if add_or_remove=='add':
                while True:
                    try:
                        more_playlist_length=int(input('how many more songs would you like in your playlist?\nplease only type an integer: '))
                        break
                    except ValueError:
                        print('that is not an integer.')
                for songz in range(len(playlist_titles),more_playlist_length+len(playlist_titles)):
                    title=input('what\'s your next song called? ')
                    while True:
                        try:
                            if title=='':
                                raise ValueError('please type something:')
                        except ValueError as err:
                            title=input(f'{err}\nwhat\'s your next song called? ')
                        else:
                            playlist_titles.append(title)
                            break
                    artist=input('who made your song? ')
                    while True:
                        try:
                            if artist=='':
                                raise ValueError('please type something:')
                        except ValueError as err:
                            artist=input(f'{err}\nwho made your song? ')
                        else:
                            playlist_artists.append(artist)
                            break
                    genre=input('what\'s the genre? ')
                    while True:
                        try:
                            if genre=='':
                                raise ValueError('please type something.')
                        except ValueError as err:
                            genre=input(f'{err}\nwhat\'s the genre of your song? ')
                        else:
                            playlist_genres.append(genre)
                            break
                    while True:
                        try:
                            duration=int(input('about how many minutes long is the song?\nplease only type an integer: '))
                            playlist_durations.append(duration)
                            total_time+=duration
                            break
                        except ValueError:
                            print('that is not an integer.')                    
                #print(playlist_titles)
                #print(playlist_artists)
                #print(playlist_genres)
                #print(playlist_durations)
                #print(total_time)
                for music in range(len(playlist_titles),int(more_playlist_length)+len(playlist_titles)):
                    playlist.update({f'song{music-(1*int(more_playlist_length))}':{'title':playlist_titles[music-(1*int(more_playlist_length))],'artist':playlist_artists[music-(1*int(more_playlist_length))],'genre':playlist_genres[music-(1*int(more_playlist_length))],'duration':f'{playlist_durations[music-(1*int(more_playlist_length))]} minute(s) or about {round((playlist_durations[music-(1*int(more_playlist_length))]/60),2)} hour(s)'}})
                print('your playlist is currently:')
                for mu,sic in playlist.items():
                    print(f'{mu}: {sic}')
                print(f'your total playlist length is: about {total_time} minutes or about {round((total_time/60),2)} hours')
            elif add_or_remove=='remove':
                clear_playlist=input('do you want to clear/reset your playlist? y/n: ')
                if clear_playlist=='y':
                    confirmation=input('are you CERTAIN you want to CLEAR/RESET your playlist? y/n: ')
                    if confirmation=='y':
                        playlist.clear()
                        playlist_titles.clear()
                        playlist_artists.clear()
                        playlist_genres.clear()
                        playlist_durations.clear()
                        deleted_songs.clear()
                        total_time=0
                        print('your playlist is now empty')
                    else:
                        print('noted, your playlist will not be cleared.')
                else:
                    print('noted, your playlist will not be cleared.')
                    if len(deleted_songs)>=1:
                        check_deleted=input('would you like to check which songs you\'ve removed? y/n: ')
                        if check_deleted=='y':
                            for deleted in deleted_songs:
                                print(f'you have deleted song{deleted}: {playlist_titles[deleted]}, by {playlist_artists[deleted]}')
                        else:
                            print('alright, let\'s move past that.')
                    while True:
                        try:
                            remove_song=int(input('state the number corresponding to the song you\'d like to remove\nplease only type an integer: '))
                            if remove_song not in deleted_songs:
                                deleted_songs.append(remove_song)
                                total_time-=playlist_durations[remove_song]
                            else:
                                print('that song has already been removed.')
                            break
                        except ValueError:
                            print('that is not an integer.')
                        except IndexError:
                            print('that song is not in your playlist.')
                    for songz in list(playlist.keys()):
                        if songz.endswith(str(remove_song)):
                            del playlist[songz]
                #print(playlist_titles)
                #print(playlist_artists)
                #print(playlist_genres)
                #print(playlist_durations)
                #print(total_time)
                print('your playlist is currently:')
                for mu,sic in playlist.items():
                    print(f'{mu}: {sic}')
                print(f'your total playlist length is: about {total_time} minutes or about {round((total_time/60),2)} hours')
                if len(deleted_songs)>=1:
                    check_deleted=input('would you like to check which songs you\'ve removed? y/n: ')
                    if check_deleted=='y':
                        for deleted in deleted_songs:
                            print(f'you have deleted song{deleted}: {playlist_titles[deleted]}, by {playlist_artists[deleted]}')
                    else:
                        print('alright, let\'s move past that.')
            done=input('will that be all for now? y/n: ')
            if done=='y':
                print('have a great day!')
            else:
                print('aw shit, here we go again')