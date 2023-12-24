const btn = document.getElementById('summarize-btn');
btn.addEventListener('click', () => {
    btn.disabled = true;
    btn.innerHTML = 'Summarizing...';
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var url = tabs[0].url;
        // var hxr = new XMLHttpRequest();
        // hxr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true);
        // hxr.onload = function () {
        //     var text = hxr.responseText;
        //     var summary = document.getElementById('summary');
        //     summary.innerHTML = text;
        //     btn.disabled = false;
        //     btn.innerHTML = 'Summarize';
        // }
        // hxr.send();
        var data = fetch("http://127.0.0.1:5000/summary?url=" + url)
            .then(response => response.text())
            .then(text => {
                console.log(text);
                var summary = document.getElementById('summary');
                summary.innerHTML = text;
                btn.disabled = false;
                btn.innerHTML = 'Summarize';
            });

    });
});

