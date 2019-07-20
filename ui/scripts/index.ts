import { Navbar } from "./navbar";
import { List } from "./list";

var m = require("mithril");
(<any>window).m = m;

var buttons = document.getElementById("button-area");

function addInitiative() {
    m.request({
        method: "POST",
        // body: {
        //     "socialNetwork": "vk",
        //     "fromUrl": ""
        // },
        url: "/85.",
        withCredentials: true,
    })
        .then(function (data) {
            console.log("ye")
        })
}

var Btn = {
    view() {
        return m("",
            Navbar(),
            m(
                "button.uk-button.uk-button-default",
                "Добавить"
            ),
            List(["Ямы", "Бордюр", "Клумба"])
        )
    }
}

m.mount(document.body, Btn);
