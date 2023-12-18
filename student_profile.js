document.addEventListener("DOMContentLoaded", function () {
    
    const achievementsData = [
        "Research Paper Published in IEEE",
        "President's List - GPA 4.0",
        "Best Speaker in Debate Club"
    ];

    const achievementList = document.getElementById("achievement-list");

    
    achievementsData.forEach(achievement => {
        const li = document.createElement("li");
        li.textContent = achievement;
        achievementList.appendChild(li);
    });

    document.getElementById("student-name").textContent = "Jane Doe";
    document.getElementById("college-name").textContent = "Sample College";
    document.getElementById("student-year").textContent = "Junior";
});


function loadProfilePic(event) {
    const input = event.target;
    const reader = new FileReader();

    reader.onload = function () {
        const profilePic = document.getElementById("profile-pic");
        profilePic.src = reader.result;
    };

    reader.readAsDataURL(input.files[0]);
}