import firebase_admin
from firebase_admin import credentials, firestore

# reference the firebase private key JSON that authorizes the program to write to the database
cred = credentials.Certificate(r"C:\Users\cjand\OneDrive - BYU-Idaho\CSE 310\Sprint 1\playlist-creator-e00d4-firebase-adminsdk-eny5a-e1fc3cbefa.json")
firebase_admin.initialize_app(cred)

# store the firestore call as the variable db
db = firestore.client()

class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"{self.title} by {self.artist}"

# start playlist class and define the functions for add, remove, and display.
class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, title, artist):
        track = Track(title, artist)
        self.tracks.append(track)

    def remove_track(self, title):
        for track in self.tracks:
            if track.title == title:
                self.tracks.remove(track)
                return
        print("Track not found in the playlist.")

    def display_tracks(self):
        print(f"Tracks in {self.name} playlist:")
        for i, track in enumerate(self.tracks, start=1):
            print(f"{i}. {track}")

    def to_dict(self):
            return {
                "name": self.name,
                "tracks": [str(track) for track in self.tracks]
            }

# define the create playlist function, where user input is the name of the playlist
def create_playlist():
    print("Type 'exit' to return to the main menu at any time.")
    while True:
        name = input("Enter the name of the playlist: ")
        if name == 'exit':
            break
        else:
            playlist = Playlist(name)
            # add playlist name to firestore db
            playlist_ref = db.collection("playlists").document(name)
            playlist_ref.set(playlist.to_dict())
            print(f"Playlist '{name}' created successfully.")

# define the edit playlist function, where user input allows adding or removing tracks
def edit_playlist():
    print("Type 'exit' to return to the main menu at any time.")
    while True:
        name = input("Enter the name of the playlist you want to edit: ")
        playlist_ref = db.collection("playlists").document(name)
        playlist_doc = playlist_ref.get()
        if playlist_doc.exists:
            playlist_data = playlist_doc.to_dict()
            playlist = Playlist(playlist_data['name'])
            for track_str in playlist_data['tracks']:
                title, artist = track_str.split(" by ")
                playlist.add_track(title, artist)
            action = input("Enter 'add' to add a track or 'remove' to remove a track: ")
            if action == 'add':
                title = input("Enter the title of the track to add: ")
                artist = input("Enter the artist of the track to add: ")
                playlist.add_track(title, artist)
                print(f"'{title}' by '{artist}' added to '{name}' successfully.")
            elif action == 'remove':
                title = input("Enter the title of the track to remove: ")
                playlist.remove_track(title)
                print(f"'{title}' by '{artist}' removed from '{name}' successfully.")
            else:
                print("Invalid action.")
            playlist_ref.set(playlist.to_dict())
        elif name == 'exit':
            break
        else:
            print("Playlist not found.")

def delete_playlist():
    print("Type 'exit' to return to the main menu at any time.")
    while True:
        name = input("Enter the name of the playlist you want to delete: ")
        playlist_ref = db.collection("playlists").document(name)
        playlist_doc = playlist_ref.get()
        if playlist_doc.exists:
            playlist_ref.delete()
            print(f"Playlist '{name}' deleted successfully.")
        elif name == 'exit':
            break
        else:
            print("Playlist not found.")

def view_playlists():
    print("Stored playlists:")
    playlists_ref = db.collection("playlists")
    playlists = playlists_ref.stream()
    for playlist in playlists:
        print(playlist.id)

def display_tracks():
    name = input("Enter the name of the playlist to view its tracks: ")
    playlist_ref = db.collection("playlists").document(name)
    playlist_doc = playlist_ref.get()
    if playlist_doc.exists:
        playlist_data = playlist_doc.to_dict()
        playlist = Playlist(playlist_data['name'])
        for track_str in playlist_data['tracks']:
            title, artist = track_str.split(" by ")
            playlist.add_track(title, artist)
        playlist.display_tracks()
    else:
        print("Playlist not found.")
    

print("\n~ Welcome to PLAYLIST CREATOR ~")
print("This program allows you to insert, modify, delete, and retrieve data from a cloud database.")

def main():
    while True: 
        print("\n------------- MENU -------------")
        print("| 1) Create a new playlist     |")
        print("| 2) Edit an existing playlist |")
        print("| 3) Delete a playlist         |")
        print("| 4) View all playlists        |")
        print("| 5) View playlist tracks      |")
        print("| 6) Exit the program          |")
        print("--------------------------------")
        
        choice = input("To begin, please type the number of your selection: ")

        if choice == '1':
            create_playlist()
        elif choice == '2':
            edit_playlist()
        elif choice == '3':
            delete_playlist()
        elif choice == '4':
            view_playlists()
        elif choice == '5':
            display_tracks()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()