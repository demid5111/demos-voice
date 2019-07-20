var m = require("mithril");

var buttons = document.getElementById("button-area");



function addInitiative() {
    const ipж
    m.request({
        method: "POST",
        body: "",
        url: "/85.",
        withCredentials: true,
    })
        .then(function (data) {
            console.log("ye")
        })
}
m.render(buttons, m([
    m(
        "button.uk-button.uk-button-default",
        {
            onclick: addInitiative();
        },
        "Добавить"
    ),
    m("input", {
        oninput: (v) => console.log(v.data.value),
    })
])