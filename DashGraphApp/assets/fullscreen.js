
window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        request_full_screen: function(_) {
            let graph_div;
            const triggered_id = dash_clientside.callback_context.triggered_id;
            if ("fullscreen-graph" == triggered_id) {
                graph_div = document.getElementById("view-graph")
            } else if ("fullscreen-short-tree" == triggered_id) {
                graph_div = document.getElementById("view-short-tree")
            } else if ("fullscreen-flat-tree" == triggered_id) {
                graph_div = document.getElementById("view-flat-tree")
            }
            if (!document.fullscreenElement) {
                if (graph_div.requestFullscreen) {
                    graph_div.requestFullscreen();
                } else if (graph_div.mozRequestFullScreen) { // Firefox
                    graph_div.mozRequestFullScreen();
                } else if (graph_div.webkitRequestFullscreen) { // Chrome, Safari and Opera
                    graph_div.webkitRequestFullscreen();
                } else if (graph_div.msRequestFullscreen) { // IE/Edge
                    graph_div.msRequestFullscreen();
                }
            }
        }
    }
});