
<?php
/*	 Tittel  : 										       *
 *				SessionTeller							   *
 *														   *
 *														   *
 *														   *
 *	 Laget   : 										       *
 *				20.05-17	 							   *
 *														   *
 *														   *
 *														   *
 *	Hensikt  : 											   *
 *				Hensikten med SessionTeller er å skrive    *
 *				ut hvor mange ganger man har oppdatert	   *
 *				Siden 									   *
 *														   *
 *														   *
 * 	    MERK : 											   *
 *														   *
 *														   *
 *														   *
*/
function SessionTeller($var){ // funksjon navn (alt mulig kan tas med her)
session_start(); // Starter en Økt
if ( isset($_SESSION['teller']) ) {
	$_SESSION['teller']++;
}
else {
	$_SESSION['teller'] = 1;

}
$Teller = "<p>";
$Teller .= "Du har oppdatert siden ";
$Teller .= "<strong>";
$Teller .= $_SESSION['teller'];
$Teller .= "</strong></p>";
echo $Teller;
}
?>