
document.addEventListener("DOMContentLoaded", () => {
const token = localStorage.getItem("token");
const id = localStorage.getItem("userId");

if (!token || !id) {
    window.location.href = "Login.html";
    return;
};

document.getElementById("logOutBotton")?.addEventListener("click", () => {
    localStorage.clear();
    window.location.href = "Login.html";
});

document.getElementById("changePassword")?.addEventListener("click", () => {
    window.location.href = "C_password.html";
});


async function loadUserInformation() {
    try {
        const result = await axios.get(`https://api.restful-api.dev/objects/${id}`
        );
        const {name, data = {} } = result.data;

        document.getElementById("user_data_info").innerHTML = `
            <strong>Name:</strong> ${name}<br>
            <strong>Email:</strong> ${data.email}<br>
            <strong>Address:</strong> ${data.address}
        `;
    }catch (error){
        console.error(error);
        document.getElementById("user_data_info").textContent = 
            "Information data not load";
    }
}

loadUserInformation();

});
