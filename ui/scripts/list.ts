export const List = (data: string[]) => {
    m(
        "ul.uk-list.uk-list-divider",
        data.map((x)=> m("li", x))
    )
}
