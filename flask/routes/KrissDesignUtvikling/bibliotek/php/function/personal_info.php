<?php
/*****************************************************
* Tittel : Funksjoner fra boken Webprogrammering 
* Hensikt :  A place to store function from codes from the book
* Laget : 24.04-17
* Last time Edited : 
* Merk:  // Skiller kode snutter
*******************************************************/
?>
<?php // Kodesnutt 5.7
function PersonalInfo( $Name, $age, $Comments) { // Function head
	echo "<h1> Checking your age</h1>";
	$Skjema = "Greetings,<strong> %s </strong> your current age is <strong>%s</strong> <br> With-in 10 years, <strong>%s</strong> will be <strong>%d</strong> years old <br><strong>%s</strong>'s comment : <strong>%s</strong>"; // Legge strengen inni i matrise, gir bedre flytt for Printf
	$Name = $_POST['Name'];
	$CurrentAge = $_POST['Age'];
	$NewAge = $_POST['Age'] +10;
	$Comment = $_POST['Comments'];
	printf($Skjema, $Name, $CurrentAge, $Name, $NewAge, $Name, $Comment ); // Legge $_POST['attribute'] eller $variabel etter rekke følge, der %s, %d osv kommer.
} // Slutt på Funksjon
?>