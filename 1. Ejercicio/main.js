const result = await fetch("https://randomfox.ca/floof/");
const data = await result.json();
const foxImage = data.image;

document.querySelector('#app').innerHTML = `<img src="${foxImage}" />`;  