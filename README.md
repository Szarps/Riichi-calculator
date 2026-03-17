## What is "Riichi Mahjong"?

Riichi Mahjong is a japanese variant of Mahjong. This is a game that is played often with 4 players total (or 3 with slight changes in rules) where the main objective is to achieve the biggest amounts of points possible by the end of the game, as established based off the initial rules accepted by the players (which among them include but not limited to; preemptive game finish if someone goes into negative points and how many rounds are given.)

This is a tile-based game, each player gets to hold 13 tiles at a time and drawing from "the wall" one tile and if their hand isn't considered "complete" they would have to choose a tile to discard, the next player to the right (counter-clockwise) will repeat the process, so on and so forth until someone declares a win.
There is more nuance to the game than this but this is the basic idea.

## Aim of the project

This is made solely for learning purposes for myself as I learn how to code and program. In it's finished state the "app" should be able to correctly determine the value of a hand, if a hand is valid and ideally have some API to integrate it alongside with other kinds of software, thus scaling it's capacity.

## Challenges of this project

Because every good game that stood the test of time isn't quite straightforward with it's point system Mahjong is no exception. This goes beyond a simple "create a database of possible combinations and return a fixed result", due to the nature of the game there are a lot of factors to take into account, such as:

- Is the hand open or closed?
- Is the winning hand declared by calling a tile someone discarded or by drawing from the wall?
- How many "yakus (a kind of winning hand that follows specific criteria)" does the hand applies? and correct for redundancy (as some of these make others null since they are a kind of "upgraded version" so it can not count both at the same time)
- As per the rules, in case of ambiguity (read a hand can be read in two different ways or more) the case where it yields the most amounts of point will be chosen

Hopefully this gives enough perspective about the scope and how this can be a more complicated process.

## Things this project taught me so far: (permanent WIP as i work on it)

- Unit testing
- Project structuring and planning
- Bases of orchestration and modularity
