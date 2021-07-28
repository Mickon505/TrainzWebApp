let columns = document.getElementsByClassName("col");

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


let forwardButton = document.getElementById("forward");
let stopButton = document.getElementById("idle");
let backwardsButton = document.getElementById("backwards");


forwardButton.addEventListener("click", highlightForward);

stopButton.addEventListener("click", highlightIdle);

backwardsButton.addEventListener("click", highlightBackwards);

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


let rrSwitch = document.getElementById("chckbx");

document.getElementsByClassName("switch")[0].addEventListener("click", (e) => {
    console.log(rrSwitch.checked)
    railRoadSwitch();
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

document.onkeydown = (e) => {
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

        case "d":
            console.log("Rail Road Switch Status: switched");
            rrSwitch.checked = !rrSwitch.checked;
            railRoadSwitch();

        default:
            console.log(e.key);
        break;
    }
}