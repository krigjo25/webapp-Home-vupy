 <?php
/*****************************************************
* Tittel : Email - form (send from form)
* Hensikt :  User can submit a feedback, which can be retrived with-in the inbox in e-mail
* Laget : 15/04-17 
* Merk: // 
*******************************************************/
// To, from, subject

$email_to = 'krigjo25@gmail.com';
$email_subject = $_POST['email_subject'];
//feedback & wordwrap in-case the user insert more than 70 words in one line.
$email_feedback = $_POST['email_feedback'];
$email_feedback = wordwrap($feedback, 70, "\r\n");

// Headers
$email_header = 'K-design / Utviklings feedback' . "\r\n";
// Hashtag
$hashtag = $_POST['hashtag'];
// Mail () function 

 mail($email_to, $email_subject, $email_header, $email_feedback $hashtag);
 

?>
<div class="feedback">
<h1>Feedback</h1>
<p>Greetings,</p>
<p>Please take your time to write us a feedback, i would appriciate it.<br>
Sincerely, <br>
K. Gjøsund</p>
<form action="" method="POST">
<fieldset>
  <legend> Write us a feedback</legend>
    <label> What is your name</label><br>
      <input type="text" name="name" placeholder="Jhon Doe"><br>
    <label>Write us a comment</label>
        <br>
      <textarea name="feedback" rows="10" cols="50" max= "3" placeholder=" Write a feedback...">
      </textarea><br>
      <label>Add some hashtags(Optional)</label><br>
      <input type="text" name="hashtag" placeholder="#Awesome #amazing">
        <br>
      <input type="checkbox" name="agree"><label>by checking this box, you agree to our "<a href="feedback_agreement.com">Feedback agreement"</a></label>
        <br>
      <input type="send" name="submit" value="send feedback">  
      <input type="reset" name="reset" value="reset the form">
</fieldset>

</form>
