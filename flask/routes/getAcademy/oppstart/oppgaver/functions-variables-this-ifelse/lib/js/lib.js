function upperCase(id, txt)
{
    //  Returning text with a uppercase in the begining of the sentence.
    return document.getElementById(id).innerHTML = /*HTML*/`${txt.replace(txt.charAt(0), txt.charAt(0).toUpperCase())}`;
}