import instaloader

insta = instaloader.Instaloader()

username = input('Enter the username: ')

profile = instaloader.Profile.from_username(insta.context, username)


print("username: ", profile.username)
print("Number of posts ", profile.mediacount)
print("followers" ,profile.followers)
print("bio", profile.biography)
