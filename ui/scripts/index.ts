import { Navbar } from "./navbar";
import { List } from "./list";
import { Button, Input } from "./button";
import { sendData } from "./sendMessage";

export const m = require("mithril");
(<any>window).m = m;

type CustomInputValue = () => string;

export type ListItem = {
    id: string,
    title: string,
    callback: () => void
}

const Page = {
    controller: function (customInputValue: CustomInputValue) {
        let actionItems: ListItem[] | any = [
            { id: "1", title: "Яма", description: "hello1", open: m.prop(false) },
            { id: "2", title: "Two", description: "hello2", open: m.prop(false) }
        ];
        // sendData(
        //     'http://localhost:5000/all',
        //     "GET")
        //     .then(data => { actionItems = JSON.stringify(data) })
        //         .catch(error => console.error(error));
    return {
        value: "vk",
        actionItems
    };
},
    view: function (controller: { value: CustomInputValue, actionItems }) {

        // const sendData = () => {
        // m.request({
        //     method: "GET",
        //     body: {
        //         "socialNetwork": "vk",
        //         "fromUrl": controller.value
        //     },
        //     url: "/new",
        //     withCredentials: true,
        // })
        //     .then(function (data) {
        //         console.log("ye")
        //     })
        // }

        return m("",
            Navbar(),
            m(".uk-container",
                m(
                    ".flex-inline",
                    [
                        m("input.uk-input", {
                            oninput: m.withAttr("value", (value) => controller.value = value),
                        }),
                        Button("Добавить", () => {
                            sendData(
                                'http://localhost:5000/new',
                                {
                                    socialNetwork: "vk",
                                    fromUrl: controller.value
                                },
                                "POST")
                                .then(data => console.log(JSON.stringify(data)))
                                .catch(error => console.error(error));
                        })
                    ]
                ),
                List(controller.actionItems)
            )
        );
    }
};

m.mount(document.body, Page);
