//let currSpeed

function start(){
    console.log("Train started");
    $.ajax({
        type:'POST',
        url:'/start',
        data:{
        signal: "go"
        },
        success:function()
        {
        console.log("success");
        }
    })
}

function stop(){
    console.log("Train stopped");
    $.ajax({
        type:'POST',
        url:'/stop',
        data:{
        signal: "stop"
        },
        success:function()
        {
        console.log("success");
        }
    })
}

function reverse(){
    console.log("Train reversed");
    $.ajax({
        type:'POST',
        url:'/rev',
        data:{
        signal: "reverse"
        },
        success:function()
        {
        console.log("success");
        }
    })
}
