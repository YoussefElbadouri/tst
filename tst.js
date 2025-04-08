// 🔥 Exécution dynamique de code JS
const userInput = prompt("Enter code:");
eval(userInput);

// 🔥 Injection DOM
const name = "<img src=x onerror=alert('xss')>";
document.body.innerHTML = "Hello " + name;
