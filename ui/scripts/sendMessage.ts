export function sendData(url = '', data = {}, sendMethod?: "POST") {
    return fetch(url, {
        method: sendMethod, 
        mode: 'cors', 
        cache: 'no-cache',
        credentials: 'same-origin', 
        headers: {
            'Content-Type': 'application/json',
        },
        redirect: 'follow', 
        referrer: 'no-referrer', 
        body: JSON.stringify(data), 
    })
        .then(response => response.json()); 
}