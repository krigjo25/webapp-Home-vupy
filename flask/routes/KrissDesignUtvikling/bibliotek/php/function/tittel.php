<?php
/***************************************************** 
* Tittel : Title function.
* Hensikt : Interactive Title
* Laget : 13/04-17 
* Merk:   
*******************************************************/
// Creating a Title element.
function Title($Kriss, $Title) {
	// Declearing variable name
	$Kriss = "Kriss Design / Utvikling |";
echo "<title>";
echo $Kriss . " ". $Title;
echo "</title></head>";
} // End of Title
?>