function sendEmail() {
  let recipient = 'your@gmail.com'
  let name = document.querySelector('#msgName').value ?? ''
  let email = document.querySelector('#msgEmail').value ?? ''
  let msg = document.querySelector('#msgText').value ?? ''
  let url = 'mailto:?subject=Welcome&to=' + recipient + '&body=' + msg + '<br/>Regards<br/> Name: ' + name + '<br/>Email: ' + email
  url = url.replace(/<br\s*\/?>/gm, '%0D%0A')  
  // Redirect to email client
  location.href = url
}

/*
<form>
  <input type="text" name="name" id="msgName" />
  <input type="text" name="email" id="msgEmail" />
  <input type="text" name="text" id="msgText" />
  
  <div class="sendEmail" onclick="sendEmail()">Send Email</div>
</form>
*/
