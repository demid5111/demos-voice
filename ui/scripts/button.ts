var btn = document.getElementById("reqBtn");
var input = () => (<HTMLInputElement>document.getElementById("initPost")).value;

btn.addEventListener("click", () => send());

const reqData = {
    socialNetwork: "vk",
    fromUrl: input()
};

var send = () => {
    postData('http://localhost:5000/new', reqData)
        .then(data => console.log(JSON.stringify(data))) // JSON-строка полученная после вызова `response.json()`
        .catch(error => console.error(error));
};

function postData(url = '', data = {}) {
    // Значения по умолчанию обозначены знаком *
    return fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, cors, *same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // no-referrer, *client
        body: JSON.stringify(data), // тип данных в body должен соответвовать значению заголовка "Content-Type"
    })
        .then(response => response.json()); // парсит JSON ответ в Javascript объект
}