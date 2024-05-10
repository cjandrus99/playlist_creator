## Overview

**Project Title**: 

Playlist Creator

**Project Description**:

This simple python program utilizes a Firestore database to store data about playlists entered in the terminal by a user. The user makes a selection from a menu to create, edit, or delete that data. 

**Project Goals**:

The primary goal for this project was to learn how to perform CRUD operations on a cloud database. I am unfamiliar with cloud databases and how they work, and would like to learn how to simply utilize them in a basic python program. I also had a goal to refresh my knowledge on python as I started a programming class.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Open the program file
2. Firebase requires a private key JSON file. This is downloaded and stored locally, so the program needs to point to the location path of the private key JSON. 
3. Python and Firebase-admin need installed to run the program.
4. The program can then be run.

Instructions for using the software:

1. A welcome message and a menu is displayed in the terminal output. 
2. The user makes a selection as follows: (1) to create a new playlist, (2) to edit an existing playlist, (3) to delete a playlist, (4) to view all playlists in the database, and (5) to exit the program.
3. "exit" can be typed at any time to return to the main menu.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Install firebase with pip install firebase-admin
* Python

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Cloud Firestore Documentation](https://firebase.google.com/docs/firestore)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add a user login to save their particular playlists
* [ ] Maybe update from playlist creator to something like a finance tracker
* [ ] Improve menu navigation, maybe a GUI?
