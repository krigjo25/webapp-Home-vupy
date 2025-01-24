// Alert dialog box
alert("Welcome to our Super Hero Quiz !");

// Variable declaretion
var ninjaQuiz = [
["What is the real Name of the character SuperGirl", "Karen Denvers"],
["Who is the brother of Karen Denvers?", "Clark Kent"],
["What is the real Name of the character Batman?", "Bruce Wayne"],
["What is the real Name of the character Spiderman","PeterParker"],
["What is the real Name of the character Wonderwoman","Dianna Prince"]
];
var Gcore = 0;  // Gscore, the score point of Ninja Quiz.
for(var i=0, max=ninjaQuiz.length;i<max;i++){
	var answer = prompt (ninjaQuiz[i][0]); // is the question
	// If answer is a boolean value >>

	if(answer === ninjaQuiz[i][1]){ // Hvis Svar er lik spørsmålet
		alert("Congratulations you had the correct answer");
		// Increase Gcore by 1 else NOT.
		Gcore++;
    }	else { 
			alert("Fail, you've written incorrect name.");

		}
}
// After the game is over
if (Gcore >= 5){
alert("Congratulations, you've answered" +" " +Gcore + " " + " Of 5 possible Gcore");  

} else {
	(Gcore < 5)
		alert("Game over, better luck next time, you've recieved:  " + Gcore + " Gcore");
	}


