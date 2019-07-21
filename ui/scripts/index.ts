import { Navbar } from "./navbar";
import { List } from "./list";
import { Button, Input } from "./button";
import { sendData, getData } from "./sendMessage";

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
        let actionItems = m.prop([]);
        getData(
            'http://localhost:5000/all',
            "GET")
            .then(data => {
                let items = data ? data.map(x => {
                    return {
                        description: x.content,
                        open: m.prop(false),
                        title: `${x.name} (${x.subject})`,
                        id: x.id
                    }
                }) : [];
                actionItems(items)
                m.redraw();
            })
            .catch(error => console.error(error));
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
                                .then(data => {
                                    getData(
                                        'http://localhost:5000/all',
                                        "GET")
                                        .then(data => {
                                            let items = data ? data.map(x => {
                                                return {
                                                    description: x.content,
                                                    open: m.prop(false),
                                                    title: `${x.name} (${x.subject})`,
                                                    id: x.id
                                                }
                                            }) : [];
                                            controller.actionItems(items)
                                            m.redraw();
                                        })
                                }
                                )
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
