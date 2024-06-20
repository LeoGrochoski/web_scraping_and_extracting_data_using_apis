function toggleDarkMode() {
    var body = document.body;
    var currentClass = body.className;
    body.className = currentClass === "dark-mode" ? "" : "dark-mode";
}

document.addEventListener("DOMContentLoaded", function() {
    var toggleSwitch = document.createElement('button');
    toggleSwitch.innerText = 'Botão Dark Mode';
    toggleSwitch.style.position = 'fixed';
    toggleSwitch.style.top = '1rem';
    toggleSwitch.style.right = '1rem';
    toggleSwitch.style.zIndex = '1000';
    toggleSwitch.onclick = toggleDarkMode;
    document.body.appendChild(toggleSwitch);
});
