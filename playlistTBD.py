make_playlist=input('would you like to make a playlist? y/n: ')
if make_playlist!='y':
    print('okay, see you later then')
elif make_playlist=='y':
    playlist_length=(input('how many songs would you like in your playlist?\nplease only type an integer: '))
    playlist_songs=[0]
    playlist_artists=[0]
    playlist_genres=[0]
    playlist_durations=[0]
    total_time=0
    for songz in range(1,int(playlist_length)+1):
        if len(playlist_songs)<2:
            song=input('what\'s your song called? ')
            playlist_songs.append(song)
        else:
            song=input('what\'s your next song called? ')
            playlist_songs.append(song)
        artist=input('who made your song? ')
        playlist_artists.append(artist)
        genre=input('what\'s the genre? ')
        playlist_genres.append(genre)
        duration=int(input('about how many minutes long is the song?\nplease only type an integer: '))
        playlist_durations.append(duration)
        total_time+=(duration)
    print(playlist_songs)
    print(playlist_artists)
    print(playlist_genres)
    print(playlist_durations)
    print(total_time)
    playlist={}
    for music in range(1,int(playlist_length)+1):
        playlist.update({f'song{music}':playlist_songs[music],f'artist{music}':playlist_artists[music],f'genre{music}':playlist_genres[music],f'duration{music}':f'{playlist_durations[music]} minute(s) or about {round((playlist_durations[music]/60),2)} hour(s)'})
    print('your playlist is currently:',playlist)
    print(f'your total playlist length is: about {total_time} minutes or about {round((total_time/60),2)} hour(s)')
    done=input('will that be all for now? y/n ')
    if done=='y':
        print('have a great day!')
    elif done!='y':
        while done!='y':
            add_or_remove=input('would you like to add or remove songs? ')
            if add_or_remove=='add':
                more_playlist_length=input('how many more songs would you like in your playlist?\nplease only type an integer: ')
                for songz in range(len(playlist)+1,int(more_playlist_length)+len(playlist)+1):
                    song=input('what\'s your next song called? ')
                    playlist_songs.append(song)
                    artist=input('who made your song? ')
                    playlist_artists.append(artist)
                    genre=input('what\'s the genre? ')
                    playlist_genres.append(genre)
                    duration=int(input('about how many minutes long is the song?\nplease only type an integer: '))
                    playlist_durations.append(duration)
                    total_time+=duration
                print(playlist_songs)
                print(playlist_artists)
                print(playlist_genres)
                print(playlist_durations)
                print(total_time)
                for music in range(len(playlist)+1,int(more_playlist_length)+len(playlist)+1):
                    playlist.update({f'song{music}':playlist_songs[music],f'artist{music}':playlist_artists[music],f'genre{music}':playlist_genres[music],f'duration{music}':f'{playlist_durations[music]} minute(s) or about {round((playlist_durations[music]/60),2)} hour(s)'})
                print('your playlist is now:',playlist)
                print(f'your total playlist length is: about {total_time} minutes or about {round((total_time/60),2)} hours')
            elif add_or_remove=='remove':
                clear_playlist=input('do you want to clear your playlist? y/n: ')
                if clear_playlist=='y':
                    confirmation=input('are you CERTAIN you want to CLEAR your cart? y/n: ')
                    if confirmation=='y':
                        playlist=playlist.clear()
                        print('your playlist is now empty')
                    elif confirmation!='y':
                                    print('noted, your playlist will not be cleared')
                elif clear_playlist!='y':
                    print('noted, your playlist will not be cleared')
                remove_song=input('please state the number corresponding to the song you\'d like to remove: ')
                for songz in list(playlist.keys()):
                    if songz.endswith(remove_song):
                        del playlist[songz]
                total_time-=playlist_durations[int(remove_song)]
                print(playlist_songs)
                print(playlist_artists)
                print(playlist_genres)
                print(playlist_durations)
                print(total_time)
                print('your playlist is now:',playlist)
                print(f'your total playlist length is: about {total_time} minutes or about {round((total_time/60),2)} hours')
            done=input('will that be all for now? y/n ')
            if done=='y':
                print('have a great day!')
            elif done!='y':
                print('aw shit, here we go again')
