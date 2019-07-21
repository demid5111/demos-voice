import { ListItem, m } from ".";
import { Button } from "./button";

export const List = (data: ListItem[]) => {
    return m(
        "ul.uk-list.uk-list-divider.uk-accordion",
        data.map((x) => {
            return ListItem(x.title, x.open(), x.description,x.open)
        }
        )
    )
}

var ListItem = (title, changeOpen, description ,callback) => {
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
            ".uk-accordion-content",
            {
                class: changeOpen ? "" : "hide"
            },
            m(".uk-margin", description),
            Button("Провести анализ")
        )
    )
}
