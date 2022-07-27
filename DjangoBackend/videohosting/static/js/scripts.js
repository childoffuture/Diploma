$(function()
{
  var webSocket = null;
  var userName = document.getElementById("chat_page").getAttribute("user_name");

  function connect()
  {
    disconnect();

    var roomCode = document.getElementById("chat_page").getAttribute("room_code");
    var connectionString = 'ws://' + window.location.host + '/ws/chat/' + roomCode + '/';
    webSocket = new WebSocket(connectionString);
    webSocket.onopen = function()
    {
      update_ui();
    };

    webSocket.onmessage = function(e)
    {
        console.log(e.data)
        let data = JSON.parse(e.data);
        data = data["payload"];
        let event = data["event"];
        if (event == "MESSAGE")
        {
          let message = data['text'];
          var chat_log = $('#chat_log');
          chat_log.html(chat_log.html() + message + '<br/>');
          chat_log.scrollTop(chat_log.scrollTop() + 1000);
        }
    };

    webSocket.onclose = function()
    {
      webSocket = null;
      update_ui();
    };
  }

  function disconnect()
  {
    if (webSocket != null)
    {
      webSocket.close();
      webSocket = null;
      update_ui();
    }
  }

  function update_ui()
  {
    if (webSocket == null) {
      $('#connect_status').text('Не подключено');
      $('#connect_button').html('Подключиться');
    } else {
      $('#connect_status').text('Подключено');
      $('#connect_button').html('Отключиться');
    }
  }

  $('#connect_button').click(function()
  {
    if (webSocket == null) {
      connect();
    } else {
      disconnect();
    }
    update_ui();
    return false;
  });

  $('#send_button').click(function()
  {
    if (webSocket != null)
    {
        var date = new Date().toLocaleTimeString();
        var text = $('#text').val();
        let data = {
            "event" : "MESSAGE",
            "text" :  userName + ' (' + date + '): ' + text
        }
        console.log(JSON.stringify(data))
        webSocket.send(JSON.stringify(data));
        $('#text').val('').focus();
    }
    return false;
  });

  $('#text').keyup(function(e)
  {
    if (e.keyCode === 13)
    {
      $('#send_button').click();
      return false;
    }
  });
});