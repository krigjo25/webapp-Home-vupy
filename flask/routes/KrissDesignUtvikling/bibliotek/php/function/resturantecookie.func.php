<?php
/*	 Tittel  : 										       *
 *				Input hidden 							   *
 *														   *
 *														   *
 *														   *
 *	 Laget   : 										       *
 *				19.05-17	 							   *
 *														   *
 *														   *
 *														   *
 *	Hensikt  : 											   *
 *				Hensikten med hiddenInput er å skrive ut   *
 *				innholdet av en matrise eller som er 	   *
 *				Gjemt									   *
 *														   *
 *														   *
 * 	    MERK : 											   *
 * 				Bruker HTML-elemeentet <pre> for å få en   * 
 *				oversiktlig utskrift av innholdet. Passer  *
 *			   	derfor godt til debugging.				   *
*/
function cookie($mat) { // Declearing
	foreach ($mat as $key => $value) { // Foreach   //
		if( !strstr($key, "knapp")) {
			echo "<input type='hidden'"; // legger til input element
			echo "name='$key' value='$value'> \n";  // same
		} // foreach 
	} // IF
} // Function
?>