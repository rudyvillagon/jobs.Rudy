function toggleCurrentPassword() {
    const input = document.getElementById("Current_password");
    input.type = input.type === "password" ? "text" : "password";
}

function toggleNewPassword() {
    const input = document.getElementById("New_password");
    input.type = input.type === "password" ? "text" : "password";
}

function toggleConfNewPassword() {
    const input = document.getElementById("Conf_new_password");
    input.type = input.type === "password" ? "text" : "password";
}

document.addEventListener("DOMContentLoaded", () => {
const token = localStorage.getItem("token");
const id = localStorage.getItem("userId");

if (!token || !id) {
    window.location.href = "Login.html";
    return;
}

document.getElementById("Cancel_c")?.addEventListener("click", () => {
    window.location.href = "Profile.html";
});

document.getElementById("C_change")?.addEventListener("click", async () => {

    const currentPassword = document.getElementById("Current_password").value;
    const newPassword = document.getElementById("New_password").value;
    const confNewPassword = document.getElementById("Conf_new_password").value;

    if (newPassword !== confNewPassword) {
        alert("The passwords dont match!")
        return;
    }

    try{

        const response = await axios.patch(`https://api.restful-api.dev/objects/${id}`, 
        { data: {currentPassword, password: newPassword } },
            { headers: { Authorization: `Bearer ${token}` } }
        );

        alert("Password changed Correctly!");

        document.getElementById("Current_password").value = "";
        document.getElementById("New_password").value = "";
        document.getElementById("Conf_new_password").value = "";

        return response.data;

    } catch (error){
        console.error (error.message);
        alert("Failed to change the password. Try again.");
    } 

    });
});