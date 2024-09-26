const socket = new WebSocket('ws://127.0.0.1:8000/ws/send_rack/');

socket.onopen = function(e) {
  console.log("[open] Connection established");
  socket.send(JSON.stringify({message: "Hello Server!"}));
};

socket.onmessage = function(event) {
  console.log(`[message] Data received from server: ${event.data}`);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    console.log('[close] Connection died');
  }
};

socket.onerror = function(error) {
  console.log(`[error] ${error.message}`);
};
