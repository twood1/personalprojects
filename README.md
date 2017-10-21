# personalprojects

My projects here are as follows:

* GDAX Ticker bot - Ticker.py:
	* This bot does what it sounds like. It writes into a file 	the order book for every second. Given fast enough queries 	from the GDAX website, one could write an arbitrage bot 	with this. In order for the script to work for you, you 	need two things: A GDAX private key (register with GDAX 	and download the key that you request.) Here is how:
	[https://docs.gdax.com/#generating-an-api-key](Generating 	API Key). You will also need to modify the line that 	writes a .txt file to the appropriate path you wish to 	write the 	order book to.

* Neural Network - Prac.py
	* A simple (broken) neural network. I was fiddling around 	with it a while ago and broke the indexing such that I 	have errors... But, besides for that, it works just like a 	simple NN should!

* Class scheduler via genetic algorithm: Schedule.py
	* This script solves a scheduling problem that I was 	tasked with by Dr. Charles Delwiche. The task is simple: 	Develop a schedule that conforms to hard constraints and 	minimizes number of soft constraints broken.
		* The constraints are as follows (HC - hard 				constraint, SC - soft constraint):
			* HC - Each day, two groups of three present
			* HC - In each group, there is a Leader, 					Presenter,	and Scribe role.
			* HC - No person should do multiple jobs on the 			same day
			* HC - Each person must do each job exactly once 			before the first half of the semester, and each 			job exactly once in the second half of the 				semester.
			* SC - No person should have to do leader or 				presenter roles (heavy roles)on back to back 				days.
			* SC - No person should work with the same 				person twice.
	* I used a genetic algorithm to solve this: Some HC's were 	hard coded, i.e. groups of 3, and other HC's caused 	immediate fatality of the produced schedule (Multiple jobs 	same day)
	* SC's broken produce a positive value added to the score. 	An increase in score corresponds to a loss of fitness, 	i.e. a worse schedule.
	* The genetic algorithm is as follows:
		* Generate random schedule X
		* Score schedule
		* parentArray <- [X]
			* Repeat
				* offspringArray <- []
				* Sort population array by score (I should 				have used min heap instead actually)
				* Take lowest scoring matrix and randomly 					permute specific positions and add to 					offspring array (Elitism).
				* Select n schedules to reproduce from parent array, 						weighted probability by their score. The 					lower the score, the higher probability 					they have to be selected to reproduce.
				* Mutate the selected n schedules 						preserving the HC's, scoring each one, and 				remembering Best solution found globally. Store in offspring array.
				* Replace parent array with offspring 					array