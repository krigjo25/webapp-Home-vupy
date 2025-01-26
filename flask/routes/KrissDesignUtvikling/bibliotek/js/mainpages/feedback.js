// JavaScript Document
function formValidation() {
	var x = document.forms["feedback"]["textbox"].value;
	if ( x == null || x == "") {
		alert("feeback must be filled out");
		return false;
	}
}