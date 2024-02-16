
async function verifyUser(event) {
    event.preventDefault();
    email = document.querySelector("#email").value;
    password = document.querySelector("#password").value;
    url = `http://localhost:8000/users/verify`
    const payload = {
      email: email,
      password: password
    };
    console.log(`Payload: ${payload.JSON}`)
    console.log(`url: ${url}`)
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })
      .then(response => {
        if (response.ok) {
          console.log('Request successful!');
          window.location.href = "profile_new.html";
        } else {
          console.error(`Request failed with status code: ${response.status}`);
          return response.text();
        }
      })
      .then(data => {
        if (data) {
          console.error(data); // Print response content for debugging if needed
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });  
  }
  
  // Add event listener to the form
  document.getElementById("loginForm").addEventListener("submit", verifyUser);
  
  


