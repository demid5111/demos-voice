import { m } from ".";

export const Button = (title: string, callback?: (e) => void) => 
    m(
        "button.uk-button.uk-button-default",
        {            
            onclick: callback
        },
        title
    )

export const Input = (callback?: (value: string)=> void) => 
    m(
        "input.uk-input.uk-margin-right",
        {
            type: "text",
            oninput: (v) => callback(v.srcElement.value)
        },
    )
