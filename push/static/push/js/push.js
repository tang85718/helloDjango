/**
 * Created by dauglas on 16/7/14.
 */

$(document).ready(function () {
    // When we're using HTTPS, use WSS too.
    var scheme = window.location.protocol == 'https:' ? 'wss' : 'ws';
    var socket = new ReconnectingWebSocket(scheme + '://' + window.location.host + '/chat/');

    socket.onmessage = function (e) {
        var h3_sel = $("h3#2013");
        var span = $("<span></span>").text(e.data);
        var p = $("<p></p>");
        var month_span = $("<span></span>").text("6月");
        var li = $("<li></li>");
        p.append(span);
        li.append(month_span);
        li.append(p);
        h3_sel.after(li);
    }
    socket.onopen = function () {
        socket.send("hello push....");
    }
});