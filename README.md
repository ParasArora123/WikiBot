# WikiBot
Implemented a bot that intelligently finds a Wikipedia link ladder between two given pages. Bot is inspired by the game https://www.thewikigame.com/ and uses the most efficient algorithm possible to get from one page to any other page. 

## __Notes on my Implementation__:
### Traversing Trees:

1. Breadth-first search (look at every path that is one length away from you), once you look at every 1 hop away, then I look at every 2 hop
2. Depth-first search (go as far down as it can before it does anything)

1. Preorder (is an example of depth-first search)
2. Inorder 
3. Postorder

Breadth first search --> use a queue (put them in the back take them out the front...first in first out)
when you go to a page you add all the links to a queue

                o  
	 1   2   3   4      5  
       o     o    o   o     o   
       /     /     \   \    |  
      6     7      8    9   10   
      o     o      o    o   o  
 
With breadth first search I would add links (the numbers) using the following steps:  
Step 1: Add 1, 2, 3, 4, 5, onto the list (list = 1, 2, 3, 4, 5)  
Step 2: Take off 1 and add 6 (list = 2, 3, 4, 5, 6)  
Step 3: Take off 2 and add 7 (list = 3, 4, 5, 6, 7)  

Conitinue this process until you find the link  
  
Queue:  
	.append()  
	.pop()  

### Pseudocode
put starter page in queue 
while queue is not empty:  
&nbsp;&nbsp;&nbsp;pop the front of queue 
&nbsp;&nbsp;&nbsp;go to that page and get links  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for each link:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if link is not the target:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;append link to queue  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return the path to this link   
        
### Output/Final Display
Path to the link:
in the queue append the list of the links to get to that link in a tuple 
e.g: 
my_queue = [(United_states, Michigan, Hawaii), (United_states, Michigan, Latin_language)]
