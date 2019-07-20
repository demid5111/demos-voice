import { Navbar } from "./navbar";
import { List } from "./list";
import { Button, Input } from "./button";
import { send } from "q";

var m = require("mithril");
(<any>window).m = m;

var buttons = document.getElementById("button-area");

let initiativePostUrl = "";

const changeUrl = (value: string) => {
    initiativePostUrl = value;
}

const sendData = () => {
    m.request({
        method: "POST",
        body: {
            "socialNetwork": "vk",
            "fromUrl": ""
        },
        url: "/example.comm",
        withCredentials: true,
    })
        .then(function (data) {
            console.log("ye")
        })
}

const Page = {
    view() {
        return m("",
            Navbar(),
            m(".uk-container",
                m(
                    ".flex-inline",
                    [
                        Input(changeUrl),
                        Button("Добавить", sendData)
                    ]
                ),
                List(["Ямы", "Бордюр", "Клумба"])
            )
        )
    }
}

m.mount(document.body, Page);
