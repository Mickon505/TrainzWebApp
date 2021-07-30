let columns = document.getElementsByClassName("col");
let rrSwitch = document.getElementById("chckbx");
let forwardButton = document.getElementById("forward");
let stopButton = document.getElementById("idle");
let backwardsButton = document.getElementById("backwards");
let engine = false;


function resolution_changed(){
    //console.log("yes, screen changed");
    //console.log(columns)
    if (window.innerWidth > 992){
        for(var i = 0; i < columns.length; i++){
            columns[i].classList.remove("offset-4");
            columns[i].classList.add("offset-5");
        }
    }
    else if (window.innerWidth < 376){
        for(var i = 0; i < columns.length; i++){
            columns[i].classList.remove("offset-4");
            columns[i].classList.add("offset-3");
        }
    }
    else if (window.innerWidth > 376){
        for(var i = 0; i < columns.length; i++){
            columns[i].classList.remove("offset-3");
            columns[i].classList.add("offset-4");
        }
    }
    else if (window.innerWidth < 992){
        for(var i = 0; i < columns.length; i++){
            columns[i].classList.remove("offset-5");
            columns[i].classList.add("offset-4");
        }
    }
}

//resolution_changed();
//window.addEventListener("resize", resolution_changed)


forwardButton.addEventListener("click", (e) => {
    if (engine){
        highlightForward();
        start();
    }
});

stopButton.addEventListener("click", (e) => {

    if (engine){
        highlightIdle();
        stop();
    }
});

backwardsButton.addEventListener("click", (e) => {
    if (engine){
        highlightBackwards();
        reverse();
    }
    
});

document.getElementById("switch").addEventListener("click", (e) => {
    if (engine){
        console.log(rrSwitch.checked)
        railRoadSwitch();
    }
    else {
        rrSwitch.checked = false;
    }
});

function highlightForward(){
    stopButton.classList.remove("controller-pressed");
    backwardsButton.classList.remove("controller-pressed");
    forwardButton.classList.add("controller-pressed");
}

function highlightIdle(){
    stopButton.classList.add("controller-pressed");
    backwardsButton.classList.remove("controller-pressed");
    forwardButton.classList.remove("controller-pressed");
}

function highlightBackwards(){
    stopButton.classList.remove("controller-pressed");
    backwardsButton.classList.add("controller-pressed");
    forwardButton.classList.remove("controller-pressed");
}

function resetTrack(){
    highlightIdle();
    stop();
    rrSwitch.checked = false;
    railRoadSwitch();
}

window.onload = resetTrack

document.getElementById("engine").addEventListener("click", (e) => {
    startEngine();
});


// SERVER COMMUNICATION
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
        console.log("command sent");
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
        console.log("command sent");
        }
    })
}

function railRoadSwitch(){
    let en_di = rrSwitch.checked; // Enabled or Disabled (true / false)

    $.ajax({
        type:'POST',
        url:'/rr',
        data:{ 
        signal: en_di
        },
        success:function()
        {
        console.log("command sent");
        }
    })
}

function startEngine(){
    engine = document.getElementById("engine").checked;
    

    $.ajax({
        type:'POST',
        url:'/startengine',
        data:{ 
        signal: engine
        },
        success:function()
        {
            if(engine == false){
                location.href = "/thanks_for_playing";
            }
            else {
                engine = true;
                timer();
            }
        }
    })
}

document.onkeydown = (e) => {
    console.log(engine);
    if (engine){
        switch(e.key){
            case " ":
                console.log("Train Status: Idle");
                highlightIdle();
                stop();
            break;
    
            case "w":
                console.log("Train Status: Going Forward");
                highlightForward();
                start();
            break;
    
            case "s":
                console.log("Train Status: Going Backwards");
                highlightBackwards();
                reverse();
            break;
    
            case "r":
                console.log("Rail Road Switch Status: switched");
                rrSwitch.checked = !rrSwitch.checked;
                railRoadSwitch();
    
            case "e":
                console.log("Train Status: Idle");
                highlightIdle();
                stop();
            break;
    
            default:
                console.log(e.key);
            break;
        }
    }
}

function timer(){
    let seconds = 30;
    let timerInterval = setInterval(() => {
        console.log(seconds);
        seconds--;
        if(seconds < 1){
            resetTrack();
            document.getElementById("engine").addEventListener("click", (e) => {
                engine = false;
                document.getElementById("engine").checked = false;
            });

            $.ajax({
                type:'POST',
                url:'/startengine',
                data:{ 
                signal: false
                },
                success:function()
                {
                location.href = "/thanks_for_playing";
                }
            })

            clearInterval(timerInterval);
        }
    }, 1000);
}