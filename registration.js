
async function createUser(event) {
    event.preventDefault();
    username = document.querySelector("#username").value;
    email = document.querySelector("#email").value;
    password = document.querySelector("#password").value;
    url = `http://localhost:8000/users/create`
    const payload = {
      username: username,
      email: email,
      password: password
    };
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
  document.getElementById("registrationForm").addEventListener("submit", createUser);
