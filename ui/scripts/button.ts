<<<<<<< HEAD
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
=======
export const Button = (title: string, callback?: () => void) => 
    m(
        "button.uk-button.uk-button-default",
        {            
            onclick: callback
        },
        title
    )
>>>>>>> add mithril

export const Input = (callback?: (value: string)=> void) => 
    m(
        "input.uk-input.uk-margin-right",
        {
            type: "text",
            oninput: (v) => callback(v.data.value)
        },
    )
