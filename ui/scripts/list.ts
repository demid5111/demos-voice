import { ListItem, m } from ".";
import { Button } from "./button";
import { sendData } from "./sendMessage";

export const List = (data: ListItem[]) => {
    return m(
        "ul.uk-list.uk-list-divider.uk-accordion",
        data.map((x) => {
            return ListItem(x.title, x.id, x.open(), x.description, x.open)
        }
        )
    )
}

var ListItem = (title, id, changeOpen, description, callback) => {
    return m(
        "li",
        {
            class: changeOpen ? "uk-open" : "",
            onclick: () => {
                callback(!callback());
            }
        },
        m("a.uk-accordion-title", title),
        m(
            ".",
            {
                class: changeOpen ? "" : "hide"
            },
            m(".uk-margin", description),
            Button("Провести анализ", (e) => {
                e.preventDefault();
                e.stopPropagation();
                sendData("http://localhost:5000/analyze", { proposalId: id }, "POST")
                    .then(
                        () => {}
                    )
                    .catch(e => console.error(e));
            })
        )
    )
}
