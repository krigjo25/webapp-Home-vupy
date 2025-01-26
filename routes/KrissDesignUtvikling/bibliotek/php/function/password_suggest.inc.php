<?php
/***************************************************** 
* Tittel : Interaktiv Passord
* Hensikt : Hensikten er at brukeren kan velge mellom 3- 10 
		    karakterer lang passord.
* Laget : 11/05-17 
* Merk:   
*******************************************************/
// Creating a Title element.
SuggestPass();
$Name = $_POST['Name'];
$PsLength = $_POST['list'];
function SuggestPass($Kriss, $Title) {
foreach ($PsLength as $key => $value) {
if ($Pslength == 5 ) {
	// Rand & md5
$utgangspunkt = "abcde";
echo "$utgangspunkt";
// Hashet strengen
$HashetStreng = md5($utgangspunkt);
$Length =strlen($HashetStreng);
echo "<p> Etter at md5 har behandlet utganspunktet får vi :</p><br>";
echo "<strong> $HashetStreng</strong>";
echo "<strong>$Length</strong><br>";
echo "Tegn lang streng av HEX tall <br>";
/////////////////////////////////////////
// PsLength setter start verdien til et tilfeldig sted i strengen.
$start = rand(0,($Length - $psLength - 1));
$Passord = substr($HashetStreng, $start, $psLength);
echo "Foreslående passord er :<br> <strong> $Passord</strong>"; 
} 
else {
	echo "Do'h an 404 Something went wrong !";
}
}
}
?>