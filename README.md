## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies

## Dependency Management

The `JAVA DEPENDENCIES` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-pack/blob/master/release-notes/v0.9.0.md#work-with-jar-files-directly).

## TODO
Battleship

MENU
-----------------------------------------------------------------------------------------------------
#	(or) Start as server
#		V Print IP and PORT

#	(or) Start as client
#		Insert IP and PORT
#		Connect to server

#	Check if both are connected = true or if connection established from server only	
PLACEBOATS
-----------------------------------------------------------------------------------------------------
#    Insert coordinates

#		Check if valid coords
	
#			Coords are in table

#			Control boat place
#				Not over the edge (boat lenght)
#				Not overlap
#				Not around other boat

#    Remove boat from list

#    End placing status ready = true
#		
#	Check if both are ready = true
START PLAYING
-----------------------------------------------------------------------------------------------------
#	Random turn choice
#		Server generate random number for the turn
#	Shot
#		Insert coords
#		Send to client coords

#	ResponseShot
#		Client receive coords
#		Check coords status
#		Send response to server

#	Update screen

WIN STATEMENT
-----------------------------------------------------------------------------------------------------
#	End Game
#		Show who won