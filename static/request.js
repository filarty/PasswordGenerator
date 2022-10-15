let sendPost = () => {
    let xhr = new XMLHttpRequest();
    url = "/";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    let elem = document.getElementById("counter");
    let resultNumber = document.getElementById("result");
    xhr.send(JSON.stringify({"count": elem.value}));
    xhr.onreadystatechange = () => {
        if (xhr.readyState == 4 && xhr.status == 200){
            resultNumber.value = JSON.parse(xhr.response).result;
        };
    };
};
