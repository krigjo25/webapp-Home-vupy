
<div class="feedback">
<h1>Feedback</h1>
<p>Greetings,</p>
<p>Please take your time to write us a feedback, i would appriciate it.<br>
Sincerely, <br>
K. Gjøsund</p>
<form action="feedback.php" method="POST" enctype="">
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
      <input type="submit" name="submit" value="POST feedback">  
      <input type="reset" name="reset" value="reset the form">
</fieldset>

</form>
