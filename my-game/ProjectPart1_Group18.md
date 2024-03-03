![Cover Page-1](https://github.com/BUIE201-Fall2023/project-group-18/assets/126497934/5e5abb6c-07a9-4a37-8266-fd4d2f6a80ba)

![image](https://github.com/BUIE201-Fall2023/project-group-18/assets/126497934/1f72e2dc-2ad3-4f41-a33f-cba0944f7e93)


# Table of Contents


1. A Brief Description of the Game

2. Class Diagram

3. Brief Explanation of Class Diagram

4. Use-Case Diagram

5. Brief Explanation Of Use-Case Diagram

# 1. A Brief Description of the Game

Harry Potter - Hogwarts Under Attack:
Our game is a Harry Potter themed 2D platform game. In this game our main objective is to kill as many dementors as possible, to face the Voldemort, save Hogwarts and win the game. Within the game there will be three vertical platforms where our playable character Harry can switch up and down between platforms to slay dementors on each platform. Harry uses his wand to (key.X) throw magic towards enemies. Two hits of magic kill a dementor. But while attacking dementors, Harry must be cautious about dementor attacks. Jumping over them or switching between platforms to avoid might be considerable choices to prevent damage. Every damage decreases the life bar by 25 and once the initial life bar is down to 0, Harry fails to protect Hogwarts and the game is over. Dementors will be spawned on platforms randomly. After 20 dementors are slayed, (count will be kept on screen) our final boss The Lord Voldemort will appear. Killing Voldemort won’t be as easy as killing dementors. However, the potions are there to help! Throughout the gameplay there will be random potions spawned on the map somewhere on the platforms, you can obtain the potions to increase your life bar by 50. Kill dementors to face Voldemort while dodging the attacks, obtain potions to increase your chances and slay Voldemort to finish the game and save Hogwarts, once and for all.

# 2. Class Diagram

# 3. Brief Explanation of Class Diagram
Our Class Diagram has a total of 9 classes: Game Wand, LifeBar, Entity, Enemy, Potion, Dementor, Voldemort, Harry Potter.
Game Class:
Game class is the most important class of our diagram. This is where the game will be run with play() function. Game has “has a” relationship with Potion, Enemy and Harry Potter classes. These are components of the game; our game involves these elements. However, Harry Potter, Enemy and Potion can exist without the game’s play itself. They are separate entities. Therefore, they are aggregated to our game class. There will be one Harry Potter in the game and 0 potions initially. There will be 0 enemies eventually and the numbers on these aggregation lines indicate that. Game is associated with LifeBar class because LifeBar is updated with the changes that are happening in the Game class. Needs information from there. And wand is also associated with the game class since the damage will be controlled there.
LifeBar Class:
For Harry’s life we are defining a Lifebar class. Harry Potter has a life bar therefore it is aggregated to Harry Potter class and associated with game as we discussed above. It’ll be shown on screen, so it has width and height attributes.
Potion Class:
For obtainable life potions we are defining a potion class. It is associated with Harry Potter since the picked potions increase Harry’s life bar, needs information from Harry to update the life bar. And aggregated with game class as discussed above.
Wand Class:
For the magic Harry Potter throws to deal magic we are defining a wand class. It is associated with the game on both sides since its position on the map will be updated and the damage will be dealt with accordingly, they both need information from each other.
Enemy Class:
For the enemies Harry is going to face we are creating an enemy class, with two subclasses that are composed of enemy class, which are different enemy types: Dementor Class and Voldemort Class. Enemy is associated with wand since its death is dependent on the wand and the magic it throws on the map. Harry Potter is also associated with enemy class because he might get damage from the collision.
Harry Potter Class:
For our playable character we are creating a Harry Potter class. Harry is associated with wand and aggregated to game as explained above. Associated with potion class since his vitality is dependent on it. In Harry’s class there are attributes like its image, position life etc.
Entity Class
To make coding easier for our dynamic entities, we are defining an entity class which will check their positions collision and aliveness for our moving elements: Harry Potter, Enemies and Wand (its magic on map).

# 4. Use-Case Diagram
![Use Case Diagram](https://github.com/BUIE201-Fall2023/project-group-18/assets/126497934/084ab4a1-2769-4bdf-be66-dc9aa3985f38)

# 5.Brief Explanation Of Use-Case Diagram

Start Game Use Case:
To start the game users can engage with the key.S
Exit Game Use Case:
To exit the game users can engage with the key.ESC
Jump Use Case:
To jump users can engage with the key.SPACE
Shoot Magic Use Case:
To shoot magic users can engage with the key.X
Move Left Use Case:
To move left users can engage with the key.LEFT
Move Right Use Case:
To move right users can engage with the key.RIGHT
Platform Up Use Case:
To move to the upper platform users can engage with the key.UP
Platform Down Use Case:
To move to the lower platform users can engage with the key.DOWN



