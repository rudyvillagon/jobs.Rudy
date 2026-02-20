function toggleLoginPassword() {
    const input = document.getElementById("Password");
    input.type = input.type === "password" ? "text" : "password";
}

const loginUser = async(name, password) => {

    try{
        const response = await axios.get(`https://api.restful-api.dev/objects?name=${encodeURIComponent(name)}`);

        if (response.data.length === 0) {
            alert("Theres no user with that name.");
            return null;
        }

        const foundUser = response.data[0];

        if (foundUser.data?.password !== password) {
            alert ("Password Incorrect");
            return null;
        }
        
        const token = `token-${foundUser.id}-${Date.now()}`;
        localStorage.setItem("token", token);
        localStorage.setItem("userId", foundUser.id);

        return foundUser.id;

    } catch (error){
        console.error (error.message);
        return null;
    }
}

document.getElementById("Login_botton").addEventListener("click", () => {
loginUser(
    document.getElementById("User_name").value,
    document.getElementById("Password").value,
).then(result => {
    if (result) { 
        window.location.href = "Profile.html";
    }
});
});
document.getElementById("Register")?.addEventListener("click", () => {
    window.location.href = "Registration.html";
});