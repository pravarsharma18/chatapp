let socketUrl = "ws://127.0.0.1:8000/ws/sc/";
let ws = new WebSocket(
  "ws://" + window.location.host + "/ws/sc/" + groupName + "/"
);
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
  msgLogs.append(parsedData.user + " : " + parsedData.msg + "\n");
};
ws.onerror = function (e) {
  console.log("Error occured", e);
};
ws.onclose = function (e) {
  console.log("Connection close", e);
};

submit.addEventListener("click", function (e) {
  console.log(JSON.stringify(msg.value));
  ws.send(
    JSON.stringify({
      msg: msg.value,
      user: userName,
    })
  );
  msg.value = "";
});
