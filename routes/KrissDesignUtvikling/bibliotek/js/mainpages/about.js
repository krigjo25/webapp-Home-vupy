// Declearation of variables
var i, tabContent, tabUrl;
function openTab(evt, tabName) {
    // Hide the tabcontent
    tabContent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }
        // remove the activation of the class "tablinks"
        tabUrl = document.getElementsByClassName("tabUrl");
        for (i = 0; i < tabUrl.length; i++){
            tabUrl[i].className = tabUrl[i].className.replace("active", "");
        }

        // Open the current tab, and add an "active" class to the link
        document.getElementById(tabName).style.display = "block";
        evt.currentTarget.className += "active";
}