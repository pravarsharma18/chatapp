let socketUrl = "ws://127.0.0.1:8000/ws/sc/";
url = "ws://" + window.location.host + "/ws/ac/" + groupName + "/";
console.log("url: ", url);
let ws = new WebSocket(url);
let submit = document.getElementById("chat_submit");
let msg = document.getElementById("chat_input");
let msgLogs = document.getElementById("chat_logs");

console.log("userName", userName);

ws.onopen = function (e) {
  console.log("Websocket open", e);
};
ws.onmessage = function (e) {
  console.log("recieved from server", e);
  console.log(JSON.parse(e.data));
  parsedData = JSON.parse(e.data);
  let p = document.createElement("div");
  p.classList.add("border");
  p.append(
    `${parsedData.user == userName ? "You" : parsedData.user} : ${
      parsedData.msg
    }`
  );

  msgLogs.prepend(p);
};
ws.onerror = function (e) {
  console.log("Error occured", e);
};
ws.onclose = function (e) {
  console.log("Connection close", e);
};

submit.addEventListener("click", function (e) {
  if (!msg.value) {
    return;
  }
  console.log(JSON.stringify(msg.value));
  ws.send(
    JSON.stringify({
      msg: msg.value,
      user: userName,
    })
  );
  msg.value = "";
});

window.onload = (event) => {
  console.log("focus");
  msg.focus();
};
