(function () {
    var coreSocialistValues = ["Oops!", "Here!", "No,"]
        , index = Math.floor(Math.random() * coreSocialistValues.length);
    document.body.addEventListener('click', function (e) {
        if (e.target.tagName == 'A') {
            return;
        }
        var x = e.pageX
            , y = e.pageY
            , span = document.createElement('span');
        span.textContent = coreSocialistValues[index];
        index = (index + 1) % coreSocialistValues.length;//取模循环
        span.style.cssText = ['font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif; z-index: 10; position: absolute; font-weight: bold; color: rgba(29, 29, 29, 0.8); top: ', y - 20, 'px; left: ', x, 'px;'].join('');
        document.body.appendChild(span);
        animate(span);
    });
    function animate(el) {//动画
        var i = 0
            , top = parseInt(el.style.top)
            , id = setInterval(frame, 24);
        function frame() {//帧
            if (i > 180) {
                clearInterval(id);
                el.parentNode.removeChild(el);
            } else {
                i += 2;
                el.style.top = top - i + 'px';
                el.style.opacity = (180 - i) / 180;
            }
        }
    }
}());

let a_list = document.querySelectorAll('a');
    var i = 0;
    for (len = a_list.length; i < len; i++) {
        a_list[i].onmouseover = function () {
            this.style.textDecoration = 'underline';
        }
        a_list[i].onmouseout = function () {
            this.style.textDecoration = 'none';
        }
    }