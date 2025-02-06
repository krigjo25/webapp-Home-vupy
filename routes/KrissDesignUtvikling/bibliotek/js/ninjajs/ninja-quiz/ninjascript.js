// Alert dialog box
alert("Welcome to our Super Hero Quiz !");

// Variable declaretion
var ninjaQuiz = [
["What is the real Name of the character SuperGirl", "Karen Denvers"],
["Who is the brother of Karen Denvers?", "Clark Kent"],
["What is the real Name of the character Batman?", "Bruce Wayne"],
["What is the real Name of the character Spiderman","Peter Parker"],
["What is the real Name of the character Wonderwoman","Dianna Prince"]
];
var Gcore = 0;  // Gscore, the score point of Ninja Quiz.
play(ninjaQuiz);
function play(ninjaQuiz) {
for(var i=0, question, answer, max=ninjaQuiz.length;i<max;i++){
	question = ninjaQuiz[i][0];
	answer = ask (question);
	check (answer);
}
gameOver();
}
function ask(question){
	return prompt(question);
}
function check(answer){
	if(answer === ninjaQuiz[i][1]){ // Hvis Svar er lik spørsmålet
		alert("Congratulations you had the correct answer");
		// Increase Gcore by 1 else NOT.
		Gcore++;
    }	else { 
			alert("Fail, you've written incorrect name.");

		}
}
function gameOver(){	
// After the game is over
if (Gcore >= 5){
alert("Congratulations, you've answered" +" " +Gcore + " " + " Of 5 possible Gcore");  

} else {
	(Gcore < 5)
		alert("Game over, better luck next time, you've recieved:  " + Gcore + " Gcore");
	}
}

