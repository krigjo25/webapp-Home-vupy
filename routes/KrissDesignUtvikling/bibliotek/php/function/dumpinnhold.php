
<?php
/*	 Tittel  : 										       *
 *				Dump Innhold 							   *
 *														   *
 *														   *
 *														   *
 *	 Laget   : 										       *
 *				19.05-17	 							   *
 *														   *
 *														   *
 *														   *
 *	Hensikt  : 											   *
 *				Hensikten med DumpInnhold er å skrive ut   *
 *				innholdet av en matrise eller en variabel. *
 *				Fungerer med vanlige matriser og Super	   *
 *				globale matriser						   *
 *														   *
 * 	    MERK : 											   *
 * 				Bruker HTML-elemeentet <pre> for å få en   * 
 *				oversiktlig utskrift av innholdet. Passer  *
 *			   	derfor godt til debugging.				   *
*/
function DumpInnhold($var){ // funksjon navn (alt mulig kan tas med her)
echo "<pre>";
print_r($var); // Finner innholdet i matrisen
echo "</pre>";
}
?>