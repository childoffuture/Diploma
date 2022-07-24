$(function()
{
  var conn = null;

  function log(msg)
  {
    var control = $('#log');
    control.html(control.html() + msg + '<br/>');
    control.scrollTop(control.scrollTop() + 1000);
  }

  function connect()
  {
    disconnect();
    var wsUri = (window.location.protocol=='https:'&&'wss://'||'ws://')+window.location.host;
    conn = new WebSocket(wsUri);
    conn.onopen = function()
    {
      update_ui();
    };

    conn.onmessage = function(e)
    {
      if (e.data == "test checked")
      {
        $('#check_status').text('подключено (проверка пройдена)');
      }
      else
      {
        log('Новая новость: ' + e.data);
      }
    };

    conn.onclose = function()
    {
      conn = null;
      update_ui();
    };
  }

  function disconnect()
  {
    if (conn != null) {
      conn.close();
      conn = null;
      update_ui();
    }
  }

  function update_ui()
  {
    if (conn == null) {
      $('#status').text('не подключено');
      $('#connect').html('Подключиться');
    } else {
      $('#status').text('подключено');
      $('#connect').html('Отключиться');
    }
  }

  $('#connect').click(function()
  {
    if (conn == null) {
      connect();
    } else {
      disconnect();
    }
    update_ui();
    return false;
  });

  $('#check').click(function()
  {
    if (conn == null) {
      $('#check_status').text('не подключено');
    } else {
      $('#check_status').text('проверка соединения...');
      conn.send("test");
    }
    update_ui();
    return false;
  });

  $('#send').click(function()
  {
    var text = $('#text').val();
    conn.send(text);
    $('#text').val('').focus();
    return false;
  });

  $('#text').keyup(function(e)
  {
    if (e.keyCode === 13)
    {
      $('#send').click();
      return false;
    }
  });
});