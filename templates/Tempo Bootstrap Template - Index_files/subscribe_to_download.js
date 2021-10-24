
function showSubscribe(){
    var subscribeContainer = document.createElement("div");
    subscribeContainer.setAttribute('style', 'position: fixed; right:0; bottom:0px; z-index:10000;');
    var subscribeImg = document.createElement("img");
    subscribeImg.setAttribute('src', 'http://static.nowait.xin/studio/images/subscribe_wx.png');
    subscribeImg.setAttribute('style', 'width: 300px; opacity: 0.9;');
    subscribeContainer.appendChild(subscribeImg);
    document.body.appendChild(subscribeContainer);
    return subscribeContainer;
}


setTimeout(function(){
    if(window.jQuery){
        var node = showSubscribe();
        $(node).hide().fadeIn(1000);
    }else{
        showSubscribe();
    }
}, 5000);